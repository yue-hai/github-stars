#!/usr/bin/env python3
"""Read public Stars only. Fail closed; never change account Stars."""
import argparse
import io
import subprocess
import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = 'yue-hai'
FIELDS = ['id', 'full_name', 'html_url', 'description', 'topics', 'archived', 'disabled', 'language', 'pushed_at', 'stargazers_count']

def open_api(request, timeout=30):
    try:
        return urllib.request.urlopen(request, timeout=timeout)
    except urllib.error.URLError:
        # Some environments reject Python TLS while curl works. Keep certificate
        # verification enabled; pass token via stdin config, never process argv.
        config = ['url = ' + json.dumps(request.full_url)]
        for key, value in request.header_items():
            config.append('header = ' + json.dumps(key + ': ' + value))
        result = subprocess.run(['curl', '--fail', '--silent', '--show-error', '--max-time', str(timeout), '--config', '-'], input=chr(10).join(config), text=True, capture_output=True, check=True)
        return io.StringIO(result.stdout)

def fetch(opener=open_api):
    items = []
    seen = set()
    for page in range(1, 101):
        url = f'https://api.github.com/users/{OWNER}/starred?per_page=100&page={page}&sort=created&direction=desc'
        headers = {'User-Agent': 'yuehai-star-library', 'Accept': 'application/vnd.github.star+json', 'X-GitHub-Api-Version': '2022-11-28'}
        token = os.environ.get('GITHUB_TOKEN')
        if token:
            headers['Authorization'] = 'Bearer ' + token
        with opener(urllib.request.Request(url, headers=headers), timeout=30) as response:
            rows = json.load(response)
        if not isinstance(rows, list):
            raise ValueError('API response is not a list')
        for row in rows:
            r = row.get('repo')
            if not isinstance(r, dict) or not isinstance(r.get('id'), int) or r.get('private') is not False:
                raise ValueError('Invalid or nonpublic repository')
            name = r.get('full_name', '')
            if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', name):
                raise ValueError('Invalid repository name')
            if r.get('html_url') != 'https://github.com/' + name:
                raise ValueError('Unexpected repository URL')
            if r['id'] in seen:
                raise ValueError('Duplicate ID; Stars may have changed while paging. Retry later.')
            if not isinstance(r.get('stargazers_count'), int) or not isinstance(row.get('starred_at'), str):
                raise ValueError('Incomplete metadata')
            seen.add(r['id'])
            items.append({'starred_at': row['starred_at'], 'repo': {k: r.get(k) for k in FIELDS}})
        if len(rows) < 100:
            return items
    raise ValueError('Pagination safety limit reached')

def normalize(items):
    return sorted([{'starred_at': x.get('starred_at', ''), 'repo': {k: x.get('repo', x).get(k) for k in FIELDS}} for x in items], key=lambda x: x['repo']['id'])

def plan(old, items, allow_large_drop=False):
    before = {x.get('repo', x)['id']: x.get('repo', x) for x in old['items']}
    after = {x['repo']['id']: x['repo'] for x in items}
    removed = set(before) - set(after)
    if before and (not after or len(removed) > max(5, len(before) * 0.2)) and not allow_large_drop:
        raise ValueError('Suspicious removal count. Old snapshot preserved; manual review required.')
    events = []
    for i in sorted(set(after) - set(before)):
        events.append({'type': 'added', 'id': i, 'name': after[i]['full_name']})
    for i in sorted(removed):
        events.append({'type': 'no_longer_publicly_visible', 'id': i, 'name': before[i]['full_name']})
    for i in sorted(set(before) & set(after)):
        if before[i]['full_name'] != after[i]['full_name']:
            events.append({'type': 'renamed', 'id': i, 'from': before[i]['full_name'], 'name': after[i]['full_name']})
    return normalize(old['items']) != normalize(items), events

def atomic_json(path, data):
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temp.replace(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--allow-large-drop', action='store_true', help='Only after manually confirming many removals')
    args = parser.parse_args()
    old = json.loads((ROOT / 'data/stars.json').read_text())
    # Complete two reads, comparing membership and names; refuse unstable snapshots.
    items = fetch()
    confirmation = fetch()
    identity = lambda xs: sorted((x['repo']['id'], x['repo']['full_name'], x['starred_at']) for x in xs)
    if identity(items) != identity(confirmation):
        raise ValueError('Stars changed during reading. Retry later; nothing written.')
    changed, events = plan(old, items, args.allow_large_drop)
    if not changed:
        print('No effective changes; timestamp preserved.')
        return
    now = datetime.now(timezone.utc).isoformat()
    history_path = ROOT / 'data/history.json'
    history = json.loads(history_path.read_text()) if history_path.exists() else []
    registry_path = ROOT / 'data/identities.json'
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}
    for x in old['items'] + items:
        r = x.get('repo', x)
        names = registry.setdefault(str(r['id']), [])
        if r['full_name'] not in names:
            names.append(r['full_name'])
    if events:
        history.append({'at': now, 'events': events})
    # Only public membership changes; disappearance is not proof of un-starring.
    atomic_json(registry_path, registry)
    atomic_json(history_path, history)
    atomic_json(ROOT / 'data/stars.json', {'owner': OWNER, 'fetched_at': now, 'scope': 'public-stars', 'items': normalize(items)})
    print(f'Synced {len(items)} public Stars; {len(events)} membership/name events.')

if __name__ == '__main__':
    main()

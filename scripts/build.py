#!/usr/bin/env python3
"""Build offline HTML and Markdown from public metadata + manual curation. No network."""
import csv
import html
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ['AI 与智能助手', '日常应用与效率', '媒体与内容处理', '服务器与自托管', '网络与连接', '设备与系统增强', '开发与技术资源', '签到与平台自动化', '通讯与机器人', '游戏与生活参考']

def load():
    snapshot = json.loads((ROOT / 'data/stars.json').read_text())
    curated = {}
    for row in csv.reader((ROOT / 'data/curation.tsv').read_text().splitlines(), delimiter='	'):
        if not row or row[0].startswith('#'):
            continue
        if len(row) != 6:
            raise ValueError(f'Expected six columns: {row}')
        name, category, subcategory, summary, tags, note = [s.strip() for s in row]
        if name.casefold() in curated or category not in CATEGORIES:
            raise ValueError(f'Duplicate or invalid classification: {name}')
        curated[name.casefold()] = dict(category=category, subcategory=subcategory, summary=summary, tags=tags.split(','), note=note)
    usage_path = ROOT / 'data/usage.tsv'
    usage = {}
    if usage_path.exists():
        for line in usage_path.read_text().splitlines():
            if not line or line.startswith('#'):
                continue
            name, explanation = line.split(chr(9), 1)
            if name.casefold() in usage:
                raise ValueError('Duplicate use case: ' + name)
            usage[name.casefold()] = explanation
    registry_path = ROOT / 'data/identities.json'
    registry = json.loads(registry_path.read_text()) if registry_path.exists() else {}
    by_id = {}
    for repo_id, names in registry.items():
        matches = [curated[n.casefold()] for n in names if n.casefold() in curated]
        if matches:
            by_id[int(repo_id)] = matches[-1]
    result = []
    seen = set()
    for item in snapshot['items']:
        r = item.get('repo', item)
        if r['id'] in seen:
            raise ValueError('Duplicate repository ID')
        seen.add(r['id'])
        name = r['full_name']
        c = curated.get(name.casefold()) or by_id.get(r['id']) or dict(category='待分类', subcategory='待复核', summary=r.get('description') or '暂无说明，待人工复核', tags=[], note='新项目尚未进行中文用途审核。')
        aliases = registry.get(str(r['id']), [])
        scenario = usage.get(name.casefold()) or next((usage[n.casefold()] for n in reversed(aliases) if n.casefold() in usage), '')
        c = dict(c, usage=scenario)
        status = '已归档' if r.get('archived') else '未归档'
        if name == 'leiurayer/downkyi':
            status = '停止维护'
        elif name == 'lllyasviel/Fooocus':
            status = '有限 LTS'
        result.append(dict(id=r['id'], name=name, url=r['html_url'], stars=r['stargazers_count'], language=r.get('language') or '未标注', pushed_at=r.get('pushed_at') or '', starred_at=item.get('starred_at') or '', status=status, **c))
    return snapshot, result

def mdcell(s):
    return html.escape(str(s), quote=False).replace('|', '&#124;').replace('\n', ' ')

def build():
    snapshot, rows = load()
    categories = CATEGORIES + (['待分类'] if any(r['category'] == '待分类' for r in rows) else [])
    counts = Counter(r['category'] for r in rows)
    date = snapshot['fetched_at'][:10]
    from markdown_catalog import write_catalog
    write_catalog(ROOT, snapshot, rows, categories)
    template = (ROOT / 'templates/index.html').read_text()
    payload = json.dumps(dict(date=date, categories=categories, rows=rows), ensure_ascii=False).replace('<', chr(92) + 'u003c').replace('>', chr(92) + 'u003e').replace('&', chr(92) + 'u0026')
    (ROOT / 'index.html').write_text(template.replace('__LIBRARY_DATA__', payload))
    (ROOT / 'data/catalog.json').write_text(json.dumps(dict(date=date, rows=rows), ensure_ascii=False, indent=2) + '\n')
    print(f'Built {len(rows)} items; {len(categories)} categories; {sum(r["category"] == "待分类" for r in rows)} pending')
    for category in categories:
        print(f'{category}: {counts[category]}')

if __name__ == '__main__':
    build()

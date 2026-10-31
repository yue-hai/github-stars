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
    md = ['# 月海的 GitHub 收藏导航', '', f'账号：[yue-hai](https://github.com/yue-hai?tab=stars) · **{len(rows)} 个公开 Star** · 快照日期：{date}（UTC）', '', '> 按用途找项目，而不是在收藏列表里翻页。中文说明是整理判断，不代表已安装、推荐或安全审计。', '', '## 怎么查找', '', '- **在 GitHub 里**：使用下方分类目录，或浏览器 Ctrl/Cmd+F 搜索项目名、中文用途、平台和标签。', '- **离线查找**：下载本仓库后直接打开 [搜索网页](index.html)，可按关键词、分类、标签、状态筛选和排序，不需要服务器。', '- **手工维护**：[分类与中文说明](data/curation.tsv) 是人工维护源；[原始快照](data/stars.json) 保存公开 API 数据。', '', '## 分类目录', '', '| 分类 | 数量 |', '| --- | ---: |']
    for i, c in enumerate(categories, 1):
        md.append(f'| [{c}](#category-{i}) | {counts[c]} |')
    md += ['', '## 值得留意', '', '- **停止维护**：[downkyi](https://github.com/leiurayer/downkyi#readme) 的 README 已明确宣布停止维护；API 的未归档状态不等于仍在维护。', '- **有限 LTS**：[Fooocus](https://github.com/lllyasviel/Fooocus#readme) 声明仅修复 Bug，暂无新模型架构迁移计划。', '- **已归档**：' + '、'.join(f'[{r["name"]}]({r["url"]})' for r in rows if r['status'] == '已归档') + '。', '- **同名与配套项目**：两份 Cloud189Checkin 分别保留作者；NapCat 与 Docker 部署、n2n 与 Windows GUI、Fooocus 与汉化补丁都分别列出。', '- **状态边界**：“未归档”仅指 API 字段；最近推送不等于最近发布，也不保证软件仍可用。', '']
    for i, c in enumerate(categories, 1):
        md += [f'<a id="category-{i}"></a>', f'## {c}（{counts[c]}）', '']
        group = [r for r in rows if r['category'] == c]
        for sub in dict.fromkeys(r['subcategory'] for r in group):
            md += [f'### {sub}', '', '| 项目 | 中文用途 | 标签 | 状态 / 备注 |', '| --- | --- | --- | --- |']
            for r in sorted((r for r in group if r['subcategory'] == sub), key=lambda x: x['name'].casefold()):
                note = (r['status'] + '；' if r['status'] != '未归档' else '') + r['note']
                md.append(f'| [{r["name"]}]({r["url"]}) | {mdcell(r["summary"])} | {mdcell(" / ".join(r["tags"]))} | {mdcell(note or "—")} |')
            md.append('')
    md += ['## 更新与来源', '', '- [公开仓库](https://github.com/yue-hai/github-stars) · [同步运行记录](https://github.com/yue-hai/github-stars/actions/workflows/sync.yml)：每日北京时间 09:17 左右同步，也支持手动运行；实际执行以 Actions 记录为准。', '- 数据来自 GitHub 公开 Star API；不包含私有仓库 Star，也没有更改 GitHub 上的收藏。', '- 初次整理的 100 项已逐项写中文用途与主分类；描述不足的 7 项补读 README。后续新增项目先显示待分类，不代表已完成中文审核。', '- 构建：Python 3.9+ 执行 \u0060python3 scripts/build.py\u0060；不联网、不安装依赖。', '- 后续同步方案见 [维护说明](docs/维护说明.md)。', '- 原项目代码和资料的许可归各自作者；本目录只索引，不复制分发软件。', '']
    text = '\n'.join(md).replace('\u0060', chr(96))
    (ROOT / 'README.md').write_text(text)
    template = (ROOT / 'templates/index.html').read_text()
    payload = json.dumps(dict(date=date, categories=categories, rows=rows), ensure_ascii=False).replace('<', chr(92) + 'u003c').replace('>', chr(92) + 'u003e').replace('&', chr(92) + 'u0026')
    (ROOT / 'index.html').write_text(template.replace('__LIBRARY_DATA__', payload))
    (ROOT / 'data/catalog.json').write_text(json.dumps(dict(date=date, rows=rows), ensure_ascii=False, indent=2) + '\n')
    print(f'Built {len(rows)} items; {len(categories)} categories; {sum(r["category"] == "待分类" for r in rows)} pending')
    for category in categories:
        print(f'{category}: {counts[category]}')

if __name__ == '__main__':
    build()

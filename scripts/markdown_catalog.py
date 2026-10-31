"""GitHub-native catalog: generated Markdown, no deployment required."""
import html
import re
from collections import Counter
from urllib.parse import quote

SLUGS = ['ai', 'productivity', 'media', 'self-hosted', 'network', 'devices', 'development', 'automation', 'communication', 'games-and-life']

GUIDES = dict(zip(SLUGS, [
    '想接入工具、扩展助手能力，先看 Agent 与扩展；需要聊天界面看聊天客户端；本地绘图和 SVG 生成看图像分区。模型、聊天前端、插件清单是不同层次的项目。',
    '收录日常直接使用的应用与插件。跨设备复制和剪贴板历史放一起比较；输入法方案、输入法应用和 Obsidian 插件分别说明；社区客户端按实际平台选择。',
    '按处理流程选择：播放器、转码、录屏与字幕工具在音视频分区；下载与投稿工具在下载与发布分区。上传、下载、字幕识别和字幕编辑不是同一种能力。',
    '既有可部署服务，也有项目清单和运维客户端。找软件先看部署资源；管理主机看远程与监控；统一文件入口和同步看导航与文件服务。',
    '代理客户端、DDNS、虚拟组网和 Hosts 工具解决不同连接问题。先明确是代理配置、动态域名更新还是设备互联，不要仅因都涉及网络就互相替代。',
    '按桌面外设、Android 模块、系统授权及智能家居区分。系统模块和支付相关工具权限较高；功能说明不表示设备兼容或安全性已验证。',
    '开发组件需要集成进自己的代码，API 和免费服务清单是寻找资源的入口，课程与书籍则用于学习；不是这里每个仓库都能作为独立软件安装。',
    '区分执行签到的脚本、取得登录态的工具、请求模板以及话费监控。通常需要已有框架和账户配置，不应把 Cookie、HAR 或账号数据上传到本公开目录。',
    '这里是 QQ 协议接入、容器部署和 PC 客户端增强。NapCat 为上层机器人提供接口；需要 AI 对话时还应结合 AI 分类中的助手项目。',
    '游戏任务助手与验证工具放在游戏分区；食谱、健康与社会资料放在参考资料分区。自动化、游戏 Mod 和生活参考各有使用边界，详见条目备注。'
]))

def text(value):
    s = html.escape(str(value), quote=False).replace(chr(10), ' ')
    return re.sub(r'([\\*_[\]~])', lambda m: chr(92) + m.group(0), s)

def item_lines(r):
    status = ' · **' + text(r['status']) + '**' if r['status'] != '未归档' else ''
    lines = [f'- **[{r["name"]}]({r["url"]})**{status}', '', '  **功能**：' + text(r["summary"])]
    if r.get('usage'):
        lines += ['', '  **适用场景**：' + text(r['usage'])]
    if r['tags']:
        lines += ['', '  **标签**：' + ' · '.join(chr(96) + t.replace(chr(96), '') + chr(96) for t in r['tags'])]
    if r['note'] and r['note'] != '—':
        lines += ['', '  <details>', '  <summary>备注与使用提醒</summary>', '', '  ' + text(r['note']), '', '  </details>']
    lines.append('')
    return lines

def write_catalog(root, snapshot, rows, categories):
    out = root / 'catalog'
    out.mkdir(exist_ok=True)
    counts = Counter(r['category'] for r in rows)
    paths = {c: f'{SLUGS[i] if i < len(SLUGS) else "pending"}.md' for i, c in enumerate(categories)}
    # Keep pending page stable even when no repository needs classification.
    paths['待分类'] = 'pending.md'
    date = snapshot['fetched_at'][:10]
    nav = ['# 月海的 GitHub 收藏导航', '', f'**{len(rows)} 个公开收藏 · {len(categories)} 个分类** · 内容快照 {date}（UTC）', '', '> 按用途找工具，直接在 GitHub 浏览。无需安装、登录第三方服务或部署应用。', '', '[全部收藏](catalog/all.md) · [待分类](catalog/pending.md) · [同步记录](https://github.com/yue-hai/github-stars/actions/workflows/sync.yml) · [维护说明](docs/维护说明.md)', '', '## 按用途浏览', '']
    full = ['# 全部收藏', '', '[← 返回首页](../README.md)', '', f'共 {len(rows)} 项。用浏览器 Ctrl/Cmd+F 搜索中文用途、项目名或标签。长备注可展开。', '']
    for c in categories:
        group = [r for r in rows if r['category'] == c]
        subs = list(dict.fromkeys(r['subcategory'] for r in group))
        nav.append(f'- **[{c}](catalog/{paths[c]})** · {counts[c]} 项<br>')
        nav.append('  ' + ' / '.join(subs) + '<br>')
        nav.append('  ' + GUIDES.get(paths[c][:-3], '新收藏的临时入口，等待用途核对与分类。'))
        nav.append('')
        body = [f'# {c}', '', '[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)', '', f'共 {len(group)} 项 · 快照 {date}（UTC）。按用途分组；平台和技术见标签。', '']
        body += [GUIDES.get(paths[c][:-3], '新收藏尚未完成中文用途审核。'), '']
        body += [f'- [{sub}](#section-{i})' for i, sub in enumerate(subs, 1)] + ['']
        section = []
        for i, sub in enumerate(subs, 1):
            body += [f'<a id="section-{i}"></a>']
            block = ['## ' + sub, '']
            for r in sorted((r for r in group if r['subcategory'] == sub), key=lambda r: r['name'].casefold()):
                block += item_lines(r)
            body += block
            section += block
        (out / paths[c]).write_text(chr(10).join(body), encoding='utf-8')
        full += ['# ' + c, ''] + section
    if not any(r['category'] == '待分类' for r in rows):
        (out / 'pending.md').write_text('# 待分类'+chr(10)*2+'[← 返回首页](../README.md)'+chr(10)*2+'目前没有待分类项目。新收藏同步后会先显示在这里，等待补充中文用途和准确分类。'+chr(10), encoding='utf-8')
    (out / 'all.md').write_text(chr(10).join(full), encoding='utf-8')
    recent = sorted(rows, key=lambda r: r['starred_at'], reverse=True)[:8]
    nav += ['## 最近收藏', '', '按 GitHub 收藏时间展示最近 8 项，不代表本次同步新增。', '']
    for r in recent:
        path = paths[r['category']]
        nav.append(f'- [{r["name"]}]({r["url"]}) — {text(r["summary"])}<br>')
        nav.append(f'  <sub>{r["starred_at"][:10] or "时间未知"} · <a href="catalog/{path}">{html.escape(r["category"])}</a></sub>')
    special = [r for r in rows if r['status'] != '未归档']
    nav += ['', '<details>', '<summary>维护状态提醒（' + str(len(special)) + ' 项）</summary>', '']
    for r in special:
        nav.append(f'- [{r["name"]}]({r["url"]})：**{text(r["status"])}**。详见[分类备注](catalog/{paths[r["category"]]})。')
    nav += ['', '“未归档”不等于仍活跃；收藏也不代表安全推荐。', '', '</details>', '', '## 查找与更新', '', '- **找工具**：从用途分类进入；想一次搜索全部内容，打开[全部收藏](catalog/all.md)后按 Ctrl/Cmd+F。', '- **仓库内搜索**：使用 GitHub 搜索，例如 ' + chr(96) + 'repo:yue-hai/github-stars path:catalog 剪贴板' + chr(96) + '；代码索引可能延迟。', '- **自动同步**：每天北京时间 **09:17 左右**检查，GitHub 调度可能延迟；可在 Actions 手动运行。', '- **新收藏**：先进入待分类；已有人工用途和备注不会被自动覆盖。', '- **变更追溯**：[收藏变化数据](data/history.json)与 Git 提交历史保留记录；项目从公开列表消失不一定意味着取消 Star。', '', '<details>', '<summary>数据来源与可选离线工具</summary>', '', '仅收录公开 Star。初次 100 项经人工整理，描述不足的 7 项补读 README；不代表逐一实测或源码审计。', '', '[中文分类源数据](data/curation.tsv) · [公开快照](data/stars.json) · [可选离线搜索网页](index.html)（下载后打开；不是在线应用）', '', '原项目代码及资料的许可归各自作者。本仓库只作索引。', '', '</details>', '']
    (root / 'README.md').write_text(chr(10).join(nav), encoding='utf-8')

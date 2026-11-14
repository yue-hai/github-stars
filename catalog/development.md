# 开发与技术资源

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 12 项 · 快照 2026-11-14（UTC）。按用途分组；平台和技术见标签。

开发组件需要集成进自己的代码，API 和免费服务清单是寻找资源的入口，课程与书籍则用于学习；不是这里每个仓库都能作为独立软件安装。

- [开发工具与组件](#section-1)
- [学习资料](#section-2)
- [API 与免费资源](#section-3)

<a id="section-1"></a>
## 开发工具与组件

- **[dotnetcore/AgileConfig](https://github.com/dotnetcore/AgileConfig)**

  **主要功能**：.NET分布式配置中心，集中管理多应用配置并向客户端推送更改；需部署服务端并集成客户端，存储和依赖依版本设置。

  **适用场景**：多个应用需要集中管理配置、减少逐台修改配置文件时参考，尤其适合进一步评估 .NET 技术栈的配置中心方案。

  **标签**：`.NET` · `配置管理`

- **[hlmd/Postman-cn](https://github.com/hlmd/Postman-cn)**

  **主要功能**：Postman旧版中文化资源和安装说明，README指向后续注入器项目；不是官方中文发行版，传统替换方式不适配新版且仓库停更。

  **适用场景**：希望查找 Postman 汉化资料时参考；第三方汉化与官方产品更新可能不同步，且仓库已归档。

  **标签**：`API` · `Postman` · `汉化`

  <details>
  <summary>备注与使用提醒</summary>

  仓库已归档；不是官方中文版本的保证。

  </details>

- **[Hufe921/canvas-editor](https://github.com/Hufe921/canvas-editor)**

  **主要功能**：Canvas/SVG富文本编辑器组件，可集成到Web应用实现文档编辑；属于开发组件，不是独立办公套件。

  **适用场景**：开发 Web 文档编辑功能、需要基于 Canvas/SVG 的富文本编辑器组件时参考；这是开发组件，不是独立 Office 套件。

  **标签**：`编辑器` · `Canvas` · `TypeScript`

- **[markedjs/marked](https://github.com/markedjs/marked)**

  **主要功能**：JavaScript Markdown解析/编译库，支持浏览器、Node和CLI转HTML并扩展语法；不会清理HTML，渲染不可信内容需额外消毒。

  **适用场景**：开发网页或文档工具、需要把 Markdown 文本转换为 HTML 时使用；输出中的不可信 HTML 仍需按应用需求做安全处理。

  **标签**：`Markdown` · `JavaScript`

- **[sindresorhus/github-markdown-css](https://github.com/sindresorhus/github-markdown-css)**

  **主要功能**：为已渲染Markdown提供GitHub风格CSS主题，支持明暗呈现；只负责样式，不解析Markdown。

  **适用场景**：自己做文档页面、希望 Markdown 内容接近 GitHub 阅读样式时参考；它只负责样式，不负责解析文本。

  **标签**：`Markdown` · `CSS`

- **[xbeeant/downstash](https://github.com/xbeeant/downstash)**

  **主要功能**：本地模拟QStash/Redis REST API，支持延时、重试、签名回调、队列、死信和cron；适合Bun离线测试，不是生产队列。

  **适用场景**：开发依赖 QStash 的任务投递功能时，可在本地模拟其 API，减少离线开发和测试对远端服务的依赖。

  **标签**：`API` · `测试`

<a id="section-2"></a>
## 学习资料

- **[caoaolong/coding-soul-docs](https://github.com/caoaolong/coding-soul-docs)**

  **主要功能**：编程课程文档，含手写操作系统、编译器/语言实现及Godot示例，主要供阅读学习，不是软件应用。

  **适用场景**：学习 CodingSoul 系列课程、查找对应技术说明时参考；它属于学习资料，不是可直接使用的软件应用。

  **标签**：`编程` · `教程`

- **[EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books)**

  **主要功能**：按语言/主题整理免费编程书籍和课程链接，可浏览搜索；它是资源索引不是完整课程，链接、授权和质量需分别核对。

  **适用场景**：学习某种语言或技术、需要寻找免费书籍和课程资源时使用；它是资料索引，不是一套按顺序编排的统一课程。

  **标签**：`编程` · `书籍` · `资源清单`

<a id="section-3"></a>
## API 与免费资源

- **[public-apis/public-apis](https://github.com/public-apis/public-apis)**

  **主要功能**：按主题汇总公开API和数据服务链接，涵盖多个类别，供开发者查找接口；它是社区清单，不负责运行服务，也不保证免费或持续可用。需核实各API条款、认证、额度和隐私政策。

  **适用场景**：做原型或小项目、需要寻找某类数据接口时作为入口；每个接口的授权、收费与调用限制仍需去原站核对。

  **标签**：`API` · `资源清单`

- **[ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev)**

  **主要功能**：汇集面向开发者的免费服务与免费层资源，覆盖云、托管、API、开发工具等，并规定收录条件；只纳入符合标准的服务，不是自托管软件清单。免费额度可能变化。

  **适用场景**：给个人开发项目选云服务、托管、数据库等基础资源时比较免费额度；免费条件可能随供应商政策变化。

  **标签**：`云服务` · `资源清单`

- **[tvvocold/free-for-dev-zh](https://github.com/tvvocold/free-for-dev-zh)**

  **主要功能**：中文开发工具和免费服务索引，便于寻找国内或中文资料；额度、地区支持及可用性需回到服务商核实。

  **适用场景**：更希望先查中文或国内开发资源时参考；可与 free-for-dev 对照，具体优惠与可用范围以服务商当前说明为准。

  **标签**：`资源清单` · `中文`

- **[vikiboss/60s](https://github.com/vikiboss/60s)**

  **主要功能**：开放API集合，重点提供每日新闻，也含文档列出的其他数据接口；新闻端点可返回JSON、文本或图片，数据定时抓取并缓存。公共主站额度有限并严格限流；生产建议自部署，支持Docker/Workers/Deno/Bun/Node等。

  **适用场景**：给个人主页、机器人或小工具接入新闻、热搜、天气等信息时查找接口；接入前核对具体端点、频率限制与服务可用性。

  **标签**：`API` · `自托管`

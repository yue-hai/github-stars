# AI 与智能助手

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 11 项 · 快照 2026-11-14（UTC）。按用途分组；平台和技术见标签。

想接入工具、扩展助手能力，先看 Agent 与扩展；需要聊天界面看聊天客户端；本地绘图和 SVG 生成看图像分区。模型、聊天前端、插件清单是不同层次的项目。

- [Agent 与扩展](#section-1)
- [聊天客户端](#section-2)
- [图像与 SVG](#section-3)

<a id="section-1"></a>
## Agent 与扩展

- **[AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot)**

  **主要功能**：一体化Agent聊天机器人平台，可接QQ、企业微信、飞书、钉钉、Telegram等IM，支持多模型、多模态、MCP、技能、知识库、插件、WebUI/Web ChatUI及沙箱。可uv或Docker部署；平台和模型需另行配置。

  **适用场景**：需要在 QQ、Telegram 等聊天平台接入 AI 助手并通过插件扩展时参考；它负责助手与平台集成，不等于 QQ 协议端本身。

  **标签**：`机器人` · `QQ` · `MCP`

- **[awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)**

  **主要功能**：DSH插件目录，可浏览或用DSH命令发现/添加；需兼容版本，收录不等于安全审查。

  **适用场景**：给 DSH 找扩展能力时先查这份目录，再进入具体插件仓库核对功能、安装方式与维护情况。

  **标签**：`DSH` · `资源清单`

- **[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)**

  **主要功能**：插件化Agent环境，支持Web/headless编码Agent及模型/工具/沙箱/会话扩展；需Node.js，README称preview并提示安全及兼容变化。

  **适用场景**：希望在一个可扩展的 AI 工作环境里组合工具与插件时参考；插件生态和使用入口可结合收藏中的插件清单查看。

  **标签**：`DSH` · `Agent`

- **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)**

  **主要功能**：轻量自托管Python个人AI Agent，可在Web、终端及Telegram/Discord/Slack/微信等渠道工作，支持文件处理、工具/MCP、搜索、定时、多代理、长期记忆和SDK/API。需Python 3.11+及模型服务；硬件和模型费用自备，stable与current source文档可能不同。

  **适用场景**：想尝试轻量个人 AI 助手，或研究 Agent 如何连接聊天平台与工具时参考；实际能力取决于模型和接入配置。

  **标签**：`Agent` · `自托管`

- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)**

  **主要功能**：MCP服务器/客户端/教程/框架及托管平台分类目录，供AI集成选型；不是单一服务，安全和维护需逐项审核。

  **适用场景**：想让 AI 接入文件、数据库、搜索或其他外部系统时，用它寻找 MCP 服务候选；清单本身不提供全部服务。

  **标签**：`MCP` · `资源清单`

<a id="section-2"></a>
## 聊天客户端

- **[ChatGPTNextWeb/NextChat](https://github.com/ChatGPTNextWeb/NextChat)**

  **主要功能**：跨平台AI聊天前端，连接配置的模型服务并提供Web/桌面交互；供应商、账户和费用取决于当前配置。

  **适用场景**：想在 Web 或桌面上使用统一 AI 聊天界面时参考；模型与服务接入方式以当前版本为准，不把宣传语视为永久免费承诺。

  **标签**：`LLM` · `聊天`

- **[LiLittleCat/awesome-free-chatgpt](https://github.com/LiLittleCat/awesome-free-chatgpt)**

  **主要功能**：第三方ChatGPT镜像/服务链接目录，可浏览并反馈新增/失效；非官方，站点可能收费或变更，勿输入敏感信息。

  **适用场景**：想了解第三方 ChatGPT 镜像站线索时参考；不是官方客户端，站点是否可用、收费以及如何处理输入内容需单独核对。

  **标签**：`ChatGPT` · `资源清单`

  <details>
  <summary>备注与使用提醒</summary>

  第三方站点可用性与隐私未验证，不提交敏感信息。

  </details>

- **[SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern)**

  **主要功能**：本地安装的统一界面，可连接文本LLM、图像生成与TTS服务，提供角色/提示词交互、视觉小说模式、世界信息、移动布局及第三方扩展；不托管模型。需Node.js 20+，本地推理硬件要求由模型后端决定。

  **适用场景**：希望更细致地管理与大模型的聊天交互时参考。它属于前端，不是模型本身，仍需配置可用的模型后端。

  **标签**：`LLM` · `聊天`

<a id="section-3"></a>
## 图像与 SVG

- **[joanrod/star-vector](https://github.com/joanrod/star-vector)**

  **主要功能**：视觉语言模型项目，可将图像或文字转换为SVG代码；需模型环境，不是普通矢量编辑器。

  **适用场景**：需要研究将图片或文字转换为可编辑 SVG 的模型方案时参考；它更接近生成模型项目，不是普通矢量编辑器。

  **标签**：`SVG` · `生成模型`

- **[lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus)** · **有限 LTS**

  **主要功能**：本地SDXL图像生成，支持文生图、图生图、放大、修补/扩图、图像提示；需模型与显存/内存，有限LTS主要修Bug，远程Web默认无认证。

  **适用场景**：想在本地围绕提示词生成图像、减少手动调参时参考；基于 SDXL，有限 LTS 状态下不宜期待持续接入新模型架构。

  **标签**：`绘图` · `SDXL` · `本地部署`

  <details>
  <summary>备注与使用提醒</summary>

  README 声明有限 LTS，仅修复 Bug，暂无迁移新模型架构计划。

  </details>

- **[SoftMeng/Fooocus-zh](https://github.com/SoftMeng/Fooocus-zh)**

  **主要功能**：Fooocus简体中文语言包，安装到相应语言目录并按参数启用；需兼容Fooocus，本身不是生成程序或模型。

  **适用场景**：已经使用 Fooocus、需要中文界面相关补丁时参考；需匹配 Fooocus 版本，不能当作独立图像生成软件使用。

  **标签**：`Fooocus` · `汉化`

  <details>
  <summary>备注与使用提醒</summary>

  配套补丁，不是独立绘图模型。

  </details>

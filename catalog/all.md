# 全部收藏

[← 返回首页](../README.md)

共 101 项。用浏览器 Ctrl/Cmd+F 搜索中文用途、项目名或标签。长备注可展开。

# AI 与智能助手

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

# 日常应用与效率

## 剪贴板与跨设备

- **[CrossPaste/crosspaste-desktop](https://github.com/CrossPaste/crosspaste-desktop)**

  **主要功能**：跨平台局域网剪贴板同步，README列端到端加密、OCR、CLI和MCP；参与设备需安装且网络可达。

  **适用场景**：经常在多台电脑之间复制文字或文件内容时参考，重点是跨设备剪贴板流转；区别于主要管理单机剪贴板历史的 CopyQ。

  **标签**：`剪贴板` · `跨设备`

- **[hluk/CopyQ](https://github.com/hluk/CopyQ)**

  **主要功能**：跨平台剪贴板管理器，可记录多种格式、搜索筛选、编辑、标签、快捷键、命令和脚本，适合本机历史管理；不等同跨设备同步。

  **适用场景**：经常重复复制粘贴、需要找回剪贴板历史或编写剪贴板处理脚本时参考；跨电脑同步可另看 CrossPaste。

  **标签**：`剪贴板` · `跨平台`

## 输入法与笔记

- **[guopenghui/obsidian-quiet-outline](https://github.com/guopenghui/obsidian-quiet-outline)**

  **主要功能**：Obsidian大纲增强，README列标题搜索/正则、层级折叠及状态记忆、Canvas/Kanban/PDF导航、悬停预览；未说明最低版本。

  **适用场景**：Obsidian 笔记标题层级多、需要改善大纲浏览体验时参考；与管理文件树折叠的 Collapse All 插件用途不同。

  **标签**：`Obsidian` · `大纲`

- **[gurecn/YuyanIme](https://github.com/gurecn/YuyanIme)**

  **主要功能**：Android Rime输入法，支持九宫格/双拼/手写、剪贴板短语、主题及悬浮键盘；需Android 6+，厂商权限有影响。

  **适用场景**：在 Android 上需要 Rime 输入能力，并想使用九键、双拼、手写或单手布局时参考；与雾凇拼音的配置层用途不同。

  **标签**：`Android` · `Rime`

- **[iDvel/rime-ice](https://github.com/iDvel/rime-ice)**

  **主要功能**：离线即用的简体中文Rime输入方案与词库，覆盖全拼、常见双拼、英文和扩展输入，适配Weasel、Squirrel、Fcitx5、iBus等Rime客户端。需先安装Rime并部署配置；部分双拼方案或语言模型需额外设置。

  **适用场景**：正在配置 Rime、需要简体中文拼音方案与词库时使用；它是输入方案和配置，不是单独安装即可运行的完整输入法应用。

  **标签**：`Rime` · `拼音`

- **[nathonius/obsidian-collapse-all](https://github.com/nathonius/obsidian-collapse-all)**

  **主要功能**：Obsidian文件树、标签、搜索、书签折叠/展开命令，可由命令面板或热键调用；README指出Search没有toggle，Bookmarks主要toggle且可能不稳定。

  **适用场景**：Obsidian 文件树、标签或搜索视图层级较多时，用折叠与展开命令减少逐项点击，也可绑定快捷键。

  **标签**：`Obsidian` · `插件`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对，主要作用于文件树等视图。

  </details>

## 社区客户端

- **[Richasy/Bili.Copilot](https://github.com/Richasy/Bili.Copilot)**

  **主要功能**：Windows第三方B站客户端，README列登录/播放、AI总结问答及BBDown/FFmpeg下载混流；部分AI需字幕，下载受架构和FFmpeg条件影响。

  **适用场景**：希望在 Windows 上通过原生桌面界面浏览 B 站时参考；它是观看与浏览类客户端，不是投稿工具。

  **标签**：`Windows` · `B站`

- **[TG-Twilight/c001apk](https://github.com/TG-Twilight/c001apk)**

  **主要功能**：非官方酷安客户端，可看动态、文章、评论和搜索，管理收藏/屏蔽/历史及多账号；验证码流程有限，跨版本迁移受限。

  **适用场景**：想在 Android 上浏览酷安社区、尝试非官方客户端时查阅；它是社区客户端，不是应用商店或手机管理工具。

  **标签**：`Android` · `酷安`

- **[zhihulite/Hydrogen](https://github.com/zhihulite/Hydrogen)**

  **主要功能**：基于LuaJVM的知乎第三方客户端工程，使用Lua业务层与Android原生API桥接，含网络请求、缓存、下载、主题和WebView等模块。README标注维护延缓，Final 7已存档停止维护；下载APK需核对来源。

  **适用场景**：希望在 Android 上通过第三方应用浏览知乎时参考；功能与登录兼容性取决于知乎接口及项目适配。

  **标签**：`Android` · `知乎`

# 媒体与内容处理

## 音视频与字幕

- **[Lake1059/FFmpegFreeUI](https://github.com/Lake1059/FFmpegFreeUI)**

  **主要功能**：Windows FFmpeg GUI，可组合参数、预设、批处理、估算时间体积、暂停和字幕/混流；需兼容Windows/.NET并自备FFmpeg。

  **适用场景**：需要压缩视频、转换媒体格式，又不想手写复杂 FFmpeg 命令时参考；界面用于组织转换参数和执行任务。

  **标签**：`Windows` · `FFmpeg`

- **[NickeManarin/ScreenToGif](https://github.com/NickeManarin/ScreenToGif)**

  **主要功能**：录制屏幕区域、摄像头或绘图板，逐帧编辑并导出GIF/APNG/视频/PSD/PNG序列；需要兼容的.NET/Windows环境，适合教程与问题复现。

  **适用场景**：需要录制一小段屏幕操作、编辑后导出 GIF 或视频来说明问题时参考，适合教程和问题反馈素材。

  **标签**：`Windows` · `录屏` · `GIF`

- **[rRemix/APlayer](https://github.com/rRemix/APlayer)**

  **主要功能**：Android音乐播放器，可按歌曲/艺人/专辑/目录/播放列表浏览，含歌词、小组件、媒体扫描和封面；系统要求以当前版本为准。

  **适用场景**：想在 Android 设备上找音乐播放应用时参考；支持格式、媒体来源和设备兼容性需以当前版本说明为准。

  **标签**：`Android` · `音乐`

- **[SubtitleEdit/subtitleedit](https://github.com/SubtitleEdit/subtitleedit)**

  **主要功能**：字幕编辑、校时、播放、格式转换和备份，并有可选翻译、语音识别和OCR；在线服务可能处理字幕/媒体数据。

  **适用场景**：需要修改字幕文本和时间轴、处理现有字幕文件时参考；和主要通过语音识别生成字幕的工具侧重点不同。

  **标签**：`字幕` · `编辑`

- **[wxbool/video-srt-windows](https://github.com/wxbool/video-srt-windows)**

  **主要功能**：Windows GUI调用语音识别生成SRT/文本，支持批处理、过滤和翻译；云端API需账号/密钥，不同版本功能不同并可能上传媒体/文本。

  **适用场景**：手头只有视频、希望先用语音识别生成 SRT 字幕再人工校对时参考；识别服务可用性和当前兼容性需核对。

  **标签**：`Windows` · `字幕` · `语音识别`

## 下载与发布

- **[404-novel-project/novel-downloader](https://github.com/404-novel-project/novel-downloader)**

  **主要功能**：浏览器用户脚本，可从支持小说页面导出TXT/EPUB并按站点取章节；需用户脚本管理器，部分站点需登录/已购，需核对版权与README披露的数据处理。

  **适用场景**：需要按可扩展站点适配方式保存小说文本时参考；是否允许下载和保存需核对内容版权与站点规则。

  **标签**：`小说` · `下载`

  <details>
  <summary>备注与使用提醒</summary>

  获取内容前核对版权和平台规则。

  </details>

- **[agalwood/Motrix](https://github.com/agalwood/Motrix)**

  **主要功能**：桌面下载管理器支持HTTP/FTP/BT/Magnet，含BT文件选择、Tracker更新、并行任务、限速和通知；安装依平台，下载依网络。

  **适用场景**：希望在桌面上统一管理 HTTP、BT、磁力链接下载任务时参考；与放在 Linux 主机上的迅雷远程服务分开选择。

  **标签**：`下载` · `跨平台`

- **[biliup/biliup-app](https://github.com/biliup/biliup-app)** · **已归档**

  **主要功能**：B站投稿客户端，旧版支持多P上传、线路/并发控制和稿件编辑；仓库已归档停更并迁往新项目，不是视频下载器。

  **适用场景**：需要向 B 站投稿、编辑稿件或管理多 P 上传时参考；它不是从 B 站下载视频的工具，并且仓库已归档。

  **标签**：`B站` · `投稿`

  <details>
  <summary>备注与使用提醒</summary>

  仓库已归档；这是上传投稿工具，不是视频下载器。

  </details>

- **[cnk3x/xunlei](https://github.com/cnk3x/xunlei)**

  **主要功能**：从群晖迅雷套件提取的Linux远程下载服务，提供网页控制台并支持本地/Docker；README标为测试版、未大规模验证，仅供研究测试。

  **适用场景**：需要在 NAS 之外的 Linux 主机上使用迅雷远程下载时参考；与桌面下载器 Motrix 的交互和账号依赖不同。

  **标签**：`Linux` · `迅雷` · `Docker`

- **[leiurayer/downkyi](https://github.com/leiurayer/downkyi)** · **停止维护**

  **主要功能**：README明确Deprecated并宣布永久停更，仅供历史参考，不作当前可用工具推荐；README里的法律事项为开发者转述，不代表法院裁定。

  **适用场景**：保留曾用于 B 站下载的项目线索与停更信息，不作为当前仍可用的下载方案推荐。

  **标签**：`B站` · `历史参考`

  <details>
  <summary>备注与使用提醒</summary>

  README 明确宣布停止维护并永久关停；不能因为 archived=false 就判为仍维护。

  </details>

# 服务器与自托管

## 远程管理与监控

- **[gnmyt/Nexterm](https://github.com/gnmyt/Nexterm)**

  **主要功能**：README列SSH/VNC/RDP连接、SFTP文件管理、Docker部署、Proxmox管理、2FA/OIDC及组织隔离；支持Docker和客户端，公网需加固。

  **适用场景**：需要集中访问多台机器的 SSH、VNC、RDP 连接时参考；重点是远程会话管理，与只看服务器指标的监控组件不同。

  **标签**：`SSH` · `VNC` · `RDP`

- **[kingToolbox/WindTerm](https://github.com/kingToolbox/WindTerm)**

  **主要功能**：跨平台终端支持SSH/Telnet/TCP/串口/Shell，并集成SFTP/SCP、本地文件管理、SSH转发/代理和tmux；README说明开源范围有限。

  **适用场景**：经常通过 SSH、SFTP、串口等方式维护设备或服务器时参考，重点是跨平台终端与远程操作。

  **标签**：`SSH` · `终端` · `SFTP`

- **[lollipopkit/flutter_server_box](https://github.com/lollipopkit/flutter_server_box)**

  **主要功能**：移动端ServerBox客户端/工具箱，可查看服务器状态并通过SSH等方式管理主机；需配置主机和认证，保护密钥/密码。

  **适用场景**：需要在移动端查看服务器状态、使用服务器管理工具箱时参考；与 server\_box\_monitor 配套关系需按具体功能核对。

  **标签**：`SSH` · `监控` · `移动端`

- **[lollipopkit/server_box_monitor](https://github.com/lollipopkit/server_box_monitor)**

  **主要功能**：ServerBox配套服务端监控组件，在服务器侧采集状态供客户端查看；需配置认证并限制网络暴露。

  **适用场景**：使用 ServerBox 生态、需要在被监控服务器上放置配套监控端时参考；它不是用户日常操作的完整客户端。

  **标签**：`监控` · `服务器`

## 部署资源与容器

- **[coracoo/awesome_docker_cn](https://github.com/coracoo/awesome_docker_cn)**

  **主要功能**：中文Docker部署项目/教程目录，按类别提供项目和部署链接；适合发现候选，教程可能过期，应看上游文档。

  **适用场景**：想按中文介绍寻找 Docker 自部署项目和教程时浏览；适合发现候选，不是全部服务已由清单作者验证的保证。

  **标签**：`Docker` · `教程` · `资源清单`

- **[dockur/windows](https://github.com/dockur/windows)**

  **主要功能**：Docker方式启动Windows虚拟机并提供Web/VNC访问；需虚拟化资源和合法许可证，不是普通容器进程。

  **适用场景**：希望在现有 Docker 管理环境里运行 Windows 虚拟机时参考；不是把完整 Windows 变成普通 Linux 进程，需核对虚拟化与许可要求。

  **标签**：`Docker` · `Windows` · `虚拟化`

- **[dongyubin/DockerHub](https://github.com/dongyubin/DockerHub)**

  **主要功能**：Docker镜像源/加速资料汇总，用于排查拉取问题；第三方源时效与可信度未逐一验证。

  **适用场景**：Docker 镜像拉取不顺畅时，用它寻找镜像源和加速资料；第三方源的可信度、时效与实际连通性需单独核对。

  **标签**：`Docker` · `镜像源`

  <details>
  <summary>备注与使用提醒</summary>

  可用性未逐一实测，说明中的日期不代表验证日期。

  </details>

- **[eysp/portainer-ce](https://github.com/eysp/portainer-ce)**

  **主要功能**：第三方Portainer CE中文化容器镜像/部署，用图形界面管理容器；功能边界应对照官方矩阵，镜像来源和README版本信息需核实。

  **适用场景**：需要评估 Portainer CE 中文汉化容器镜像时参考；与上游官方镜像分别核对版本、来源和镜像可信度。

  **标签**：`Docker` · `Portainer` · `汉化`

  <details>
  <summary>备注与使用提醒</summary>

  第三方镜像，需核对来源与版本。

  </details>

- **[hotheadhacker/awesome-selfhost-docker](https://github.com/hotheadhacker/awesome-selfhost-docker)**

  **主要功能**：按类别整理Docker/Compose自托管项目，供NAS/服务器选型；是资源目录，部署细节查看上游。

  **适用场景**：想找能自己部署的服务、比较 Docker 项目候选时浏览；它是项目目录，不是统一安装或运维面板。

  **标签**：`Docker` · `资源清单`

## 导航与文件服务

- **[codewec/dashlit](https://github.com/codewec/dashlit)**

  **主要功能**：自托管个人/团队仪表盘，可建公开、登录可见或私有看板，以行列/瀑布布局整理链接和服务；支持拖拽、搜索、快捷键、图标主题、用户权限及URL可用性监测。可Docker或Go二进制部署；生产环境应持久化数据并保护密钥。

  **适用场景**：家里或服务器上的服务入口太多时，用统一首页集中放链接、工具入口和状态信息，减少逐个记地址。

  **标签**：`导航` · `自托管`

- **[dr34m-cn/taosync](https://github.com/dr34m-cn/taosync)**

  **主要功能**：OpenList/AList v3+同步任务管理，支持全量/仅新增/移动、过滤、cron/定时、进度和通知；需另部署OpenList，公网需保护。

  **适用场景**：已有 OpenList 或 AList，需要编排文件同步任务时参考；它是同步配套工具，不替代文件列表服务本体。

  **标签**：`OpenList` · `同步`

- **[FNOSP/fnnas-api](https://github.com/FNOSP/fnnas-api)**

  **主要功能**：Python异步飞牛NAS WebSocket SDK，含登录/token、用户、文件列表/搜索/上传、磁盘/端口接口和重连；错误处理不完善，未实现下载/双向同步。

  **适用场景**：需要研究飞牛 NAS 网页接口或编写与 NAS 交互的小工具时参考；不能仅凭项目名认定所有功能和版本均受支持。

  **标签**：`NAS` · `API`

- **[OpenListTeam/OpenList](https://github.com/OpenListTeam/OpenList)**

  **主要功能**：多存储文件列表服务，把网盘等统一为浏览/分享入口；不是同步工具，驱动和权限需分别配置。

  **适用场景**：需要将不同存储统一为文件浏览入口时参考。它解决文件列表与访问入口问题，跨存储自动同步可另看 TaoSync。

  **标签**：`网盘` · `自托管`

- **[tsxcw/oneNav](https://github.com/tsxcw/oneNav)**

  **主要功能**：oneNav网页导航项目，README说明npm安装、开发及构建流程；具体功能信息有限，按仓库代码核实，不与同名项目混淆。

  **适用场景**：需要一个网页导航项目或想参考其前端打包方式时查看；应按这个作者的代码判断，不能套用其他 oneNav 项目的说明。

  **标签**：`导航` · `网页`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；不要与其他同名导航项目混淆。

  </details>

# 网络与连接

## 动态域名与组网

- **[dwj0-code/n2n-gui-for-windows](https://github.com/dwj0-code/n2n-gui-for-windows)**

  **主要功能**：Windows图形界面管理n2n edge/supernode及路由，可与OpenWrt配合；需运行库及n2n组件，配置文件网络密码未加密。

  **适用场景**：已经使用或准备使用 n2n、希望在 Windows 中用图形界面管理连接时参考；底层组网方案仍是 n2n。

  **标签**：`Windows` · `n2n`

  <details>
  <summary>备注与使用提醒</summary>

  与 n2n 主项目配套。

  </details>

- **[jeessy2/ddns-go](https://github.com/jeessy2/ddns-go)**

  **主要功能**：探测公网IPv4/IPv6并更新DNS服务商记录，提供Web配置、日志、Webhook和TTL；需要DNS API凭据及网络连通，管理页面应保护。

  **适用场景**：家庭宽带或服务器公网 IP 会变、希望域名自动跟随更新时参考；DDNS 更新记录不等于自动解决内网穿透问题。

  **标签**：`DDNS` · `DNS`

- **[ntop/n2n](https://github.com/ntop/n2n)**

  **主要功能**：轻量P2P虚拟网络，edge节点可UDP直连，NAT受限时经supernode中继，也可自建supernode；节点须能访问supernode且配置匹配。

  **适用场景**：需要将分散设备接入点对点虚拟网络时参考；Windows 端图形操作可另看 n2n-gui-for-windows。

  **标签**：`P2P` · `VPN`

## 代理客户端

- **[chen08209/FlClash](https://github.com/chen08209/FlClash)**

  **主要功能**：ClashMeta/mihomo多平台代理客户端，支持配置导入、规则、代理组、延迟测试、系统代理/TUN、DNS日志及备份；需自行提供服务配置，平台条件不同。

  **适用场景**：希望在多个操作系统上使用相近的 ClashMeta 代理客户端体验时参考；仍需配置合法可用的代理服务与规则。

  **标签**：`Clash` · `跨平台`

- **[MetaCubeX/ClashMetaForAndroid](https://github.com/MetaCubeX/ClashMetaForAndroid)**

  **主要功能**：Clash.Meta Android GUI，用于配置和运行代理内核、导入配置文件并通过Intent控制启停。最低Android 5、推荐7+，支持多ABI；内核依赖Clash.Meta，源码构建需Android/Go/CMake工具链。

  **适用场景**：Android 设备需要按规则管理网络代理时参考。客户端与线路配置是两回事，收藏应用不代表已有可用服务。

  **标签**：`Android` · `Clash`

- **[v2rayA/v2rayA](https://github.com/v2rayA/v2rayA)**

  **主要功能**：Web代理管理客户端，可导入节点/订阅、测延迟、设置RoutingA规则分流和透明代理；需配套核心/规则，透明代理可能要求root及防火墙/TUN。

  **适用场景**：希望通过 Web 界面管理 Xray 相关代理配置，或研究透明代理部署时参考；运行条件因平台和权限不同而异。

  **标签**：`Xray` · `代理`

## Hosts 与连通性

- **[GoodCoder666/GoogleTranslate_IPFinder](https://github.com/GoodCoder666/GoogleTranslate_IPFinder)**

  **主要功能**：扫描translate.googleapis.com候选IP并测速排序，可辅助Hosts排障；针对特定Windows环境，写Hosts需提权，结果时效性强。

  **适用场景**：排查谷歌翻译接口连通性、研究 IP 扫描与测速方式时参考；具体 IP 的有效性具有时效性。

  **标签**：`翻译` · `IP` · `Hosts`

  <details>
  <summary>备注与使用提醒</summary>

  IP 和服务是否可用未实测。

  </details>

- **[Licoy/fetch-github-hosts](https://github.com/Licoy/fetch-github-hosts)**

  **主要功能**：GUI/CLI从可配置数据源同步GitHub Hosts到系统，也能提供HTTP文本/JSON服务和定时刷新；写系统文件需提权，映射可能过时。

  **适用场景**：研究通过同步 Hosts 改善 GitHub 域名连通性时参考；它不保证任何网络环境都能访问，也不是代理客户端。

  **标签**：`GitHub` · `Hosts`

- **[Ponderfly/GoogleTranslateIpCheck](https://github.com/Ponderfly/GoogleTranslateIpCheck)**

  **主要功能**：扫描和测速谷歌翻译候选IP，支持IPv4/IPv6、快速扫描及可选写Hosts；提权按OS而异，不能保证翻译服务恢复。

  **适用场景**：寻找谷歌翻译可用 IP 扫描思路时参考，可与 IPFinder 对照；并不意味着已恢复任何客户端的翻译功能。

  **标签**：`翻译` · `IP`

# 设备与系统增强

## 桌面与外设

- **[AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)**

  **主要功能**：Logitech本地配置工具，支持按键/手势、应用配置、指针滚轮灯光和部分摄像头控制；支持有限且开发中，可能需退出其他占用软件。

  **适用场景**：希望调整罗技鼠标按键、DPI、SmartShift 等行为，又希望采用本地优先工具时参考，具体支持型号需核对。

  **标签**：`罗技` · `鼠标` · `本地优先`

- **[TranslucentTB/TranslucentTB](https://github.com/TranslucentTB/TranslucentTB)**

  **主要功能**：Windows 10/11任务栏外观工具，可调透明度、颜色及Normal/Opaque/Clear/Blur/Acrylic状态，并按窗口最大化、开始菜单、搜索和任务视图动态切换。Blur和便携构建有系统版本限制；测试构建可能不稳定。

  **适用场景**：只想调整 Windows 任务栏外观时使用，不需要为了这个目的安装完整桌面主题套件。

  **标签**：`Windows` · `美化`

## Android 与模块

- **[Androidacy/MagiskModuleManager](https://github.com/Androidacy/MagiskModuleManager)**

  **主要功能**：Android Magisk模块发现与管理应用，README建议当前V3并警告旧版/部分渠道过时停更；需兼容Magisk，核对模块来源。

  **适用场景**：已有 Magisk 环境、需要浏览和管理模块时参考；模块管理器不等于模块本身，兼容性与风险仍需逐项核对。

  **标签**：`Android` · `Magisk`

- **[chenzyadb/CuprumTurbo-Scheduler](https://github.com/chenzyadb/CuprumTurbo-Scheduler)**

  **主要功能**：README不可访问；简介仅称Android性能调度工具，具体功能、设备、权限未知，未按名字猜测。

  **适用场景**：研究 Android 性能调度方案或设备优化时参考；实际设备适配和权限要求未验证，不能当作通用提速开关。

  **标签**：`Android` · `性能`

  <details>
  <summary>备注与使用提醒</summary>

  具体设备适配和权限要求未实测。

  </details>

- **[eritpchy/FingerprintPay](https://github.com/eritpchy/FingerprintPay)**

  **主要功能**：为部分支付应用增加指纹确认/自动填密，README称凭据由Android Keystore加密；需要指纹硬件及兼容模块，涉及支付凭据和高权限。

  **适用场景**：希望研究为部分支付应用补充指纹验证的方案时参考；涉及支付与系统模块权限，不应只因方便就忽略安全审查。

  **标签**：`Android` · `指纹` · `支付`

  <details>
  <summary>备注与使用提醒</summary>

  涉及支付安全，使用前需审查来源与权限。

  </details>

- **[Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)**

  **主要功能**：Android屏幕镜像与控制工具，可通过USB或网络在电脑显示、操作并录制手机屏幕；需授权ADB调试并按官方说明安装。

  **适用场景**：想在电脑上查看和操作 Android 手机屏幕、减少电脑与手机之间切换时参考；连接方式与设备授权按官方文档配置。

  **标签**：`Android` · `投屏`

- **[LSPosed/LSPosed](https://github.com/LSPosed/LSPosed)**

  **主要功能**：Android ART/Xposed模块框架，为兼容模块提供Hook运行环境；需root及兼容Magisk/Riru/Zygisk路径，高权限系统修改须核对ROM和模块。

  **适用场景**：需要运行 Android Xposed 生态模块时参考；框架、具体模块和系统版本必须匹配，安装可能涉及较高系统权限。

  **标签**：`Android` · `Xposed`

- **[m9rco/Genymotion_ARM_Translation](https://github.com/m9rco/Genymotion_ARM_Translation)**

  **主要功能**：Genymotion ARM兼容转换包/资料，涉及旧ARMv7和实验性Android 11–14 x86\_64 ARM64；须匹配模拟器版本，部分适配未验证。

  **适用场景**：Genymotion 模拟器需要运行特定 ARM 应用时，查找匹配版本的转换包与校验资料；不同 Android 版本不能任意混用。

  **标签**：`Android` · `模拟器` · `ARM`

- **[MRepoApp/magisk-modules-alt-repo](https://github.com/MRepoApp/magisk-modules-alt-repo)** · **已归档**

  **主要功能**：Magisk替代模块源的镜像/索引，可供兼容管理器添加；本身不是模块，仓库已归档，需逐项核实来源/安全。

  **适用场景**：需要查找 Magisk 模块替代仓库的历史镜像时参考；已归档的模块来源尤其需要核对更新与安全性。

  **标签**：`Magisk` · `模块`

  <details>
  <summary>备注与使用提醒</summary>

  仓库已归档。

  </details>

## 系统授权相关

- **[akhilnathe/winactivate](https://github.com/akhilnathe/winactivate)**

  **主要功能**：README描述Windows HWID/KMS38相关脚本及系统要求；使用前确认合法授权，本目录不提供绕过授权步骤。

  **适用场景**：保留 Windows 激活相关脚本的研究线索；项目历史较旧，许可合规和适配情况需单独核对，本目录不提供激活步骤。

  **标签**：`Windows` · `授权`

  <details>
  <summary>备注与使用提醒</summary>

  需核对合法许可；本目录不提供激活操作。

  </details>

- **[massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts)**

  **主要功能**：Windows/Office授权与故障排查脚本集合；涉及软件许可，须确认合法授权。本目录不提供绕过授权步骤。

  **适用场景**：研究 Windows、Office 授权相关工具和故障排查资料时参考；使用任何激活功能前需确认合法许可，不作为获取授权的替代品。

  **标签**：`Windows` · `Office`

  <details>
  <summary>备注与使用提醒</summary>

  涉及软件授权，需核对合法许可；本目录不提供激活操作。

  </details>

## 智能家居

- **[XiaoMi/ha_xiaomi_home](https://github.com/XiaoMi/ha_xiaomi_home)**

  **主要功能**：Home Assistant小米智能家居集成，将兼容设备接入自动化平台；需HA和账户/地区配置，设备覆盖见文档。

  **适用场景**：已有 Home Assistant、希望接入小米智能设备时参考；支持的设备型号、地区和配置条件需按集成文档核对。

  **标签**：`小米` · `HomeAssistant`

# 开发与技术资源

## 开发工具与组件

- **[dotnetcore/AgileConfig](https://github.com/dotnetcore/AgileConfig)**

  **主要功能**：.NET分布式配置中心，集中管理多应用配置并向客户端推送更改；需部署服务端并集成客户端，存储和依赖依版本设置。

  **适用场景**：多个应用需要集中管理配置、减少逐台修改配置文件时参考，尤其适合进一步评估 .NET 技术栈的配置中心方案。

  **标签**：`.NET` · `配置管理`

- **[hlmd/Postman-cn](https://github.com/hlmd/Postman-cn)** · **已归档**

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

## 学习资料

- **[caoaolong/coding-soul-docs](https://github.com/caoaolong/coding-soul-docs)**

  **主要功能**：编程课程文档，含手写操作系统、编译器/语言实现及Godot示例，主要供阅读学习，不是软件应用。

  **适用场景**：学习 CodingSoul 系列课程、查找对应技术说明时参考；它属于学习资料，不是可直接使用的软件应用。

  **标签**：`编程` · `教程`

- **[EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books)**

  **主要功能**：按语言/主题整理免费编程书籍和课程链接，可浏览搜索；它是资源索引不是完整课程，链接、授权和质量需分别核对。

  **适用场景**：学习某种语言或技术、需要寻找免费书籍和课程资源时使用；它是资料索引，不是一套按顺序编排的统一课程。

  **标签**：`编程` · `书籍` · `资源清单`

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

# 签到与平台自动化

## 话费与用量监控

- **[Cp0204/ChinaTelecomMonitor](https://github.com/Cp0204/ChinaTelecomMonitor)**

  **主要功能**：监控电信话费、通话和流量套餐，可青龙定时或Docker/API运行；需账号配置，接口变化可能失效。

  **适用场景**：想统一查看电信套餐余量、话费、流量和通话用量时参考，可进一步评估青龙任务或 Docker API 部署方式。

  **标签**：`电信` · `青龙` · `Docker`

- **[DreamLay/MyPhoneBill](https://github.com/DreamLay/MyPhoneBill)**

  **主要功能**：移动/联通话费查询工具，通过登录获取账单或套餐数据；代码较旧，接口和登录流程未验证，需保护凭据。

  **适用场景**：希望把移动、联通话费查询纳入自己的信息面板或脚本时参考；代码历史较久，先验证登录和接口是否仍可用。

  **标签**：`移动` · `联通` · `话费`

  <details>
  <summary>备注与使用提醒</summary>

  代码较旧，接口可用性未验证。

  </details>

## 签到与日常任务

- **[Aijiaobin/Cloud189Checkin](https://github.com/Aijiaobin/Cloud189Checkin)**

  **主要功能**：天翼云盘个人/家庭空间签到，支持多账号、Actions/青龙和推送；账号凭据需用secrets妥善保管，并与同名项目按作者区分。

  **适用场景**：已有青龙环境、需要天翼网盘签到脚本时参考；与另一同名项目比较部署方式和当前维护状态后再选。

  **标签**：`天翼网盘` · `青龙`

  <details>
  <summary>备注与使用提醒</summary>

  与 wes-lin 同名项目区分作者保留。

  </details>

- **[BNDou/Auto_Check_In](https://github.com/BNDou/Auto_Check_In)**

  **主要功能**：多App/网站每日签到脚本合集，可集中运行重复任务；平台支持依脚本版本，需配置账号并遵守站点规则。

  **适用场景**：想为若干网站或 App 的重复签到任务寻找现成脚本参考时浏览；具体支持的平台以当前仓库内容为准。

  **标签**：`签到` · `脚本`

- **[fengwenhua/hifini_sign_in](https://github.com/fengwenhua/hifini_sign_in)**

  **主要功能**：HiFiNi音乐磁场签到脚本，可按README在青龙定时运行；需站点登录，接口变化可能失效。

  **适用场景**：已有青龙环境、希望研究音乐磁场 HiFiNi 签到任务时参考；网站规则与登录态变化可能影响脚本。

  **标签**：`青龙` · `签到`

- **[Ren-Boo/QiDianDuShu](https://github.com/Ren-Boo/QiDianDuShu)**

  **主要功能**：起点读书Android界面自动化脚本，处理福利/视频/听书任务；不是阅读器或下载器，界面变化可能失效。

  **适用场景**：研究起点读书福利、听书和日常任务的界面自动化时参考；不是阅读内容下载器，也不是新的阅读客户端。

  **标签**：`起点读书` · `Android`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；不是小说阅读客户端。自动化存在平台限制与账号风险。

  </details>

- **[shufflewzc/faker2](https://github.com/shufflewzc/faker2)**

  **主要功能**：青龙面板生态京东自动化脚本集合，含签到、农场/种豆、抽奖、活动及Cookie辅助脚本；需按青龙任务配置并提供账号Cookie。接口或活动时效会影响运行，须审阅脚本和授权风险。

  **适用场景**：已有青龙环境、想研究日常任务脚本如何编排时参考。不要将仓库宣传中的账户安全表述当作经过验证的保证。

  **标签**：`青龙` · `签到`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；未运行脚本，不保证平台兼容或账号安全。

  </details>

- **[Sitoi/dailycheckin](https://github.com/Sitoi/dailycheckin)**

  **主要功能**：多网站、多账号签到脚本，README列出Python/PyPI、Docker、青龙、群晖和本地方式，以及通知/定时/更新能力；需核对各平台脚本当前状态。

  **适用场景**：想统一运行多个平台、多账号签到任务时参考；可以对照收藏中的其他签到集合选择，不必把功能相近的仓库全装一遍。

  **标签**：`青龙` · `Docker` · `签到`

- **[wes-lin/Cloud189Checkin](https://github.com/wes-lin/Cloud189Checkin)**

  **主要功能**：天翼云盘签到/奖励获取，支持Actions、Node.js、青龙、多账号与推送；需配置secrets，设备锁/MFA可阻断，凭据勿公开。

  **适用场景**：需要研究天翼网盘日常签到自动化时参考；与 Aijiaobin 的同名项目按作者区分，不假设二者始终等价。

  **标签**：`天翼网盘` · `签到`

  <details>
  <summary>备注与使用提醒</summary>

  与另一同名仓库分别保留，不推断二者替代关系。

  </details>

## Cookie 与模板

- **[qd-today/get-cookies](https://github.com/qd-today/get-cookies)**

  **主要功能**：Chrome/Firefox扩展，提取浏览器Cookie供QD签到框架使用；Cookie等同登录凭据，只应在可信环境使用且不可公开提交。

  **适用场景**：使用 QD 签到框架、需要从浏览器取得站点登录态时参考；扩展取得的 Cookie 应视同账号凭据。

  **标签**：`Cookie` · `浏览器扩展`

  <details>
  <summary>备注与使用提醒</summary>

  Cookie 等同账户敏感凭据，不要上传。

  </details>

- **[wjf0214/qd-templates](https://github.com/wjf0214/qd-templates)**

  **主要功能**：qiandao/QD框架公共HAR模板示例；框架版本不匹配可能失效，HAR可能包含Cookie，个人抓包不能公开提交。

  **适用场景**：使用 QD 框架、想参考不同站点签到请求模板时查看；公共模板和自己抓取的含凭据 HAR 文件应严格区分。

  **标签**：`QD` · `HAR` · `模板`

  <details>
  <summary>备注与使用提醒</summary>

  实际 HAR 可能包含凭据，不应直接提交个人抓包。

  </details>

- **[yclown/ql_jd_cookie](https://github.com/yclown/ql_jd_cookie)**

  **主要功能**：Windows桌面京东Cookie工具，获取后可发送至青龙并管理多账号；需青龙API授权，凭据必须保密。

  **适用场景**：偏好桌面操作、需要把京东登录态交给青龙任务时参考；与自动登录更新工具分开比较交互和权限要求。

  **标签**：`京东` · `Cookie` · `青龙`

  <details>
  <summary>备注与使用提醒</summary>

  涉及账户凭据，使用前需自行审查。

  </details>

- **[zhuoyanzhe/AutoUpdateJdCookie](https://github.com/zhuoyanzhe/AutoUpdateJdCookie)**

  **主要功能**：检测京东Cookie失效并登录获取新凭据、更新青龙变量；需Python/Playwright，新设备验证可能需人工。

  **适用场景**：已有京东相关青龙任务、需要研究登录态更新流程时参考；Cookie 是敏感账户数据，不能放进公开仓库。

  **标签**：`京东` · `Cookie` · `青龙`

  <details>
  <summary>备注与使用提醒</summary>

  涉及账户凭据，使用前需自行审查。

  </details>

# 通讯与机器人

## QQ 接入与增强

- **[iii80/NtrQQ](https://github.com/iii80/NtrQQ)**

  **主要功能**：传统PC QQ/TIM插件，README列显IP、去广告和功能增强；需匹配客户端，作者提示封号风险且限学习交流、非商业。

  **适用场景**：研究传统 QQ/TIM PC 客户端去广告和增强功能时参考；不能与当前 NTQQ 协议接入框架 NapCat 混为一谈。

  **标签**：`QQ` · `TIM` · `Windows`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；不是 Android 应用。旧客户端兼容性及账号风险需核对。

  </details>

- **[NapNeko/NapCat-Docker](https://github.com/NapNeko/NapCat-Docker)**

  **主要功能**：NapCatQQ的Docker部署包装，简化容器启动与配置；只负责部署，不是独立AI机器人。

  **适用场景**：已经决定使用 NapCat，想通过容器部署时查看；实际 QQ 协议能力来自 NapCatQQ，两个收藏分别对应部署层和功能层。

  **标签**：`QQ` · `OneBot` · `Docker`

  <details>
  <summary>备注与使用提醒</summary>

  与 NapCatQQ 配套，不是独立 AI 助手。

  </details>

- **[NapNeko/NapCatQQ](https://github.com/NapNeko/NapCatQQ)**

  **主要功能**：基于NTQQ的QQ协议端框架，提供OneBot接口供机器人接入；需兼容客户端，留意账号和平台风险。

  **适用场景**：需要给机器人框架提供 QQ 的 OneBot 接口时参考；若目标是 AI 对话，还需要另接 AstrBot 等上层助手。

  **标签**：`QQ` · `OneBot`

  <details>
  <summary>备注与使用提醒</summary>

  第三方协议接入需注意账号与平台限制。

  </details>

# 游戏与生活参考

## 游戏工具

- **[Aliothmoon/MAA-Meow](https://github.com/Aliothmoon/MAA-Meow)**

  **主要功能**：在Android原生运行MAA Core的明日方舟自动化工具，可执行理智作战、公招、基建、抄作业、肉鸽及定时任务，并提供前台控制/后台虚拟显示和Intent集成。需Android 9+、arm64或x86\_64及Shizuku授权或Root；README注明开发中、功能不稳定。

  **适用场景**：希望在 Android 设备上处理明日方舟日常任务时参考；与桌面 MAA 分开保留，按实际设备选择。

  **标签**：`Android` · `明日方舟`

- **[dyc3/steamguard-cli](https://github.com/dyc3/steamguard-cli)**

  **主要功能**：Linux命令行Steam Guard工具，可生成验证码并处理交易确认；需导入认证数据，身份文件应安全保管且不可提交。

  **适用场景**：需要在 Linux 或命令行环境处理 Steam 验证码和交易确认时参考；身份文件和认证数据必须单独保护。

  **标签**：`Steam` · `2FA` · `Linux`

  <details>
  <summary>备注与使用提醒</summary>

  涉及认证数据，应妥善保存且不入库。

  </details>

- **[igromanru/Helldivers-2-Highlight-Samples](https://github.com/igromanru/Helldivers-2-Highlight-Samples)** · **已归档**

  **主要功能**：绝地潜兵2样本高亮Mod资料；仓库已归档，当前版本和反作弊兼容性不保证。

  **适用场景**：查找绝地潜兵 2 样本高亮相关 Mod 的历史资料时参考；已归档不代表兼容当前游戏版本。

  **标签**：`游戏` · `Mod`

  <details>
  <summary>备注与使用提醒</summary>

  仓库已归档；使用前核对游戏规则和兼容性。

  </details>

- **[MaaAssistantArknights/MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)**

  **主要功能**：明日方舟图像识别自动化，README列自动作战、基建、公招、日常、肉鸽及作业导入分享；需支持的游戏和运行环境，UI变化会影响识别。

  **适用场景**：想自动处理明日方舟重复日常操作时参考；Android 使用场景可同时比较 MAA-Meow，具体连接方式按项目文档选择。

  **标签**：`明日方舟` · `MAA`

## 生活与社会资料

- **[Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook)**

  **主要功能**：结构化菜谱及烹饪基础资料，包含食材、步骤和准备指南，可在线浏览或用Docker Viewer；README提供演示默认口令，部署需改密并限制访问。

  **适用场景**：需要按步骤查食谱、比较食材和做法时使用；适合日常做菜参考，不是营养治疗或个体膳食处方。

  **标签**：`食谱` · `烹饪`

- **[geekan/HowToLiveLonger](https://github.com/geekan/HowToLiveLonger)**

  **主要功能**：健康与长寿研究摘要、主题资料和原始论文链接，支持在线/离线阅读；摘要不是个体医疗建议，重要结论需看原文。

  **适用场景**：想从程序员视角了解健康与长寿相关资料时参考；内容仅作线索，不能替代循证核查和个人医疗建议。

  **标签**：`健康` · `资料`

  <details>
  <summary>备注与使用提醒</summary>

  非个体医疗建议，不代表内容均经医学审核。

  </details>

- **[WeNeedHome/SummaryOfLoanSuspension](https://github.com/WeNeedHome/SummaryOfLoanSuspension)**

  **主要功能**：省市停贷通知与楼盘历史资料汇总，含结构化、统计/地图查看；README声明可能不准确，不代表实时进展或法律/金融意见。

  **适用场景**：需要回看各地停贷通知相关汇总时查阅；它是历史社会资料，不代表当前进展、法律意见或贷款建议。

  **标签**：`社会资料` · `历史参考`

  <details>
  <summary>备注与使用提醒</summary>

  资料可能陈旧，不作为当前法律或金融建议。

  </details>

# 待分类

## 待复核

- **[for-the-zero/Free-LLM-Collection](https://github.com/for-the-zero/Free-LLM-Collection)**

  **主要功能**：免费大模型API合集 / Free LLM api Collection

  <details>
  <summary>备注与使用提醒</summary>

  新项目尚未进行中文用途审核。

  </details>

# 待分类

以下项目已收藏，但尚未完成用途核对与正式分类。

- **[for-the-zero/Free-LLM-Collection](https://github.com/for-the-zero/Free-LLM-Collection)**

  **主要功能**：免费大模型API合集 / Free LLM api Collection

  <details>
  <summary>备注与使用提醒</summary>

  新项目尚未进行中文用途审核。

  </details>

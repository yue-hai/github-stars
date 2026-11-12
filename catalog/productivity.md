# 日常应用与效率

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 9 项 · 快照 2026-11-12（UTC）。按用途分组；平台和技术见标签。

收录日常直接使用的应用与插件。跨设备复制和剪贴板历史放一起比较；输入法方案、输入法应用和 Obsidian 插件分别说明；社区客户端按实际平台选择。

- [剪贴板与跨设备](#section-1)
- [输入法与笔记](#section-2)
- [社区客户端](#section-3)

<a id="section-1"></a>
## 剪贴板与跨设备

- **[CrossPaste/crosspaste-desktop](https://github.com/CrossPaste/crosspaste-desktop)**

  **主要功能**：跨平台局域网剪贴板同步，README列端到端加密、OCR、CLI和MCP；参与设备需安装且网络可达。

  **适用场景**：经常在多台电脑之间复制文字或文件内容时参考，重点是跨设备剪贴板流转；区别于主要管理单机剪贴板历史的 CopyQ。

  **标签**：`剪贴板` · `跨设备`

- **[hluk/CopyQ](https://github.com/hluk/CopyQ)**

  **主要功能**：跨平台剪贴板管理器，可记录多种格式、搜索筛选、编辑、标签、快捷键、命令和脚本，适合本机历史管理；不等同跨设备同步。

  **适用场景**：经常重复复制粘贴、需要找回剪贴板历史或编写剪贴板处理脚本时参考；跨电脑同步可另看 CrossPaste。

  **标签**：`剪贴板` · `跨平台`

<a id="section-2"></a>
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

<a id="section-3"></a>
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

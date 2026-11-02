# 媒体与内容处理

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 10 项 · 快照 2026-11-02（UTC）。按用途分组；平台和技术见标签。

按处理流程选择：播放器、转码、录屏与字幕工具在音视频分区；下载与投稿工具在下载与发布分区。上传、下载、字幕识别和字幕编辑不是同一种能力。

- [音视频与字幕](#section-1)
- [下载与发布](#section-2)

<a id="section-1"></a>
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

<a id="section-2"></a>
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

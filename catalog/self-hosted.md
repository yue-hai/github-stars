# 服务器与自托管

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 14 项 · 快照 2026-10-31（UTC）。按用途分组；平台和技术见标签。

既有可部署服务，也有项目清单和运维客户端。找软件先看部署资源；管理主机看远程与监控；统一文件入口和同步看导航与文件服务。

- [远程管理与监控](#section-1)
- [部署资源与容器](#section-2)
- [导航与文件服务](#section-3)

<a id="section-1"></a>
## 远程管理与监控

- **[gnmyt/Nexterm](https://github.com/gnmyt/Nexterm)**

  **功能**：支持 SSH、VNC 和 RDP 的服务器管理软件

  **适用场景**：需要集中访问多台机器的 SSH、VNC、RDP 连接时参考；重点是远程会话管理，与只看服务器指标的监控组件不同。

  **标签**：`SSH` · `VNC` · `RDP`

- **[kingToolbox/WindTerm](https://github.com/kingToolbox/WindTerm)**

  **功能**：跨平台 SSH、SFTP、Telnet 与串口终端

  **适用场景**：经常通过 SSH、SFTP、串口等方式维护设备或服务器时参考，重点是跨平台终端与远程操作。

  **标签**：`SSH` · `终端` · `SFTP`

- **[lollipopkit/flutter_server_box](https://github.com/lollipopkit/flutter_server_box)**

  **功能**：ServerBox 服务器状态查看与管理工具箱

  **适用场景**：需要在移动端查看服务器状态、使用服务器管理工具箱时参考；与 server\_box\_monitor 配套关系需按具体功能核对。

  **标签**：`SSH` · `监控` · `移动端`

- **[lollipopkit/server_box_monitor](https://github.com/lollipopkit/server_box_monitor)**

  **功能**：ServerBox 配套服务端监控组件

  **适用场景**：使用 ServerBox 生态、需要在被监控服务器上放置配套监控端时参考；它不是用户日常操作的完整客户端。

  **标签**：`监控` · `服务器`

<a id="section-2"></a>
## 部署资源与容器

- **[coracoo/awesome_docker_cn](https://github.com/coracoo/awesome_docker_cn)**

  **功能**：Docker 自部署项目和中文部署教程清单

  **适用场景**：想按中文介绍寻找 Docker 自部署项目和教程时浏览；适合发现候选，不是全部服务已由清单作者验证的保证。

  **标签**：`Docker` · `教程` · `资源清单`

- **[dockur/windows](https://github.com/dockur/windows)**

  **功能**：通过 Docker 环境运行 Windows 虚拟机

  **适用场景**：希望在现有 Docker 管理环境里运行 Windows 虚拟机时参考；不是把完整 Windows 变成普通 Linux 进程，需核对虚拟化与许可要求。

  **标签**：`Docker` · `Windows` · `虚拟化`

- **[dongyubin/DockerHub](https://github.com/dongyubin/DockerHub)**

  **功能**：Docker Hub 镜像源和加速服务资料汇总

  **适用场景**：Docker 镜像拉取不顺畅时，用它寻找镜像源和加速资料；第三方源的可信度、时效与实际连通性需单独核对。

  **标签**：`Docker` · `镜像源`

  <details>
  <summary>备注与使用提醒</summary>

  可用性未逐一实测，说明中的日期不代表验证日期。

  </details>

- **[eysp/portainer-ce](https://github.com/eysp/portainer-ce)**

  **功能**：Portainer CE 中文汉化 Docker 镜像

  **适用场景**：需要评估 Portainer CE 中文汉化容器镜像时参考；与上游官方镜像分别核对版本、来源和镜像可信度。

  **标签**：`Docker` · `Portainer` · `汉化`

  <details>
  <summary>备注与使用提醒</summary>

  第三方镜像，需核对来源与版本。

  </details>

- **[hotheadhacker/awesome-selfhost-docker](https://github.com/hotheadhacker/awesome-selfhost-docker)**

  **功能**：可通过 Docker 部署的自托管项目清单

  **适用场景**：想找能自己部署的服务、比较 Docker 项目候选时浏览；它是项目目录，不是统一安装或运维面板。

  **标签**：`Docker` · `资源清单`

<a id="section-3"></a>
## 导航与文件服务

- **[codewec/dashlit](https://github.com/codewec/dashlit)**

  **功能**：自托管链接导航、工具入口与服务状态首页

  **适用场景**：家里或服务器上的服务入口太多时，用统一首页集中放链接、工具入口和状态信息，减少逐个记地址。

  **标签**：`导航` · `自托管`

- **[dr34m-cn/taosync](https://github.com/dr34m-cn/taosync)**

  **功能**：OpenList 与 AList 文件自动同步工具

  **适用场景**：已有 OpenList 或 AList，需要编排文件同步任务时参考；它是同步配套工具，不替代文件列表服务本体。

  **标签**：`OpenList` · `同步`

- **[FNOSP/fnnas-api](https://github.com/FNOSP/fnnas-api)**

  **功能**：飞牛 NAS 网页接口相关项目

  **适用场景**：需要研究飞牛 NAS 网页接口或编写与 NAS 交互的小工具时参考；不能仅凭项目名认定所有功能和版本均受支持。

  **标签**：`NAS` · `API`

- **[OpenListTeam/OpenList](https://github.com/OpenListTeam/OpenList)**

  **功能**：多存储文件列表服务，AList 分支项目

  **适用场景**：需要将不同存储统一为文件浏览入口时参考。它解决文件列表与访问入口问题，跨存储自动同步可另看 TaoSync。

  **标签**：`网盘` · `自托管`

- **[tsxcw/oneNav](https://github.com/tsxcw/oneNav)**

  **功能**：oneNav 导航页面项目

  **适用场景**：需要一个网页导航项目或想参考其前端打包方式时查看；应按这个作者的代码判断，不能套用其他 oneNav 项目的说明。

  **标签**：`导航` · `网页`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；不要与其他同名导航项目混淆。

  </details>

# 网络与连接

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 9 项 · 快照 2026-10-31（UTC）。按用途分组；平台和技术见标签。

代理客户端、DDNS、虚拟组网和 Hosts 工具解决不同连接问题。先明确是代理配置、动态域名更新还是设备互联，不要仅因都涉及网络就互相替代。

- [动态域名与组网](#section-1)
- [代理客户端](#section-2)
- [Hosts 与连通性](#section-3)

<a id="section-1"></a>
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

<a id="section-2"></a>
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

<a id="section-3"></a>
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

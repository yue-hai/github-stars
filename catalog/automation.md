# 签到与平台自动化

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 13 项 · 快照 2026-10-31（UTC）。按用途分组；平台和技术见标签。

区分执行签到的脚本、取得登录态的工具、请求模板以及话费监控。通常需要已有框架和账户配置，不应把 Cookie、HAR 或账号数据上传到本公开目录。

- [话费与用量监控](#section-1)
- [签到与日常任务](#section-2)
- [Cookie 与模板](#section-3)

<a id="section-1"></a>
## 话费与用量监控

- **[Cp0204/ChinaTelecomMonitor](https://github.com/Cp0204/ChinaTelecomMonitor)**

  **功能**：电信话费、通话与流量套餐用量监控

  **适用场景**：想统一查看电信套餐余量、话费、流量和通话用量时参考，可进一步评估青龙任务或 Docker API 部署方式。

  **标签**：`电信` · `青龙` · `Docker`

- **[DreamLay/MyPhoneBill](https://github.com/DreamLay/MyPhoneBill)**

  **功能**：登录并获取移动、联通话费数据

  **适用场景**：希望把移动、联通话费查询纳入自己的信息面板或脚本时参考；代码历史较久，先验证登录和接口是否仍可用。

  **标签**：`移动` · `联通` · `话费`

  <details>
  <summary>备注与使用提醒</summary>

  代码较旧，接口可用性未验证。

  </details>

<a id="section-2"></a>
## 签到与日常任务

- **[Aijiaobin/Cloud189Checkin](https://github.com/Aijiaobin/Cloud189Checkin)**

  **功能**：面向青龙使用的天翼网盘签到项目

  **适用场景**：已有青龙环境、需要天翼网盘签到脚本时参考；与另一同名项目比较部署方式和当前维护状态后再选。

  **标签**：`天翼网盘` · `青龙`

  <details>
  <summary>备注与使用提醒</summary>

  与 wes-lin 同名项目区分作者保留。

  </details>

- **[BNDou/Auto_Check_In](https://github.com/BNDou/Auto_Check_In)**

  **功能**：多个 App 和网站的每日签到脚本集合

  **适用场景**：想为若干网站或 App 的重复签到任务寻找现成脚本参考时浏览；具体支持的平台以当前仓库内容为准。

  **标签**：`签到` · `脚本`

- **[fengwenhua/hifini_sign_in](https://github.com/fengwenhua/hifini_sign_in)**

  **功能**：音乐磁场 HiFiNi 的青龙签到脚本

  **适用场景**：已有青龙环境、希望研究音乐磁场 HiFiNi 签到任务时参考；网站规则与登录态变化可能影响脚本。

  **标签**：`青龙` · `签到`

- **[Ren-Boo/QiDianDuShu](https://github.com/Ren-Boo/QiDianDuShu)**

  **功能**：起点读书福利与日常操作自动化脚本

  **适用场景**：研究起点读书福利、听书和日常任务的界面自动化时参考；不是阅读内容下载器，也不是新的阅读客户端。

  **标签**：`起点读书` · `Android`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；不是小说阅读客户端。自动化存在平台限制与账号风险。

  </details>

- **[shufflewzc/faker2](https://github.com/shufflewzc/faker2)**

  **功能**：配合青龙使用的日常任务和签到脚本集合

  **适用场景**：已有青龙环境、想研究日常任务脚本如何编排时参考。不要将仓库宣传中的账户安全表述当作经过验证的保证。

  **标签**：`青龙` · `签到`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；未运行脚本，不保证平台兼容或账号安全。

  </details>

- **[Sitoi/dailycheckin](https://github.com/Sitoi/dailycheckin)**

  **功能**：支持多网站、多账号的每日签到项目

  **适用场景**：想统一运行多个平台、多账号签到任务时参考；可以对照收藏中的其他签到集合选择，不必把功能相近的仓库全装一遍。

  **标签**：`青龙` · `Docker` · `签到`

- **[wes-lin/Cloud189Checkin](https://github.com/wes-lin/Cloud189Checkin)**

  **功能**：天翼网盘自动签到项目

  **适用场景**：需要研究天翼网盘日常签到自动化时参考；与 Aijiaobin 的同名项目按作者区分，不假设二者始终等价。

  **标签**：`天翼网盘` · `签到`

  <details>
  <summary>备注与使用提醒</summary>

  与另一同名仓库分别保留，不推断二者替代关系。

  </details>

<a id="section-3"></a>
## Cookie 与模板

- **[qd-today/get-cookies](https://github.com/qd-today/get-cookies)**

  **功能**：配合 QD 签到框架使用的浏览器 Cookie 获取扩展

  **适用场景**：使用 QD 签到框架、需要从浏览器取得站点登录态时参考；扩展取得的 Cookie 应视同账号凭据。

  **标签**：`Cookie` · `浏览器扩展`

  <details>
  <summary>备注与使用提醒</summary>

  Cookie 等同账户敏感凭据，不要上传。

  </details>

- **[wjf0214/qd-templates](https://github.com/wjf0214/qd-templates)**

  **功能**：QD 签到框架的公共 HAR 模板集合

  **适用场景**：使用 QD 框架、想参考不同站点签到请求模板时查看；公共模板和自己抓取的含凭据 HAR 文件应严格区分。

  **标签**：`QD` · `HAR` · `模板`

  <details>
  <summary>备注与使用提醒</summary>

  实际 HAR 可能包含凭据，不应直接提交个人抓包。

  </details>

- **[yclown/ql_jd_cookie](https://github.com/yclown/ql_jd_cookie)**

  **功能**：获取京东 Cookie 并发送到青龙的桌面工具

  **适用场景**：偏好桌面操作、需要把京东登录态交给青龙任务时参考；与自动登录更新工具分开比较交互和权限要求。

  **标签**：`京东` · `Cookie` · `青龙`

  <details>
  <summary>备注与使用提醒</summary>

  涉及账户凭据，使用前需自行审查。

  </details>

- **[zhuoyanzhe/AutoUpdateJdCookie](https://github.com/zhuoyanzhe/AutoUpdateJdCookie)**

  **功能**：自动登录京东并更新青龙面板 Cookie 的辅助工具

  **适用场景**：已有京东相关青龙任务、需要研究登录态更新流程时参考；Cookie 是敏感账户数据，不能放进公开仓库。

  **标签**：`京东` · `Cookie` · `青龙`

  <details>
  <summary>备注与使用提醒</summary>

  涉及账户凭据，使用前需自行审查。

  </details>

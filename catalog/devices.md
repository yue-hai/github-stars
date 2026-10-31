# 设备与系统增强

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 12 项 · 快照 2026-10-31（UTC）。按用途分组；平台和技术见标签。

按桌面外设、Android 模块、系统授权及智能家居区分。系统模块和支付相关工具权限较高；功能说明不表示设备兼容或安全性已验证。

- [桌面与外设](#section-1)
- [Android 与模块](#section-2)
- [系统授权相关](#section-3)
- [智能家居](#section-4)

<a id="section-1"></a>
## 桌面与外设

- **[AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)**

  **功能**：罗技鼠标按键、DPI 和滚轮行为配置工具

  **适用场景**：希望调整罗技鼠标按键、DPI、SmartShift 等行为，又希望采用本地优先工具时参考，具体支持型号需核对。

  **标签**：`罗技` · `鼠标` · `本地优先`

- **[TranslucentTB/TranslucentTB](https://github.com/TranslucentTB/TranslucentTB)**

  **功能**：Windows 任务栏透明与模糊效果工具

  **适用场景**：只想调整 Windows 任务栏外观时使用，不需要为了这个目的安装完整桌面主题套件。

  **标签**：`Windows` · `美化`

<a id="section-2"></a>
## Android 与模块

- **[Androidacy/MagiskModuleManager](https://github.com/Androidacy/MagiskModuleManager)**

  **功能**：查找和管理 Magisk 模块的 Android 应用

  **适用场景**：已有 Magisk 环境、需要浏览和管理模块时参考；模块管理器不等于模块本身，兼容性与风险仍需逐项核对。

  **标签**：`Android` · `Magisk`

- **[chenzyadb/CuprumTurbo-Scheduler](https://github.com/chenzyadb/CuprumTurbo-Scheduler)**

  **功能**：Android 性能调度相关工具

  **适用场景**：研究 Android 性能调度方案或设备优化时参考；实际设备适配和权限要求未验证，不能当作通用提速开关。

  **标签**：`Android` · `性能`

  <details>
  <summary>备注与使用提醒</summary>

  具体设备适配和权限要求未实测。

  </details>

- **[eritpchy/FingerprintPay](https://github.com/eritpchy/FingerprintPay)**

  **功能**：为部分支付 App 增加指纹支付支持的模块

  **适用场景**：希望研究为部分支付应用补充指纹验证的方案时参考；涉及支付与系统模块权限，不应只因方便就忽略安全审查。

  **标签**：`Android` · `指纹` · `支付`

  <details>
  <summary>备注与使用提醒</summary>

  涉及支付安全，使用前需审查来源与权限。

  </details>

- **[Genymobile/scrcpy](https://github.com/Genymobile/scrcpy)**

  **功能**：显示和控制 Android 设备屏幕

  **适用场景**：想在电脑上查看和操作 Android 手机屏幕、减少电脑与手机之间切换时参考；连接方式与设备授权按官方文档配置。

  **标签**：`Android` · `投屏`

- **[LSPosed/LSPosed](https://github.com/LSPosed/LSPosed)**

  **功能**：Android 上的 Xposed 模块运行框架

  **适用场景**：需要运行 Android Xposed 生态模块时参考；框架、具体模块和系统版本必须匹配，安装可能涉及较高系统权限。

  **标签**：`Android` · `Xposed`

- **[m9rco/Genymotion_ARM_Translation](https://github.com/m9rco/Genymotion_ARM_Translation)**

  **功能**：Genymotion 的 ARM 兼容转换包与相关校验工具

  **适用场景**：Genymotion 模拟器需要运行特定 ARM 应用时，查找匹配版本的转换包与校验资料；不同 Android 版本不能任意混用。

  **标签**：`Android` · `模拟器` · `ARM`

- **[MRepoApp/magisk-modules-alt-repo](https://github.com/MRepoApp/magisk-modules-alt-repo)** · **已归档**

  **功能**：Magisk 模块替代仓库的镜像

  **适用场景**：需要查找 Magisk 模块替代仓库的历史镜像时参考；已归档的模块来源尤其需要核对更新与安全性。

  **标签**：`Magisk` · `模块`

  <details>
  <summary>备注与使用提醒</summary>

  仓库已归档。

  </details>

<a id="section-3"></a>
## 系统授权相关

- **[akhilnathe/winactivate](https://github.com/akhilnathe/winactivate)**

  **功能**：Windows HWID 与 KMS38 激活相关脚本

  **适用场景**：保留 Windows 激活相关脚本的研究线索；项目历史较旧，许可合规和适配情况需单独核对，本目录不提供激活步骤。

  **标签**：`Windows` · `授权`

  <details>
  <summary>备注与使用提醒</summary>

  需核对合法许可；本目录不提供激活操作。

  </details>

- **[massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts)**

  **功能**：Windows 与 Office 激活及故障排查脚本

  **适用场景**：研究 Windows、Office 授权相关工具和故障排查资料时参考；使用任何激活功能前需确认合法许可，不作为获取授权的替代品。

  **标签**：`Windows` · `Office`

  <details>
  <summary>备注与使用提醒</summary>

  涉及软件授权，需核对合法许可；本目录不提供激活操作。

  </details>

<a id="section-4"></a>
## 智能家居

- **[XiaoMi/ha_xiaomi_home](https://github.com/XiaoMi/ha_xiaomi_home)**

  **功能**：小米设备的 Home Assistant 集成

  **适用场景**：已有 Home Assistant、希望接入小米智能设备时参考；支持的设备型号、地区和配置条件需按集成文档核对。

  **标签**：`小米` · `HomeAssistant`

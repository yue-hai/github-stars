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

  **主要功能**：Logitech本地配置工具，支持按键/手势、应用配置、指针滚轮灯光和部分摄像头控制；支持有限且开发中，可能需退出其他占用软件。

  **适用场景**：希望调整罗技鼠标按键、DPI、SmartShift 等行为，又希望采用本地优先工具时参考，具体支持型号需核对。

  **标签**：`罗技` · `鼠标` · `本地优先`

- **[TranslucentTB/TranslucentTB](https://github.com/TranslucentTB/TranslucentTB)**

  **主要功能**：Windows 10/11任务栏外观工具，可调透明度、颜色及Normal/Opaque/Clear/Blur/Acrylic状态，并按窗口最大化、开始菜单、搜索和任务视图动态切换。Blur和便携构建有系统版本限制；测试构建可能不稳定。

  **适用场景**：只想调整 Windows 任务栏外观时使用，不需要为了这个目的安装完整桌面主题套件。

  **标签**：`Windows` · `美化`

<a id="section-2"></a>
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

<a id="section-3"></a>
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

<a id="section-4"></a>
## 智能家居

- **[XiaoMi/ha_xiaomi_home](https://github.com/XiaoMi/ha_xiaomi_home)**

  **主要功能**：Home Assistant小米智能家居集成，将兼容设备接入自动化平台；需HA和账户/地区配置，设备覆盖见文档。

  **适用场景**：已有 Home Assistant、希望接入小米智能设备时参考；支持的设备型号、地区和配置条件需按集成文档核对。

  **标签**：`小米` · `HomeAssistant`

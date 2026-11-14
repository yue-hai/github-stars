# 通讯与机器人

[← 返回首页](../README.md) · [全部收藏](all.md) · [待分类](pending.md)

共 2 项 · 快照 2026-11-14（UTC）。按用途分组；平台和技术见标签。

这里是 QQ 协议接入、容器部署和 PC 客户端增强。NapCat 为上层机器人提供接口；需要 AI 对话时还应结合 AI 分类中的助手项目。

- [QQ 接入与增强](#section-1)

<a id="section-1"></a>
## QQ 接入与增强

- **[iii80/NtrQQ](https://github.com/iii80/NtrQQ)**

  **主要功能**：传统PC QQ/TIM插件，README列显IP、去广告和功能增强；需匹配客户端，作者提示封号风险且限学习交流、非商业。

  **适用场景**：研究传统 QQ/TIM PC 客户端去广告和增强功能时参考；不能与当前 NTQQ 协议接入框架 NapCat 混为一谈。

  **标签**：`QQ` · `TIM` · `Windows`

  <details>
  <summary>备注与使用提醒</summary>

  README 已核对；不是 Android 应用。旧客户端兼容性及账号风险需核对。

  </details>

- **[NapNeko/NapCatQQ](https://github.com/NapNeko/NapCatQQ)**

  **主要功能**：基于NTQQ的QQ协议端框架，提供OneBot接口供机器人接入；需兼容客户端，留意账号和平台风险。

  **适用场景**：需要给机器人框架提供 QQ 的 OneBot 接口时参考；若目标是 AI 对话，还需要另接 AstrBot 等上层助手。

  **标签**：`QQ` · `OneBot`

  <details>
  <summary>备注与使用提醒</summary>

  第三方协议接入需注意账号与平台限制。

  </details>

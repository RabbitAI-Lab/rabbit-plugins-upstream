---
name: cinema-wxamp-mode-8
description: 影院业务 Skill。通过 Cinema Agent 执行授权采集、H5 回放和绑券能力。
---

这是一个 OpenClaw 入口 Skill。完整的采集、回放、绑券和页面能力由本地 Cinema Agent 插件执行。

支持：

- 检查或创建辰星 H5 本地 Skill
- 通过 调用本地授权
- 查询本地插件安装和授权状态
- 触发已配置订单的回放与绑券

必填身份：

- `yuanxianCode`
- `weixinMpLink`

不要直接调用影院接口；。

---
license: MIT
name: weixin-debounce20s
description: "微信 20s 连发防抖 的『功能装载器』。当用户要求启用/检查/修复微信连发合并（20s 防抖），或刚从全新环境装好 OpenClaw 想获得该能力时，按本技能执行安装与配置，完成后微信连发的多条文字会合并成一轮回复。触发词：启用防抖、防抖没生效、连发合并、多条连发、debounce。"
---

# 微信 20s 连发防抖 —— 功能装载与验证

目标：让当前 OpenClaw 的微信渠道具备 **20s 连发防抖**（首条纯文本启动固定 20 秒窗口，窗口内同一发送者的后续文字合并为一轮；后续文字不刷新截止时间）。
本技能由 agent 代为执行全部安装/配置步骤（幂等：已就绪则仅校验）。

## 执行步骤

1. **判断微信渠道插件状态**
   - 运行 `openclaw plugins inspect openclaw-weixin --json`。
   - 若已存在且 source 含 `clawbot-plugins` 或显示为 ClawBot fork 包：跳第 2 步。
   - 若已装官方版（`@tencent-weixin/openclaw-weixin`，source 非 fork）：先 `openclaw plugins uninstall openclaw-weixin`（配置与登录态保留在 `.openclaw`，不受影响），再继续。
   - 若未安装：`openclaw plugins install clawhub:@yechang1450/openclaw-weixin-clawbot`（内含 20s 防抖 + 引用注入的微信渠道插件；请先征得用户同意再执行安装）。

2. **确保防抖窗口配置 = 20000ms**
   - 编辑 `openclaw.json`：`messages.inbound.debounceMs` 与 `messages.inbound.byChannel["openclaw-weixin"]` 均设为 `20000`；保留文件其余内容。
   - `openclaw config validate` 通过。

3. **重启生效**
   - `openclaw gateway restart`，等待约 20-30 秒使 monitor 恢复（可轮询日志确认 `weixin monitor started`）。

4. **验证（本技能的完成标准）**
   - 日志（`<tmp>/openclaw/openclaw-*.log`）中出现 `debounce: buffered text ... windowMs=20000`；
   - 让用户在微信上从首条开始 20 秒内连发 2 条以上文字，应只收到一轮合并回复，且不会因后续文字把截止时间延后；
   - 若窗口不是 20000：回到第 2 步修正并重启。

## 完成标准
- 微信渠道插件 = ClawBot fork（本机直连 fork 或商店包均可）；
- `messages.inbound` 生效值为 20000ms；
- 微信连发实测合并为一轮。

## 安全
- 所有操作仅限本机 openclaw CLI 与 `openclaw.json`；不读取/外发任何密钥与聊天内容。
- 安装商店插件包前先征得用户同意；用户拒绝则停在说明环节。

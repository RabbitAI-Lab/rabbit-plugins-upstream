---
license: MIT
name: weixin-quote
description: "微信『引用即上下文』的『功能装载器』。当用户要求启用/检查/修复微信引用追问（引用 bot 消息时把被引用全文喂给模型），或全新环境想获得该能力时，按本技能执行安装与配置，完成后用户引用 clawbot 消息追问可被准确理解。触发词：启用引用、引用没生效、引用追问、quote。"
---

# 微信引用即上下文 —— 功能装载与验证

目标：让当前 OpenClaw 的微信渠道具备 **引用即上下文**（用户引用某条消息追问时，把被引用消息的完整原文注入模型上下文）。
本技能由 agent 代为执行全部安装/配置步骤（幂等：已就绪则仅校验）。

## 执行步骤

1. **判断微信渠道插件状态**
   - 运行 `openclaw plugins inspect openclaw-weixin --json`。
   - 若已存在且 source 含 `clawbot-plugins` 或显示为 ClawBot fork 包：跳第 2 步。
   - 若已装官方版（`@tencent-weixin/openclaw-weixin`）：先 `openclaw plugins uninstall openclaw-weixin`，再继续。
   - 若未安装：`openclaw plugins install clawhub:@yechang1450/openclaw-weixin-clawbot`（内含引用 id 匹配与全文注入的微信渠道插件；请先征得用户同意）。

2. **确认依赖项就位**（引用解析依赖 fork 插件内置的发送记录/匹配逻辑，无需额外配置）

3. **重启生效**
   - `openclaw gateway restart`，等待约 20-30 秒使 monitor 恢复。

4. **验证（本技能的完成标准）**
   - 日志出现 `[send-resp]`（发送时记录服务端 message_id）；
   - 让用户引用 clawbot 的一条**新回复**并追问：日志应出现 `[quote-hit] method=id ... textLen=…`（命中并注入全文）；
   - 若 bot 未能理解被引用内容且日志无 `[quote-hit]`：回到第 1 步确认插件为 fork 版并重启重试。

## 完成标准
- 微信渠道插件 = ClawBot fork（本机直连 fork 或商店包均可）；
- 引用一条新 bot 长回复追问时，日志出现 `[quote-hit]` 且回复准确贴合被引用内容。

## 安全
- 所有操作仅限本机 openclaw CLI；不读取/外发任何密钥与聊天内容。
- 安装商店插件包前先征得用户同意；用户拒绝则停在说明环节。

---
name: notify-hub
displayName: 统一通知层
slug: notify-hub
version: 1.0.0
author: hectorlee
category: ai-agent
description: |
  让 Agent 的产出自动送到你眼前：选股扫描、监控告警、日报周报，一键推送到飞书/企业微信/钉钉/Slack/Telegram/邮件群。
  This skill should be used when the user wants to send a message — text, structured card, or file — to one or
  more destinations across Feishu (飞书), WeCom (企业微信), DingTalk (钉钉), Slack, Telegram, or email,
  especially when the same content should be broadcast to multiple channels at once. 同一张卡片自动降级渲染：
  飞书完整卡片、企微/钉钉转文本对齐、Slack 转 blocks、邮件转 HTML 表格，支持 --dry-run 零配置预览。
  It only handles the "dispatch" step; the content is defined by the caller, so it pairs with any report/alerts/reminder workflow.
  Trigger when the user asks to 推送/发送/通知/广播 到 飞书/企业微信/钉钉/Slack/Telegram/邮件、
  统一通知、多通道推送、群消息自动化、定时提醒、选股结果推送、监控告警推送、日报推送.
agent_created: true
license: MIT-0
---

# notify-hub — 让 Agent 的产出自动送到你眼前

**选股扫描、监控告警、日报周报，定义一次内容，广播到任意通道。** 调用方只描述"发什么"（text / card / file），`--to` 指定"发到哪"，与通道彻底解耦。新增通道 = 加一个 adapter 文件，核心不动。

## When to use

- 往飞书/企业微信/钉钉/Slack/Telegram/邮件发通知、提醒、告警
- **同一份内容广播到多个通道**（如报告同时推飞书群 + 邮件）
- 发结构化卡片（表格、按钮、跳转链接），各通道自动降级渲染
- 作为其他 skill 的"最后一步"：VPS 扫描完 → 推卡片；监控告警 → 推文本
- 发文件（邮件附件、Telegram 文档）

## When NOT to use

- 目标是个人微信 / 其他未支持的通道
- 需要读取/回复消息、撤回、回调交互（这些 webhook/机器人无权限）
- 只想发纯文本到单一飞书群（可用更轻的 `feishu-send`，但 notify-hub 也能做）

## Prerequisites

- Python 3.7+，零第三方依赖（标准库）。
- 各通道凭据（见 `references/channels-schema.md`）：飞书/企业微信/钉钉/Slack 是群机器人 webhook；Telegram 是 Bot token + chat_id；邮件是 SMTP。

## 快速开始

```bash
# 0. 零配置体验：预览同一张卡片在各通道的渲染效果（无需任何凭据）
notify send card examples/card_report.json --dry-run

# 1. 添加目标（凭据存 ~/.notify-hub/config.json，不在 skill 目录）
notify config add feishu 我的群 --url https://open.feishu.cn/open-apis/bot/v2/hook/xxx --secret xxx
notify config add wecom 我的群 --url https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx
notify config list

# 2. 连通性测试
notify test --to feishu:我的群

# 3. 发文本
notify send text "收盘提醒：沪指 +0.5%" --to feishu:我的群

# 4. 发卡片（统一 DSL，各通道自动降级渲染）
notify send card examples/card_report.json --to feishu:我的群,wecom:我的群

# 5. 广播到所有已配置通道
notify send card examples/card_report.json --to all

# 6. 发文件（邮件附件 / Telegram 文档）
notify send file report.pdf --to email:老板 --title "今日报告"
```

脚本路径：`<skill>/scripts/notify.py`（可 `alias notify="python3 <skill>/scripts/notify.py"`）。

## 核心概念

### 三分离

```
Message（发什么）  ×  Channel（通过什么发）  ×  Target（发给谁）
```

### 统一卡片 DSL

```json
{
  "kind": "card",
  "title": "今日扫描 Top5",
  "color": "blue",
  "sections": [
    {"type": "markdown", "content": "**命中 367 只**"},
    {"type": "table", "headers": ["代码","名称","评分"], "rows": [["600583","海油工程","114.7"]]},
    {"type": "button", "text": "查看完整报告", "url": "https://..."},
    {"type": "note", "content": "数据仅供参考"}
  ]
}
```

同一张卡，各通道自动**降级渲染**：飞书渲染成完整卡片（markdown 表格 + 按钮）；企业微信/钉钉把表格降级为文本对齐、按钮降级为链接；Slack 渲染成 blocks；Telegram 渲染成 HTML 文本 + inline keyboard；邮件渲染成 HTML（表格转 `<table>`）。调用方无需关心各通道差异。

## CLI 命令参考

| 命令 | 说明 |
|------|------|
| `config add <通道> <目标名> --url/--token/--smtp-host ...` | 添加目标（凭据字段按通道） |
| `config list` / `config rm` / `config default` | 管理目标 |
| `send text <内容> --to <目标>` | 发文本（支持 `--stdin`） |
| `send card <json或文件> --to <目标>` | 发卡片 |
| `send file <路径> --to <目标>` | 发文件 |
| `test --to <目标>` | 连通性测试 |
| `channels` | 列出支持的通道 |

`--to` 格式：`通道:目标`，逗号分隔即广播，`all` 广播到全部已配置通道。`--to` 省略时发全部已配置通道的默认目标。

## 各通道凭据字段

| 通道 | 凭据字段（config add 的 flag） |
|------|------------------------------|
| feishu | `--url --secret`（secret 可选） |
| wecom | `--url` |
| dingtalk | `--url --secret`（secret 可选） |
| slack | `--url` |
| telegram | `--token --chat-id` |
| email | `--smtp-host --port --user --password --to --sender` |

详细说明见 `references/channels-schema.md`。

## Red lines（安全）

1. **凭据即权限** —— 各通道 webhook/token/SMTP 密码一旦泄漏，任何人都能替你发消息。`~/.notify-hub/config.json` 不要提交公开仓库，不要外发。
2. **不采集、不外发** —— 只向你自己配置的目标发送，不读取任何通道内容，不上传第三方。
3. **内容由调用方负责** —— 推送到群 = 公开发言，发送前确认内容适合该目标。
4. **限流** —— 各通道有频率上限（见 `channels` 命令），脚本已内置节流，勿绕过。

---

通道格式速查：`references/channels-schema.md` ｜ 示例：`examples/card_report.json`

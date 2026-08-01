---
slug: "slack-workspace-free"
name: "slack-workspace-free"
version: "1.0.0"
displayName: "Slack工作区管家LITE"
summary: "Slack基础消息发送与频道列表，ClawLink OAuth托管连接。面向团队协作场景的Slack基础工作区管理技能（免费版）。通过ClawLink OAuth托管连接， 提供频道消息发送"
summary_zh: "Slack基础消息发送与频道列表，ClawLink OAuth托管连接。面向团队协作场景的Slack基础工作区管理技能（免费版）。通过ClawLink OAuth托管连接， 提供频道消息发送"
license: "MIT"
description: "|-. 适用于需要slack workspace相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  面向团队协作场景的Slack基础工作区管理技能（免费版）。通过ClawLink OAuth托管连接，
  提供频道消息发送、频道列表、用户列表三大基础能力.
  支持频道ID寻址、基础消息格式化、频道发现与用户查询.
  适用于通知发布、频道发现、成员查询等基础场景.
tags:
  - Communication
  - slack
  - workspace
  - automation
  - productivity
  - 团队协作
  - 社交
  - 通信
  - clawlink
  - 频道列表
tools:
  - read
  - exec
  - write
homepage: ""
category: "Communication"
pricing_tier: free
---
# Slack工作区管家 LITE（Slack Workspace Free）

面向团队协作场景的Slack基础工作区管理（免费版）。通过ClawLink OAuth托管连接，提供频道消息发送、频道列表、用户列表三大能力.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Slack工作区管家LITE处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent 平台**: 支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **网络**: 需可访问 `https://slack.com/api/*` 及 ClawLink 服务

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| ClawLink 插件 | 集成插件 | 必需 | Agent 平台插件市场安装 `clawlink-plugin` |
| Slack OAuth 连接 | OAuth 授权 | 必需 | 通过 ClawLink Dashboard 连接 Slack 工作区 |
| curl 或等价 HTTP 客户端 | 命令行工具 | 必需 | 系统自带或包管理器安装 |

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令驱动，需 exec 执行 clawlink 命令）
- **说明**: 通过 ClawLink 托管OAuth Token，Agent 调用 `clawlink_call_tool` 驱动 Slack Web API

### 连接说明
**无需在聊天中提供API Token**。ClawLink 安全存储 OAuth Token 并自动注入每个 Slack API 请求.
首次使用需：1) 安装 ClawLink 插件并配对设备；2) 访问 ClawLink Dashboard 连接 Slack 工作区；3) 调用 `clawlink_list_integrations` 验证连接.
## 核心能力

### 1. 频道消息发送
向指定频道发送文本消息。频道参数需使用频道ID（`C0123456789`）。支持基础Slack消息格式化：`*bold*`、`_italic_`、`` `code` ``、emoji语法 `:name:`.
### 2. 频道列表
列出工作区内全部频道，返回频道ID、名称、成员数、是否私有等。可用于频道发现与ID解析.

- 参考`频道列表`的配置文档进行参数调优
### 3. 用户列表
列出工作区内全部用户，返回用户ID、姓名、邮箱、是否在线等。可用于成员查询与用户ID获取.
> **升级提示**：线程回复、定时消息、频道创建/归档/重命名、文件上传/下载、表情反应、提醒、画布、用户组管理、企业Grid审计日志等高级功能仅在 slack-workspace 付费版中提供。- 验证返回数据的完整性和格式正确性
- 参考`用户列表`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 典型输入 | 输出内容 | 涉及能力 |
|---:|---:|---:|---:|
| 通知发布 | 向#general发送会议提醒 | 消息投递确认+时间戳 | 消息发送 |
| 频道发现 | 列出所有频道 | 频道列表（ID、名称、成员数） | 频道列表 |
| 成员查询 | 列出工作区所有用户 | 用户列表（ID、姓名、邮箱） | 用户列表 |

**不适用于**：线程回复、定时消息、频道管理、文件上传、提醒、画布（需升级付费版）

## 使用流程

### 确认连接状态
```bash
clawlink_list_integrations
```
返回列表中包含 `slack` 即已连接。若未连接，引导用户访问 ClawLink Dashboard 连接 Slack.
### 频道名解析为ID
大部分Slack工具需要频道ID。使用 `slack_list_all_channels` 列出频道后按 `name` 字段匹配.
### 发送消息或查询数据
1. 发送消息：`clawlink_call_tool --tool "slack_send_message"`，传 `channel`、`text`
2. 列出频道：`clawlink_call_tool --tool "slack_list_all_channels"`
3. 列出用户：`clawlink_call_tool --tool "slack_list_all_users"`

### 透传结果
4. 发送成功返回 `{ok: true, channel, ts, message}`
5. 频道列表返回 `{ok: true, channels: [{id, name, num_members, ...}]}`
6. 用户列表返回 `{ok: true, members: [{id, name, profile, ...}]}`

#
## 案例展示

### 案例1：通知发布
**场景**：团队需要在 `#general` 频道发布版本发布提醒

**执行**：
```bash
# 列出频道找到#general的ID
clawlink_call_tool --tool "slack_list_all_channels" --params '{}'
# ...
# 发送版本发布提醒
clawlink_call_tool --tool "slack_send_message" --params '{
  "channel": "C0GENERAL01",
  "text": ":rocket: *v2.1.0发布提醒*\n发布窗口：今晚 22:00-23:00\n负责人：@alice\n回滚方案：已准备"
}'
```

**输出**：
```json
// list_all_channels（截取）
{"ok": true, "channels": [{"id": "C0GENERAL01", "name": "general", "num_members": 42}]}
# ...
// send_message
{"ok": true, "channel": "C0GENERAL01", "ts": "1721452800.123456"}
```

**分析**：先通过频道列表解析 `#general` 的ID为 `C0GENERAL01`，再发送消息。时间戳 `1721452800.123456` 可用于后续引用。`:rocket:` 会被渲染为emoji.
## 错误处理

| 错误码 | 错误信息 | 原因分析 | 处理方式 |
|:---:|:---:|:---:|:---:|
| `channel_not_found` | 频道ID不存在或Bot不是成员 | 频道ID拼写错误或频道已删除 | 用 `slack_list_all_channels` 重新获取频道ID |
| `not_authed` | OAuth Token无效或已撤销 | 用户在Dashboard断开了Slack连接 | 引导用户重新连接 Slack |
| `missing_scope` | Token缺少所需权限范围 | 连接时未授权 `chat:write` 等Scope | 引导用户在Dashboard重新授权 |
| `is_archived` | 目标频道已归档（只读） | 向已归档频道发送消息 | 引导用户选择活跃频道 |
| `rate_limited` | 触发速率限制 | 请求频率超过Slack限制 | 等待后检查网络连接和配置后重试，建议间隔1秒 |

## 常见问题

### Q1：如何连接Slack工作区？
A：安装 ClawLink 插件后，访问 ClawLink Dashboard，点击连接Slack，完成OAuth授权。授权后调用 `clawlink_list_integrations` 验证连接，再调用 `clawlink_list_tools --integration slack` 确认工具可用。全程无需手动提供API Token.
### Q2：如何找到频道ID？
A：调用 `slack_list_all_channels` 列出工作区全部频道，返回结果中每个频道包含 `id`（以 `C` 开头）和 `name` 字段。按 `name` 匹配目标频道名即可获取对应ID。普通频道ID以 `C` 开头，DM以 `D` 开头，MPDM以 `G` 开头.
### Q3：免费版和付费版有什么区别？
A：免费版（LITE）包含频道消息发送、频道列表、用户列表三大基础功能。付费版（Slack工作区管家）额外提供：
- 线程回复与定时消息
- 频道创建/归档/重命名/话题设置/邀请成员
- 对话历史与线程获取
- 文件上传/下载/删除
- 表情反应、提醒、置顶与星标
- Canvas画布创建与编辑
- 用户组管理与企业Grid审计日志
- 自定义emoji管理
- 60+ 工具覆盖12大能力域（vs 免费版3个基础工具）
- 3 个完整案例（vs 免费版 1 个）
- 8 种错误处理（vs 免费版 5 种）

### Q4：Bot为什么发不出消息？
A：常见原因：1) OAuth Token缺少 `chat:write` 权限，需在Dashboard重新授权；2) Bot未加入目标频道，需在Slack中用 `/invite @botname` 邀请；3) 频道ID错误，建议先用 `slack_list_all_channels` 确认。检查返回的 `error` 字段可定位具体原因.
## 已知限制

1. **基础功能**：仅支持消息发送、频道列表、用户列表，不支持线程回复、频道管理、文件操作、提醒等（需升级付费版）
2. **需频道ID**：发送消息需手动提供频道ID，不支持频道名自动解析（付费版支持 `slack_find_channels` 搜索）
3. **无写操作预览**：不支持 `clawlink_preview_tool` 写操作预览（付费版支持预览+确认流程）
4. **仅基础查询**：不支持对话历史、用户在线状态、文件列表等高级查询（需升级付费版）
5. **无定时消息**：不支持消息定时发送与提醒创建（需升级付费版）

---
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> **需要更多能力？** 升级到 slack-workspace 付费版获取线程回复、定时消息、频道管理、文件操作、提醒、画布、用户组管理、企业Grid审计等60+工具覆盖12大能力域的高级功能.
---
name: email-triage
description: 电子邮件智能整理与优先级排序。每天早上自动拉取用户邮箱全文件夹未读邮件，LLM 分析后按 T0-T3 四级分级生成 HTML 看板，保存至桌面「邮件日报」文件夹，并通过企微/微信推送简报。适用于需要快速掌握当日邮件火势、按优先级处理工作邮件的场景。
version: 1.0.0
agent_created: true
tags: [email, triage, morning-brief, automation, microsoft-graph]
---

# email-triage — 邮件智能日报

## 触发场景

- 用户需要「整理邮件」「邮件日报」「邮件优先级排序」
- WB 每日 Automation 自动触发（工作日早上，默认 8:50 AM，可配置）
- 用户手动说「跑一下邮件日报」

## 分级体系

| 等级 | 标签 | 判定标准 |
|------|------|----------|
| 🔴 **T0** | 立刻处理 | 涉及资金/授信/合规/高管指令 + 正文 @用户 + 已标记旗子(flag)或颜色(category) + 待处理后续 |
| 🟡 **T1** | 今天内 | 业务相关、跨部门协作、外部合作方 + 正文含直接称呼（如 Hi {name} / Dear {name}） |
| 🟢 **T2** | 本周 | 信息同步、会议邀请、周报、系统通知 |
| ⚪ **T3** | 可忽略 | 无需行动的群发、newsletter、自动报告 |

## T0 增强判定

T0 的基础是高重要性 + 资金/授信/合规邮件。以下任一条件满足即触发 T0：
- 邮件正文包含 `@{username}` 的 @提及
- `flag.flagStatus` 为 `flagged`
- `categories` 数组非空（有颜色标记）
- `importance` 为 `high`
- 主题或正文涉及关键词：`urgent`/`紧急`/`授信`/`credit line`/`付款`/`payment`/`compliance`/`合规`/`deadline`/`截止`

## T1 直接称呼检测

检测正文前 500 字符是否包含用户名的直接称呼（需根据实际用户名配置）：
- `Hi {name}` / `Dear {name}` / `Hello {name}`
- `{name} 你好` / `{name}，`

## 输出看板

### 桌面 HTML
- 位置: `~/Desktop/邮件日报/YYYY-MM-DD.html`（跨平台路径，Windows 下自动解析为 `C:\Users\{user}\Desktop\`）
- 格式: 响应式 HTML 看板，T0-T2 分组展开，T3 折叠列表
- 每条 T0-T2 展示: 发件人、主题、一句话要点、收到时间、是否有附件、Flag/Category、是否 @用户
- T3 仅展示: 发件人 + 主题

### 推送简报
- 通过企微 skill 或微信 skill 发送文字消息（可选）
- 格式: `📬 邮件早报 (YYYY-MM-DD) | T0×N 🔴 / T1×N 🟡 / T2×N 🟢 / T3×N ⚪ | 详情见桌面邮件日报`
- 如消息渠道不可用，仅保存 HTML 文件

## 技术实现

### 邮件获取
- 使用 `mcp__microsoft__list-mail-messages` + `$filter=isRead eq false` + `$count=true`
- 分页抓取全部未读邮件（使用 `@odata.nextLink` 遍历）
- 字段: `id,subject,from,toRecipients,receivedDateTime,bodyPreview,isRead,hasAttachments,flag,importance,categories`
- 每封读取 `bodyPreview`（首 255 字符），需要深度分析时用 `get-mail-message` 拉完整正文

### LLM 分级
- 将邮件列表发送给 WorkBuddy 内置 LLM 做 T0-T3 分类
- 提供分级 Prompt（含 T0 关键词库、T1 称呼列表）
- LLM 返回每封邮件的 `tier` + `summary`（一句话要点，T0-T2 必须有）

### HTML 生成
- Agent 调用 Microsoft MCP 工具获取邮件
- LLM 完成分级后，按 HTML 模板渲染看板
- HTML 样式: 浅色主题，卡片式布局，响应式设计
- 默认打开为浏览器预览

### 去重与状态保护
- **只在 GET 请求读取邮件，绝不主动 PATCH isRead=true**
- 处理完后扫描所有取到的邮件，若发现 `isRead: true`（意外被标已读），立即 PATCH 回去 `isRead: false`

## 文件结构

```
~/.workbuddy/skills/email-triage/
├── SKILL.md                    # 本文件
└── scripts/
    ├── execution-prompt.md     # Automation 执行 prompt
    └── template.html           # HTML 看板模板
```

## 依赖

- Microsoft MCP 连接器（需用户自行配置，端点因组织而异）
- WorkBuddy Agent 运行环境
- 企微 / 微信推送 channel（可选）

## 配置说明（用户使用前需修改）

1. **Microsoft MCP 端点**：在 `~/.workbuddy/mcp.json` 配置你所在组织的 Microsoft Graph MCP 端点
2. **用户邮箱**：MCP 连接后自动读取当前登录用户邮箱，无需手动配置
3. **称呼检测**：在 `execution-prompt.md` 中将 `{name}` 替换为你的实际名字（用于 T1 直接称呼检测）
4. **推送渠道**：根据可用渠道选择企微或微信（可选）
5. **触发时间**：通过 WB Automation 配置，默认工作日 8:50 AM

---
slug: "slack-free"
name: "slack-free"
version: "1.0.0"
displayName: "Slack 消息 LITE"
summary: "通过slack工具发送与读取Slack消息,支持频道通知与历史消息查询。Slack 消息管理(免费版)。通过 slack 工具对 Slack 工作区进行基础消息操作,涵盖两大动作组: mes"
summary_zh: "通过slack工具发送与读取Slack消息,支持频道通知与历史消息查询。Slack 消息管理(免费版)。通过 slack 工具对 Slack 工作区进行基础消息操作,涵盖两大动作组: mes"
license: "MIT"
description: "|-. 适用于需要slack相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  Slack 消息管理(免费版)。通过 slack 工具对 Slack 工作区进行基础消息操作,涵盖两大动作组:
  messages(发送消息与读取消息)。工具使用已配置的 Bot Token 进行认证,支持 channel 与 user
  两种消息目标。适用于发送频道通知、读取频道历史等基础场景.
  如需消息回应(reactions)、置顶管理(pins)、成员信息查询(memberInfo)、表情列表(emojiList)、
  消息编辑与删除等高级能力,请升级至 slack 付费版.
tags:
  - Communication
  - slack
  - automation
  - productivity
  - developer-tools
  - Collaboration
  - 社交
  - 通信
  - bot
  - channelid
tools:
  - read
  - write
  - exec
homepage: ""
category: "Communication"
pricing_tier: free
---
# Slack 消息 LITE

通过 `slack` 工具对 Slack 工作区进行基础消息操作,涵盖发送消息与读取消息两大动作组。工具使用已配置的 Bot Token 进行认证.
## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Slack 工作区**: 需有已创建的 Slack 工作区与频道

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---|---|----|----|
| slack 工具 | Agent 平台工具 | 必需 | Agent 平台内置或插件提供 |
| Slack Bot Token | 凭证 | 必需 | 在 Slack App 配置页面创建 Bot 并获取 xoxb- 前缀的 Token |
| Bot 权限范围 | 配置 | 必需 | 在 Slack App 配置页授予 chat:write 与 channels:read 等 scope |

### API Key 配置
- Slack Bot Token 由 Agent 平台统一配置,无需在 Skill 中硬编码
- Bot 需被邀请加入目标频道(``/invite @botname``),否则消息操作会报 not_in_channel 错误

### 可用性分类
- **分类**: MD+EXEC模式纯 Markdown 指令,消息操作需要 exec 调用 slack 工具)
- **说明**: 基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 执行 Slack 操作

## 核心能力

### 1. 发送消息(sendMessage)
- **消息目标**: 向 channel 或 user 发送文本消息,to 字段格式为 `channel:<id>` 或 `user:<id>`
- **文本内容**: 通过 content 字段指定消息文本,支持纯文本
- **返回结果**: 发送成功后返回 ok 状态与消息时间戳(ts),可用于后续操作
- **使用场景**: 发送通知消息、发布站务公告、向同事发送提醒

### 2. 读取消息(readMessages)
- **频道历史**: 获取指定频道最近 N 条消息(通过 limit 参数控制数量)
- **返回字段**: 每条消息含消息文本(text)、发送者(user)、时间戳(ts)
- **上下文复用**: 返回的 ts 字段与 user 字段可用于后续操作
- **使用场景**: 了解频道最近讨论内容、获取消息时间戳用于引用
### 消息目标

针对消息目标,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供消息目标相关的配置参数、输入数据和处理选项.
**输出**: 返回消息目标的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`消息目标`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 输入采集

- **channelId**: Slack 频道 ID,格式为 C 开头的字符串(如 C0LPBBKMQ)
- **to**: 消息发送目标,格式为 `channel:<id>` 或 `user:<id>`
- **content**: 消息文本内容
- **limit**: 读取消息数量,整数(如 20)

消息上下文行中包含 `slack message id` 与 `channel` 字段,可直接复用.
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 发送通知消息 | 目标频道 channelId 与通知文本 | 频道收到通知消息 |
| 查询频道历史 | 频道 channelId 与读取数量 | 返回最近 N 条消息内容与发送者信息 |

**不适用于**: 需要消息回应(reactions)的场景(需升级付费版);需要置顶管理(pins)的场景(需升级付费版);需要编辑或删除消息的场景(需升级付费版).
## 使用流程

1. **确认 Bot 已配置**: 确保 Agent 平台已配置 slack 工具与 Bot Token,Bot 已被邀请加入目标频道
2. **采集必要输入**: 根据要执行的动作,准备 channelId、to、content、limit 等参数
3. **组装 JSON 调用**: 按对应动作的 JSON 格式组装调用参数,指定 action 字段
4. **执行 slack 工具**: 通过 exec 调用 slack 工具,传入组装好的 JSON 参数
5. **检查返回结果**: 确认操作成功(如 sendMessage 返回 ok 与 message ts),失败时根据错误信息排查

## 动作调用格式

### 发送消息

```json
{
  "action": "sendMessage",
  "to": "channel:C123",
  "content": "周报已更新,请查看"
}
```

### 读取消息

```json
{
  "action": "readMessages",
  "channelId": "C123",
  "limit": 20
}
```

## 案例展示

### 案例 1: 向开发频道发送版本发布通知

**场景**: 向开发频道发送版本发布通知,告知团队上线时间

**操作**:

```json
{
  "action": "sendMessage",
  "to": "channel:C0LPBBKMQ",
  "content": "v2.3.0 版本即将发布,预计今日 18:00 上线,请各位关注发布窗口"
}
```

**返回结果**:

```json
{
  "ok": true,
  "message": {
    "ts": "1712023500.5678",
    "text": "v2.3.0 版本即将发布,预计今日 18:00 上线,请各位关注发布窗口"
  }
}
```

**分析**: sendMessage 向指定频道发送文本通知,返回的 ts 字段为消息时间戳。to 字段用 `channel:` 前缀加 channelId 指定目标频道。Bot 需已加入该频道,否则会报 not_in_channel 错误.
### 案例 2: 读取频道最近讨论内容

**场景**: 需要了解开发频道最近的讨论内容,获取最近 10 条消息

**操作**:

```json
{
  "action": "readMessages",
  "channelId": "C0LPBBKMQ",
  "limit": 10
}
```

**返回结果**:

```json
{
  "messages": [
    {
      "ts": "1712023032.1234",
      "text": "这个 bug 我已经修复了",
      "user": "U0ABC"
    },
    {
      "ts": "1712023100.2345",
      "text": "感谢,我来验证一下",
      "user": "U0DEF"
    }
  ]
}
```

**分析**: readMessages 返回指定频道最近 N 条消息,每条含文本、发送者 userId 与时间戳。limit 参数控制返回数量。返回的 ts 与 user 字段可用于后续引用或操作.
## 异常处理

| 错误场景 | 错误现象 | 原因分析 | 处理方式 |
|---:|---:|---:|---:|
| channelId 无效 | 返回 `{"ok": false, "error": "channel_not_found"}` | channelId 拼写错误或频道不存在 | 核对 channelId 格式(C 开头),在 Slack 频道详情中确认正确 ID |
| Bot 未加入频道 | 返回 `{"ok": false, "error": "not_in_channel"}` | Bot 未被邀请加入目标频道 | 在频道中执行 `/invite @botname` 邀请 Bot 加入 |
| 权限不足 | 返回 `{"ok": false, "error": "missing_scope"}` | Bot Token 未授予 chat:write 或 channels:read scope | 在 Slack App 配置页授予对应 scope 后重新安装 App |
| 消息内容为空 | 返回 `{"ok": false, "error": "no_text"}` | sendMessage 的 content 字段为空字符串 | 确保 content 字段含至少一个非空白字符 |
| Bot Token 无效 | 返回 `{"ok": false, "error": "invalid_auth"}` | Bot Token 过期或已被撤销 | 在 Slack App 配置页重新生成 Bot Token,更新 Agent 平台配置 |

## 常见问题

### Q1: 如何获取频道的 channelId?
A: 在 Slack 客户端中,右键点击频道名称选择「查看频道详情」,channelId 显示在详情页底部或 URL 中,格式为 C 开头的字符串(如 C0LPBBKMQ)。也可通过 readMessages 读取消息时从返回结果的 channel 字段获取.
### Q2: sendMessage 的 to 字段如何指定消息目标?
A: to 字段支持两种格式。发到频道用 `channel:<channelId>`(如 `channel:C0LPBBKMQ`),Bot 需已加入该频道。发给个人用 `user:<userId>`(如 `user:U0ABC`),Bot 需与该用户有过对话历史。两种格式的前缀(channel: 或 user:)不可省略.
### Q3: Bot 如何加入频道?
A: Bot 不能自行加入频道,需由频道成员邀请。在频道中执行 `/invite @botname` 即可邀请 Bot。Bot 加入频道后才能执行 sendMessage 与 readMessages 等操作,否则会报 not_in_channel 错误.
### Q4: 免费版与付费版有什么区别?
A: 免费版(LITE)包含发送消息(sendMessage)与读取消息(readMessages)两大基础功能。付费版(Slack 消息管理)额外提供:
- Reactions(消息回应:添加 emoji 回应与列出回应)
- Pins(置顶管理:置顶、取消置顶、列出置顶消息)
- MemberInfo(成员信息查询)
- EmojiList(自定义表情列表)
- 消息编辑(editMessage)与删除(deleteMessage)
- 更多案例展示(3 个完整案例 vs 2 个基础案例)
- 更详细的异常处理(8 种场景 vs 5 种基础场景)
- 6 个领域专属 FAQ

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- **功能限制**: 仅支持发送与读取消息,不支持回应、置顶、成员查询、表情列表、消息编辑与删除(需升级付费版)
- **仅支持文本消息**: sendMessage 只能发送纯文本,不支持文件附件与图片
- **Bot 需被邀请**: Bot 无法自行加入频道,需频道成员手动邀请后才能操作
- **权限依赖 scope 配置**: 发送消息需 chat:write scope,读取消息需 channels:read scope
- **不支持消息搜索**: 无法按关键词搜索历史消息

---
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

## 升级提示

本免费版提供发送消息与读取消息两大基础功能。如需消息回应(reactions)、置顶管理(pins)、成员信息查询(memberInfo)、表情列表(emojiList)、消息编辑与删除等高级能力,请升级至 **slack** 付费版,获取完整的五大动作组消息管理能力.
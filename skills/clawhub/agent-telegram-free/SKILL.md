---
slug: "agent-telegram-free"
name: "agent-telegram-free"
version: "1.0.0"
displayName: "Agent TG LITE"
summary: "Agent Telegram 基础通信规范，支持 3 类角色消息发送。"
license: "MIT"
description: |-
  Agent Telegram 通信规范免费版。定义 main、backend、frontend 三类基础 Agent 角色的 accountId、
  emoji 标识与消息发送格式。Agent 向用户发送 Telegram 消息时使用 message 工具配合 accountId 与 target 字段，
  确保消息正确路由到用户账号。覆盖任务开始与任务完成两类基础汇报时机.
  适用于单 Agent 消息发送、基础任务进度通知等场景.
tags:
  - 通用办公
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Agent Telegram LITE

Agent Telegram 通信规范免费版。定义 3 类基础 Agent 角色的账号映射与消息发送格式，Agent 向用户发送 Telegram 消息时遵循此规范.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Agent TG LITE处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 核心能力

- **3 类基础角色账号映射**：为每个 Agent 分配独立的 `accountId` 与 emoji 标识
  - main（9527）→ `default` → 🤖 主控 Agent
  - backend（老崔）→ `backend` → 🔧 后端工程师
  - frontend（小白）→ `frontend` → 🎨 前端工程师
- **统一消息格式**：所有消息通过 `message` 工具发送，必填字段 `action: "send"`、`channel: "telegram"`、`accountId`、`target: "5440561025"`、`message`
- **两类汇报时机**：收到任务立即汇报、完成子任务汇报
- **基础消息模板**：任务开始、任务完成两类模板
### 3 类基础角色账号映射

针对3 类基础角色账号映射,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供3 类基础角色账号映射相关的配置参数、输入数据和处理选项.
**输出**: 返回3 类基础角色账号映射的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`类基础角色账号映射`的配置文档进行参数调优
### 统一消息格式

针对统一消息格式,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供统一消息格式相关的配置参数、输入数据和处理选项.
**输出**: 返回统一消息格式的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`统一消息格式`的配置文档进行参数调优
### 两类汇报时机

针对两类汇报时机,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供两类汇报时机相关的配置参数、输入数据和处理选项.
**输出**: 返回两类汇报时机的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`两类汇报时机`的配置文档进行参数调优
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 单 Agent 消息发送 | backend 完成 API 开发 | 🔧 前缀消息汇报接口文档路径 |
| 基础任务进度通知 | frontend 完成页面开发 | 🎨 前缀消息汇报页面文件路径 |

**不适用于**：多角色协作、问题上报决策、架构师/产品/内容/爬虫/QA 角色通信等高级场景.
## 使用流程

1. **识别当前 Agent 角色**：确定自己的 `accountId` 与 emoji（如后端工程师用 `backend` / 🔧）。不确定时回退为 `default` / 🤖
2. **组装消息内容**：按消息模板填充任务名、输出文件路径等字段，消息前缀加 emoji
3. **调用 message 工具发送**：使用标准格式 `message({action: "send", channel: "telegram", accountId: "<你的accountId>", target: "5440561025", message: "<emoji> <内容>"})`
4. **校验 accountId**：确认 accountId 拼写正确，target 固定为 `5440561025`

## 消息格式规范

### 标准发送格式

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "<你的accountId>",
  target: "5440561025",
  message: "<你的emoji> <内容>"
})
```

### 消息模板

**任务开始模板**：

```text
<emoji> 收到任务：<任务名>
📝 开始执行...
```

**任务完成模板**：

```text
<emoji> <任务名> 完成
✅ 已完成: <子任务>
📁 输出: <文件路径>
```

## 账号映射表

| Agent | 负责人 | accountId | Emoji |
|---:|---:|---:|---:|
| main | 9527 | `default` | 🤖 |
| backend | 老崔 | `backend` | 🔧 |
| frontend | 小白 | `frontend` | 🎨 |

**用户 Telegram ID**：`5440561025`（固定值）

## 案例展示

### 案例 1：后端工程师汇报 API 开发完成

**触发**：backend 完成 API 接口开发

**发送内容**：

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "backend",
  target: "5440561025",
  message: "🔧 API 接口开发完成，接口文档：~/Desktop/project/docs/backend/api.md"
})
```

**用户收到**：Telegram 收到 `🔧 API 接口开发完成，接口文档：~/Desktop/project/docs/backend/api.md`

### 案例 2：前端工程师汇报页面开发完成

**触发**：frontend 完成登录页面开发

**发送内容**：

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "frontend",
  target: "5440561025",
  message: "🎨 登录页面开发完成\n✅ 已完成: 登录表单与校验逻辑\n📁 输出: ~/Desktop/project/src/pages/login.vue"
})
```

**用户收到**：Telegram 收到带子任务与输出文件路径的完成消息

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 消息发不出去，无任何响应 | 忘记填写 `accountId` 字段 | 必须指定你的 accountId，参照账号映射表 |
| 消息未送达 Telegram | 误用 `sessions_send` 等其他工具 | 必须使用 `message` 工具，channel 固定为 `telegram` |
| 消息发给错误用户 | target 字段写错 | target 固定为 `5440561025`，不得使用其他值 |
| message 工具未找到 | Agent 平台未配置 message 工具 | 检查 `~/.skill-platform/skill-platform.json` 中 `channels.telegram` 配置 |
| 消息超长被截断 | Telegram 单条消息上限 4096 字符 | 拆分为多条消息发送 |

## 常见问题

### Q1：可以用 `sessions_send` 工具发 Telegram 消息吗？
A：不可以。`sessions_send` 是 Agent 会话内部通信工具，不会将消息路由到 Telegram。必须使用 `message` 工具并指定 `channel: "telegram"`.
### Q2：target 字段可以改成其他用户 ID 吗？
A：不可以。本规范约定所有 Agent 消息统一发送给用户 `5440561025`.
### Q3：免费版支持哪些角色？
A：免费版仅支持 main、backend、frontend 三类基础角色。如需 architect、product、content、crawler、qa 等角色，请升级付费版.
### Q4：如何配置 Telegram Bot？
A：在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts` 节点下配置 Bot Token。Bot Token 通过 @BotFather 创建获取.
## 已知限制

- 仅支持 main、backend、frontend 三类角色，不支持 architect/product/content/crawler/qa
- target 固定为 `5440561025`，不支持向其他用户发送消息
- 消息内容上限 4096 字符，超长需拆分多条
- 不支持"遇到问题"模板与问题上报决策流程
- 不支持多角色协作与 main 汇总流程
- 依赖 Agent 平台已配置 message 工具与 Telegram Bot Token

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 Telegram Bot API（`https://api.telegram.org`）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| message 工具 | Agent 平台工具 | 必需 | Agent 平台内置或插件提供 |
| Telegram Bot Token | 凭证 | 必需 | 通过 @BotFather 创建 Bot 获取 |
| skill-platform.json | 配置文件 | 必需 | `~/.skill-platform/skill-platform.json` 中配置 accounts |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供决策能力 |

### API Key 配置
- Telegram Bot Token 配置在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.<accountId>.token` 字段

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，消息发送需要 exec 调用 message 工具）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务

---

## 升级提示

当前为免费版，仅支持 3 类基础角色与两类汇报时机。如需以下完整功能，请升级付费版：

- **8 类角色账号映射**：新增 architect（🏗️）、product（🟡）、content（✍️）、crawler（🕷️）、qa（🧪）角色
- **四类汇报时机**：新增"遇到问题"汇报时机与问题上报决策流程
- **"遇到问题"消息模板**：含问题描述与建议方案的标准化模板
- **多角色协作流程**：main 分发任务 → 各角色执行并汇报 → main 汇总结果
- **product 角色 sproduct 约定**：避免 JavaScript 保留字冲突的特殊 accountId 处理
- **文件附件发送**：支持通过 attachment 字段直接发送文件
- **多 Bot 独立路由**：每个角色使用独立 Bot Token，消息互不干扰

升级至付费版：`https://SkillHub.ai/skill/agent-telegram`

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Agent TG LITE处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "agent-telegram"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```

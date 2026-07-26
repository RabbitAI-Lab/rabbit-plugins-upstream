---
slug: "agent-telegram"
name: "agent-telegram"
version: 1.0.1
displayName: "Agent Telegram"
summary: "Agent 团队 Telegram 通信规范，统一 8 类角色消息发送与汇报。"
license: "Proprietary"
description: |-
  Agent 团队 Telegram 通信规范。定义 main、architect、backend、frontend、product、content、crawler、qa
  共 8 类 Agent 角色的 accountId、emoji 标识与消息发送格式。所有 Agent 向用户发送 Telegram 消息时必须遵循此规范，
  统一使用 message 工具配合 accountId 与 target 字段，确保消息正确路由到用户账号.
  覆盖任务开始、子任务完成、遇到问题、任务全部完成四类汇报时机，提供标准化消息模板与多角色协作流程.
  适用于多 Agent 协作开发、自动化工作流通知、团队任务进度同步、问题上报决策等场景.
tags:
  - 通用办公
  - Automation
  - Collaboration
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Agent Telegram

所有 Agent 向用户（Legend）发送 Telegram 消息时必须遵循此规范。规范定义了 8 类 Agent 角色的账号映射、消息格式、汇报时机与消息模板，确保多 Agent 协作时消息统一路由到用户 Telegram 账号 `5440561025`.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Agent Telegram处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Agent Telegram类角色消息发送 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |
| 通信记录归档与检索 | 不支持 | 支持 |

## 核心能力

- **8 类角色账号映射**：为每个 Agent 分配独立的 `accountId` 与 emoji 标识，消息前缀带 emoji 便于用户快速识别来源
  - main（9527）→ `default` → 🤖 主控 Agent，负责任务分发与汇总
  - architect（亮亮）→ `architect` → 🏗️ 架构师，负责系统设计与技术选型
  - backend（老崔）→ `backend` → 🔧 后端工程师，负责 API 与服务端开发
  - frontend（小白）→ `frontend` → 🎨 前端工程师，负责界面与交互开发
  - product（小黄）→ `sproduct` → 🟡 产品经理，负责需求文档与优先级
  - content（世龙）→ `content` → ✍️ 内容运营，负责文案与素材
  - crawler（湘君）→ `crawler` → 🕷️ 爬虫工程师，负责数据采集
  - qa（赵飞）→ `qa` → 🧪 测试工程师，负责质量验证
- **统一消息格式**：所有消息通过 `message` 工具发送，必填字段 `action: "send"`、`channel: "telegram"`、`accountId`、`target: "5440561025"`、`message`
- **四类汇报时机**：收到任务立即汇报、每完成子任务汇报、遇到问题汇报、任务全部完成汇报
- **标准化消息模板**：任务开始、任务完成、遇到问题三类模板，统一 emoji 与字段格式
- **多角色协作流程**：main 分发任务 → 各角色执行并汇报 → main 汇总结果，支持任务在角色间流转
- **配置集中管理**：账号配置统一存放在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts` 节点
### 8 类角色账号映射

针对8 类角色账号映射,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供8 类角色账号映射相关的配置参数、输入数据和处理选项.
**输出**: 返回8 类角色账号映射的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`类角色账号映射`的配置文档进行参数调优
### 统一消息格式

针对统一消息格式,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供统一消息格式相关的配置参数、输入数据和处理选项.
**输出**: 返回统一消息格式的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`统一消息格式`的配置文档进行参数调优
### 四类汇报时机

针对四类汇报时机,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供四类汇报时机相关的配置参数、输入数据和处理选项.
**输出**: 返回四类汇报时机的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`四类汇报时机`的配置文档进行参数调优
#
## 适用场景

| 场景 | 输入 | 输出 |
|---:|---:|---:|
| 多 Agent 协作开发 | main 分发需求给 product+backend+frontend | 三位 Agent 分别以 🟡🔧🎨 前缀向用户 Telegram 发送任务接收与完成消息 |
| 自动化工作流通知 | crawler 完成数据采集任务 | 🕷️ 前缀消息汇报采集结果，含输出文件路径 `~/Desktop/project/data/output.json` |
| 团队任务进度同步 | backend 完成 API 开发子任务 | 🔧 前缀消息汇报接口文档路径，main 汇总后转发用户 |
| 问题上报决策 | qa 测试发现阻塞性 bug | 🧪 前缀消息汇报问题描述与建议方案，请求用户决策 |

**不适用于**：垃圾信息群发、非 Telegram 渠道的消息推送、需要端到端加密的敏感通信、跨团队的大规模广播.
## 使用流程

1. **识别当前 Agent 角色**：根据执行上下文确定自己的 `accountId` 与 emoji（如后端工程师用 `backend` / 🔧）。不确定时回退为 `default` / 🤖
2. **组装消息内容**：按消息模板填充任务名、子任务、输出文件路径、问题描述等字段，消息前缀加 emoji
3. **调用 message 工具发送**：使用标准格式 `message({action: "send", channel: "telegram", accountId: "<你的accountId>", target: "5440561025", message: "<emoji> <内容>"})`
4. **根据时机选择模板**：收到任务用"任务开始"模板，完成子任务用"任务完成"模板，遇到问题用"遇到问题"模板
5. **校验 accountId 拼写**：product 角色用 `sproduct`（非 `product`），其余角色 accountId 与角色名一致
6. **确认 target 固定值**：target 始终为 `5440561025`，不得使用其他用户 ID
7. **多角色协作时由 main 汇总**：各角色汇报后，main 收集所有子任务结果统一向用户发送最终汇总消息

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

**遇到问题模板**：

```text
<emoji> <任务名> 遇到问题
❌ 问题: <描述>
💡 建议: <解决方案或请求决策>
```

## 账号映射表

| Agent | 负责人 | accountId | Emoji | 职责 |
|:----:|:----:|:----:|:----:|:----:|
| main | 9527 | `default` | 🤖 | 任务分发与结果汇总 |
| architect | 亮亮 | `architect` | 🏗️ | 系统设计与技术选型 |
| backend | 老崔 | `backend` | 🔧 | API 与服务端开发 |
| frontend | 小白 | `frontend` | 🎨 | 界面与交互开发 |
| product | 小黄 | `sproduct` | 🟡 | 需求文档与优先级 |
| content | 世龙 | `content` | ✍️ | 文案与素材 |
| crawler | 湘君 | `crawler` | 🕷️ | 数据采集 |
| qa | 赵飞 | `qa` | 🧪 | 质量验证 |

**用户 Telegram ID**：`5440561025`（固定值，所有消息 target 字段均用此值）

## 案例展示

### 案例 1：产品经理发送需求文档完成消息

**触发**：product 完成 PRD 撰写

**发送内容**：

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "sproduct",
  target: "5440561025",
  message: "🟡 需求文档已完成，请查看：~/Desktop/project/docs/product/001-prd.md"
})
```

**用户收到**：Telegram 收到一条 `🟡 需求文档已完成，请查看：~/Desktop/project/docs/product/001-prd.md`

### 案例 2：后端工程师汇报 API 开发完成

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

### 案例 3：QA 上报阻塞性 bug

**触发**：qa 测试发现登录接口返回 500

**发送内容**：

```javascript
message({
  action: "send",
  channel: "telegram",
  accountId: "qa",
  target: "5440561025",
  message: "🧪 登录接口测试遇到问题\n❌ 问题: POST /api/login 返回 500，数据库连接池耗尽\n💡 建议: 后端检查连接池配置，建议将 max_connections 从 10 提升至 50"
})
```

**用户收到**：Telegram 收到带问题描述与建议方案的决策请求消息

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 消息发不出去，无任何响应 | 忘记填写 `accountId` 字段 | 必须指定你的 accountId，参照账号映射表（如 backend 用 `backend`） |
| 消息未送达 Telegram | 误用 `sessions_send` 等其他工具 | 必须使用 `message` 工具，channel 固定为 `telegram` |
| product 角色报"账号不存在" | product 误用 `accountId: "product"` | product 的正确 accountId 是 `sproduct`（带 s 前缀），非 `product` |
| 消息发给错误用户 | target 字段写错或用了其他用户 ID | target 固定为 `5440561025`，不得使用其他值 |
| message 工具未找到 | Agent 平台未配置 message 工具或未启用 | 检查 `~/.skill-platform/skill-platform.json` 中 `channels.telegram` 配置 |
| Telegram 账号未绑定 Bot | accounts 节点缺少对应 accountId 的 Bot Token | 在配置文件 `channels.telegram.accounts` 下补充该角色的 Bot Token |
| 消息内容含非法字符 | message 含未转义引号或换行符异常 | 对引号转义，换行用 `\n`，避免直接粘贴未格式化文本 |
| 消息超长被截断 | Telegram 单条消息上限 4096 字符 | 拆分为多条消息发送，或附件形式上传长文本 |

## 常见问题

### Q1：product 角色的 accountId 为什么是 `sproduct` 而不是 `product`？
A：`product` 是 JavaScript 保留字，作为 accountId 会引发语法冲突。因此 product 角色统一使用 `sproduct`（safe product 缩写）。这是历史遗留约定，所有 product 角色消息必须用 `sproduct`.
### Q2：可以用 `sessions_send` 工具发 Telegram 消息吗？
A：不可以。`sessions_send` 是 Agent 会话内部通信工具，不会将消息路由到 Telegram。必须使用 `message` 工具并指定 `channel: "telegram"`，消息才会通过 Telegram Bot 发送给用户.
### Q3：target 字段可以改成其他用户 ID 吗？
A：不可以。本规范约定所有 Agent 消息统一发送给用户 `5440561025`。若需向其他用户发送消息，需另行配置多用户路由，不在本规范范围内.
### Q4：如何新增一个 Agent 角色？
A：在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts` 下新增一个账号节点，配置 Bot Token 与 accountId，然后在本文档账号映射表追加一行。新角色的 emoji 自选，建议与职责语义相关.
### Q5：消息中可以发送文件吗？
A：可以。在 message 内容中包含文件路径（如 `~/Desktop/project/docs/api.md`），用户可点击路径查看。如需直接发送文件附件，需使用 message 工具的 `attachment` 字段（若平台支持）或单独的文件上传工具.
### Q6：多个 Agent 同时发消息会冲突吗？
A：不会。每个 Agent 使用独立 accountId 与 Bot Token，消息通过各自的 Bot 发送，互不干扰。用户会在 Telegram 中看到不同 Bot 账号发来的消息，前缀 emoji 进一步区分来源.
## 已知限制

- target 固定为 `5440561025`，不支持向其他用户发送消息
- product 角色的 accountId 为 `sproduct` 而非 `product`，易混淆需特别注意
- 消息内容上限 4096 字符，超长需拆分多条
- 依赖 Agent 平台已配置 message 工具与 Telegram Bot Token
- 不支持端到端加密，敏感信息不应通过此通道传输
- 不支持消息撤回与编辑，发送前需仔细校验内容
- emoji 标识为约定值，不支持运行时动态切换

## 配置位置

- **主配置**：`~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts` 节点
- **本 Skill**：`~/.skill-platform/workspace/skills/agent-telegram/SKILL.md`

**核心口诀**：发送 Telegram 消息 = `message` 工具 + `accountId` + `target: "5440561025"`

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络**：需可访问 Telegram Bot API（`https://api.telegram.org`）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| message 工具 | Agent 平台工具 | 必需 | Agent 平台内置或插件提供 |
| Telegram Bot Token | 凭证 | 必需 | 通过 @BotFather 创建 Bot 获取 |
| skill-platform.json | 配置文件 | 必需 | `~/.skill-platform/skill-platform.json` 中配置 accounts |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供决策能力 |

### API Key 配置
- Telegram Bot Token 配置在 `~/.skill-platform/skill-platform.json` 的 `channels.telegram.accounts.<accountId>.token` 字段
- 每个 Agent 角色对应一个独立的 Bot Token

### 可用性分类
- **分类**：MD+EXEC（纯 Markdown 指令，消息发送需要 exec 调用 message 工具）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Agent Telegram处理结果",
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

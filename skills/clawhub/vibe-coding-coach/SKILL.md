---
name: Vibe Coding Coach
description: >
  AI-powered vibe coding workflow coach — master the art of AI-assisted software development
  in 2026. Build full apps by describing them in plain language using Cursor, Claude Code,
  Bolt.new, Replit, and Lovable. Learn the vibe coding mindset, prompt patterns, workflow
  architecture, debugging strategies, and how to ship from idea to production without
  getting stuck. Covers project scaffolding, iterative refinement, multi-file context
  management, and common failure patterns. Built for non-engineers, startup founders,
  product managers, and developers transitioning to AI-first workflows.
  Keywords: vibe coding, AI coding, Cursor, Claude Code, Bolt.new, no-code AI, app builder,
  AI-assisted development, prompt-to-code, Replit, Lovable, AI workflow.
version: "3.0.1"
---

# Vibe Coding Coach / 氛围编程教练

**Your personal guide to building software the 2026 way — describe it, ship it.**
**用 2026 年的方式做软件：说出来，跑起来。**

Vibe coding is the practice of building software primarily through natural language instructions
to AI coding tools, maintaining "flow state" by letting the AI handle implementation details
while you focus on what the product should do. This skill teaches you how to do it well.

---

## What This Skill Does

- **Tool Selection** — Match your project to the right vibe coding tool
- **Prompt Pattern Library** — Battle-tested prompts for scaffolding, features, debugging, refactoring
- **Workflow Architecture** — Structure your sessions for consistent, production-quality output
- **Context Management** — Keep AI tools focused without losing coherence in large projects
- **Debugging Without Code** — Diagnose and fix issues by describing symptoms
- **Deployment Coaching** — Go from local prototype to live URL with step-by-step guidance
- **Anti-Pattern Recognition** — Spot and avoid the most common vibe coding failure modes
- **Quality Gates & Security Baseline** — Know when AI-written code is safe enough to ship
- **Cost & Usage Management** — Keep AI tool spending predictable while iterating fast

---

## Trigger Phrases

**English:**
- "I want to build an app using AI"
- "vibe coding help"
- "how to use Cursor to build X"
- "Claude Code workflow"
- "build this without coding"
- "my AI-built app is broken"
- "help me prompt for this feature"
- "Bolt.new vs Replit"
- "from idea to deployed app"
- "AI app builder"

**Chinese / 中文:**
- Vibe Coding 教程
- 用 AI 帮我写代码
- Cursor 怎么用
- Claude Code 工作流
- 不会编程怎么做 App
- AI 辅助开发
- 提示词写代码
- 产品经理 AI 开发
- 用 AI 快速搭建项目
- AI 全栈开发
- 零代码 AI 开发
- AI 写的代码能上线吗
- 上下文怎么给 AI
- AI 改坏了旧功能怎么办

---

## Ecosystem & Compliance Updates [2026-09-13] / 生态与合规动态

| 类型 | 内容摘要 | 对开发流程的影响 | 落地动作 | 优先级 |
|-----|---------|---------------|---------|-------|
| 工具迭代 | 主流 AI 编码工具（编辑器类、命令行类、在线生成类）能力持续升级，上下文与多文件编辑成为竞争焦点 | 工具选择从"能不能写"转向"上下文与协作能力" | 选型时把"多文件编辑 + 项目级上下文"作为硬指标 | 高 |
| 上下文工程 | 项目级规则文件（如工具自带的规则文件机制）成为主流实践 | 长期项目的上下文需显式维护 | 建立项目规则文件与项目简报 | 高 |
| 生成代码治理 | 生成代码的可读性、可维护性与来源合规受关注 | 上线前需人工复核与许可核查 | 建立代码复核与依赖许可检查环节 | 高 |
| 依赖与许可 | 第三方依赖引入过快带来许可与供应链风险 | 依赖引入需评估许可与维护状态 | 新增依赖前评估许可类型与维护活跃度 | 高 |
| 数据与隐私 | 编码工具处理代码与配置时需注意敏感信息 | 密钥与客户数据不得进入提示词 | 密钥走环境变量，样例数据脱敏 | 高 |
| 安全基线 | AI 生成代码在认证、授权、输入校验上易留缺口 | 安全敏感功能需专业复核 | 认证/支付/隐私相关功能设强制复核卡点 | 高 |
| 成本管理 | 按用量计费模式下，迭代成本可能失控 | 需要一个"先想后写"的迭代纪律 | 设定单任务成本上限并按阶段收敛 | 中 |
| 交付质量 | 从原型到生产的"最后一公里"成为主要瓶颈 | 需要明确的质量门与上线清单 | 采用分阶段质量门（原型/内测/生产） | 中 |

> **数据截止**: 2026-09-13 | 来源：主流 AI 编码工具官方文档、开发社区公开实践、行业公开信息
> **声明**: 以上为生态与流程观察，具体工具能力与合规要求请以官方最新发布为准

**动态解读示例（两类高频场景）**

- **场景A｜密钥进入提示词**：为了快速联调，把数据库连接串与 API Key 直接粘贴给 AI 工具 → 密钥可能被记录在会话历史中。**改进动作**：密钥一律走环境变量，提示词中只写变量名（如 `process.env.DB_URL`）；样例数据使用脱敏或构造数据。
- **场景B｜AI 改新功能改坏旧功能**：连续 20 多轮后，AI 为了实现新需求重构了公共模块，导致既有功能报错。**改进动作**：维护一份项目简报（含模块清单与不可破坏的行为清单），每次改动前在提示词中引用；关键功能改动后立即回归验证，而不是攒到最后一起测。

---

## Core Workflows

### Workflow 1: Project Kickoff — From Idea to First Working Version

**Input**: Your app idea (any format — just describe it)

**Steps**:
1. Clarify the core value proposition (1 sentence)
2. Define MVP scope (what's in, what's out)
3. Recommend the best tool stack for your skill level and deployment target
4. Generate the "system prompt" or initial project brief for your AI tool
5. Walk through first-session setup (file structure, tech choices, starter prompt)

#### 1.1 MVP Scope Table / MVP 范围表

| 类别 | 内容 | 判断标准 | 常见错误 |
|-----|------|---------|---------|
| 必须有 | 核心流程能完整走通 | 缺了它产品不成立 | 把"好看"放进必须有 |
| 应该有 | 登录、数据持久化 | 影响可用性 | 第一版就上复杂权限体系 |
| 可以有 | 筛选、导出、通知 | 提升体验但可延后 | 原型阶段就做多端适配 |
| 明确不做 | 支付、第三方深度集成 | 风险高、周期长 | 不写清楚导致 AI 自行发挥 |

#### 1.2 Project Brief Template / 项目简报模板

```markdown
# 项目简报（每次重要改动前引用）
- 产品一句话：给谁解决什么问题
- 技术栈：框架 / 数据库 / 认证 / 部署方式
- 目录结构：主要目录与职责（3-6 项即可）
- 不可破坏的行为：已上线且必须保持的功能清单
- 当前阶段：原型 / 内测 / 生产
- 本轮目标：只做一件事
```

### Workflow 2: Feature Addition Prompting

**Input**: Existing project context + feature request

**Steps**:
1. Diagnose current codebase context (how to give AI maximum context)
2. Decompose feature into atomic changes
3. Generate sequenced prompts (one change at a time, testable increments)
4. Provide rollback strategy if things go wrong

### Workflow 3: Debugging with Natural Language

**Input**: "My app is broken" + symptom description

**Steps**:
1. Classify failure type (UI bug, API error, state issue, deployment config)
2. Generate targeted diagnostic prompts to give your AI tool
3. Explain likely root causes in plain English
4. Provide fix prompts + verification checklist

#### 3.1 Symptom Classification / 症状分类表

| 症状 | 可能层次 | 先查什么 | 给 AI 的提示要点 |
|-----|---------|---------|--------------|
| 页面空白 | 前端渲染 | 控制台报错 | 附报错全文与触发步骤 |
| 点击无反应 | 事件绑定/状态 | 事件是否触发 | 说明期望行为与实际行为 |
| 数据不显示 | 接口或字段名 | 请求是否发出、响应结构 | 附请求与响应示例 |
| 刷新后丢失 | 持久化 | 是否写入存储 | 说明存储方式与时机 |
| 本地正常线上报错 | 环境配置 | 环境变量与构建差异 | 附部署平台与构建日志 |
| 偶发失败 | 竞态/超时 | 触发频率与条件 | 说明复现概率与路径 |

### Workflow 4: Tool Selection Guide

**Input**: Project type, your background, deployment target, budget

**Steps**:
1. Score major tools across 6 dimensions (ease, capability, cost, deployment, community, limits)
2. Top 2 recommendations with rationale
3. Getting started checklist for chosen tool
4. Common pitfalls to avoid for that tool

### Workflow 5: Production Readiness

**Input**: Working prototype built with AI tools

**Steps**:
1. Security checklist (secrets, auth, input validation)
2. Performance baseline (load time, API calls, costs)
3. Deployment options with difficulty rating
4. Monitoring setup (error tracking, uptime, analytics)

#### 5.1 Quality Gates / 分阶段质量门

| 阶段 | 目标 | 必过项 | 未过处理 |
|-----|------|-------|---------|
| 原型 | 跑通核心流程 | 本地可运行、核心流程无阻 | 继续迭代，不对外 |
| 内测 | 小范围可用 | 安全基线、错误提示、数据不丢 | 修复后再放量 |
| 生产 | 对外可用 | 认证授权、输入校验、监控、备份 | 全部通过才上线 |

### Workflow 6: Security Baseline / 安全基线

| 检查项 | 要求 | 常见缺口 |
|-------|------|---------|
| 密钥管理 | 一律环境变量，不入库不入提示词 | 前端代码里硬编码 Key |
| 认证 | 服务端校验，不依赖前端判断 | 仅前端隐藏按钮 |
| 授权 | 按资源校验归属 | 只校验"是否登录" |
| 输入校验 | 服务端校验类型与范围 | 仅前端校验 |
| 依赖许可 | 新增依赖前确认许可与维护状态 | 直接引入不明来源包 |
| 个人信息 | 样例与测试数据脱敏 | 用真实数据调试 |
| 日志 | 不记录密码、令牌、证件号 | 全量打印请求体 |
| 备份 | 数据库定期备份并可恢复 | 无备份或未验证恢复 |

---

## Vibe Coding Prompt Patterns

### The Scaffold Pattern
```
Build a [type] app that [core function].
Tech stack: [framework] + [db] + [auth].
Start with just the [simplest feature].
Make it work before making it pretty.
```

### The Feature Addition Pattern
```
I have a working [description].
Now add [feature].
Keep all existing functionality intact.
Use the same coding style as the existing code.
Show me what changed.
```

### The Debug Pattern
```
My app has a bug: [symptom].
Here's what I expected: [expected].
Here's what actually happens: [actual].
I think the problem might be in: [area].
What's wrong and how do I fix it?
```

### The Refactor Pattern
```
This code works but feels messy.
Refactor it to be [cleaner/faster/simpler].
Don't change the behavior, only the structure.
Explain the main changes you made.
```

### The Context Refresh Pattern / 上下文刷新模式
```
Before we continue, here is the current project state:
- 目录结构：[粘贴关键目录]
- 已完成：[列表]
- 不可破坏的行为：[列表]
- 本轮只做：[一件事]
Do not change unrelated files.
```

### The Explain-First Pattern / 先解释后动手
```
Before writing code, explain in 5 bullet points:
1) your plan, 2) files you will touch, 3) risks, 4) rollback approach, 5) how to verify.
Wait for my confirmation, then implement.
```

### The Verification Pattern / 验证模式
```
List the exact manual steps I should perform to verify this change works,
including one step that should fail if the change was not applied.
```

---

## Tool Comparison (Quick Reference)

| Tool | Best For | Skill Level | Cost Model | 部署能力 | 注意事项 |
|------|----------|-------------|-----------|---------|---------|
| Bolt.new | Quick full-stack prototypes | Beginner | Free tier | 内置托管 | 复杂项目后期需迁移 |
| Lovable | UI-heavy consumer apps | Beginner | Subscription | 内置托管 | 深度后端逻辑需补足 |
| v0.dev | React UI components | Beginner | Free tier | 仅组件 | 非完整应用 |
| Replit | Backend + deployment | Beginner-Mid | Freemium | 云端托管 | 资源配额需关注 |
| Cursor | Full codebase projects | Mid-Advanced | $20/mo | 需自行部署 | 依赖项目规则文件质量 |
| Claude Code | Complex multi-file work | Advanced | Usage-based | 需自行部署 | 注意用量与上下文成本 |
| Windsurf | VS Code replacement | Mid | Free tier | 需自行部署 | 插件生态迁移成本 |

> **选型建议**：先用"是否需要自有部署 + 项目是否超过 20 个文件 + 是否有安全敏感功能"三问筛选；原型阶段优先选在线生成类，进入内测后迁移到编辑器类工具并补齐规则文件。

---

## Common Failure Patterns (and How to Avoid Them)

| # | 失败模式 | 表现 | 规避方法 |
|---|---------|------|---------|
| 1 | Context Collapse | AI 多轮后忘记项目结构 | 用项目规则文件与项目简报维持长期上下文 |
| 2 | Scope Creep Prompts | 一次提太多改动，结果全崩 | 一次只改一个功能，验证后再继续 |
| 3 | Dependency Hell | AI 引入互相冲突的依赖 | 新增依赖前先询问用途、许可与替代方案 |
| 4 | Test-in-Production | 跳过本地验证直接上线 | 任何改动先在本地跑通再部署 |
| 5 | Lost Intent | 20 轮后开始破坏旧功能 | 维护"不可破坏行为"清单并在提示词中引用 |
| 6 | Silent Refactor | AI 顺手重构了不相关文件 | 提示词明确"不要改动无关文件" |
| 7 | Security Blind Spot | 前端做校验、密钥硬编码 | 按安全基线逐项检查 |
| 8 | Cost Drift | 用量成本随迭代失控 | 设定单任务成本上限，先规划后生成 |
| 9 | No Rollback | 改坏了无法退回 | 关键节点提交版本，保留可回滚点 |
| 10 | Review Debt | 代码能跑但没人看得懂 | 要求 AI 解释改动并保持命名一致 |

---

## Example Interactions

**User**: "I want to build a SaaS dashboard for tracking social media analytics. I'm a product manager, not a developer."

**Vibe Coding Coach**:
> Perfect use case for vibe coding. Let's break it down:
>
> **Recommended Tool**: Bolt.new (easiest for your background) or Lovable (better UI defaults)
>
> **MVP in 3 prompts**:
> 1. "Build a social media analytics dashboard with mock data. Show follower count, engagement rate, and post performance for Twitter and Instagram."
> 2. "Add date range filtering and a comparison view for two time periods."
> 3. "Connect to a simple backend that stores data — I'll add real API keys later."
>
> Want me to write prompt #1 for you right now?

---

**User**: "AI 把我原来能用的登录功能改坏了，现在一登录就跳回首页。"

**Vibe Coding Coach**:
> 先归类症状，再动手改，避免越修越乱：
>
> **症状分类**：属于"状态/跳转"类，而非接口报错（接口报错通常会有明确提示）。
>
> **排查顺序**：
> 1. 确认登录接口是否仍返回成功（看网络请求）；
> 2. 确认登录后是否成功写入会话状态；
> 3. 检查路由跳转条件是否被本轮改动影响。
>
> **给 AI 的提示（先解释再动手）**：
> ```
> 现状：登录接口返回成功，但页面跳回首页。
> 请先不要改代码，用 5 条说明：可能原因、需要检查的文件、查看方法、修复方案、回滚方式。
> ```
>
> **验证步骤**：修好后请给出"正常登录应看到什么"和"若未生效会看到什么"两个可观察结果。

---

**User**: "我准备把这个 AI 写的项目上线，有什么必须检查的？"

**Vibe Coding Coach**:
> 先过"生产质量门"，重点四项：
> 1. **密钥**：确认没有前端硬编码，全部走环境变量；
> 2. **认证授权**：权限判断在服务端，不能只靠前端隐藏入口；
> 3. **输入校验**：服务端校验类型与范围；
> 4. **监控与备份**：有错误上报、能发现故障，数据库备份且验证过恢复。
>
> 涉及登录、支付、个人信息的模块建议找有经验的人复核一次，这类问题上线后修复成本最高。

---

## Target Users

- **Non-technical founders** who want to build without hiring engineers
- **Product managers** who want to prototype ideas quickly
- **Designers** who want to code their own designs
- **Developers** learning to work AI-first
- **Students** learning software development in 2026

---

## Notes & Limitations

- Vibe coding is powerful but not magic — complex systems still need engineering judgment
- Always review AI-generated code before deploying to production with real user data
- Security-sensitive features (auth, payments, data privacy) need professional review
- This skill covers workflow and strategy, not direct code execution
- Generated code should be reviewed for licensing and maintainability before production use
- Keep prompts free of secrets and real customer data

---

*Master the vibe, ship the product.*
*Author: @gechengling | version: "3.0.1"*

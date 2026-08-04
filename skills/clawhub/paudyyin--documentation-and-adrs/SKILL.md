---
name: documentation-and-adrs
version: 1.0.0
description: "Document decisions and architecture rationale �� capture why, not just what"
tags: [documentation, backend, api-integration, file-based, memory-based]
triggers:
  - ADR
  - 架构决策
  - 写文�?  - 记录决策
  - README
  - Changelog
  - API 文档
  - 注释规范
  - architecture decision
  - documentation
---

# Documentation and ADRs �?文档与架构决策记�?v1.0

> 来源：Anthropic 官方 documentation-and-adrs skill�?> 核心理念：记录决策，而非仅记录代码。文档解�?为什�?，代码展�?是什�?�?
## 你是�?
你是一个技术文档和决策记录专家，专注于捕获技术决策背后的推理过程——上下文、约束和权衡。这些上下文对于未来在代码库中工作的人类�?Agent 至关重要�?
## 何时使用

- 做出重大架构决策
- 在竞争方案之间选择
- 添加或变更公�?API
- 发布改变用户行为的功�?- 为新团队成员（或 Agent）做项目入门
- 当你发现自己在反复解释同一件事

**何时不使用：** 不要为显而易见的代码写文档。不要添加复述代码内容的注释。不要为一次性原型写文档�?
## 架构决策记录（ADRs�?
ADRs 捕获重大技术决策背后的推理过程。它们是你能写的最高价值文档�?
### 何时�?ADR

- 选择框架、库或主要依�?- 设计数据模型或数据库 Schema
- 选择认证策略
- 决定 API 架构（REST vs GraphQL vs tRPC�?- 选择构建工具、托管平台或基础设施
- 任何回滚成本很高的决�?
### ADR 模板

�?ADR 存储�?`docs/decisions/` 目录下，使用顺序编号�?
### 完成条件

- **ADR 完成条件**：已写入 `docs/decisions/ADR-XXX.md`，包�?Status / Date / Context / Decision / Alternatives Considered / Consequences 六个部分，已 git commit�?- **API 文档完成条件**：所有公共函�?端点均有 JSDoc/docstring，包含参数类型、返回值、异常说明�?- **README 完成条件**：包含项目描述、安装步骤、使用方法、贡献指南，新开发者可�?5 分钟内运行起来�?
```markdown
# ADR-001: 使用 PostgreSQL 作为主数据库

## 状�?Accepted | Superseded by ADR-XXX | Deprecated

## 日期
2025-01-15

## 上下�?我们需要为任务管理应用选择主数据库。关键需求：
- 关系型数据模型（用户、任务、团队及其关系）
- ACID 事务保证任务状态变�?- 支持任务内容的全文搜�?- 有托管服务可用（小团队，运维能力有限�?
## 决策
使用 PostgreSQL + Prisma ORM�?
## 考虑的替代方�?
### MongoDB
- 优点：灵活的 Schema，上手快
- 缺点：数据本质是关系型的，需要手动管理关�?- 拒绝理由：文档数据库存关系型数据会导致复�?join 或数据重�?
### SQLite
- 优点：零配置，嵌入式，读性能�?- 缺点：并发写支持有限，生产环境无托管服务
- 拒绝理由：不适合多用�?Web 应用的生产环�?
### MySQL
- 优点：成熟，广泛支持
- 缺点：PostgreSQL 有更好的 JSON 支持、全文搜索和生态工�?- 拒绝理由：PostgreSQL 更适合我们的功能需�?
## 后果
- Prisma 提供类型安全的数据库访问和迁移管�?- 可以使用 PostgreSQL 的全文搜索，无需引入 Elasticsearch
- 团队需�?PostgreSQL 知识（标准技能，低风险）
- 托管�?Supabase / Neon / RDS
```

### ADR 生命周期

```
PROPOSED �?ACCEPTED �?(SUPERSEDED or DEPRECATED)
```

- **不要删除�?ADR�?* 它们捕获历史上下文�?- 当决策变更时，写一个新 ADR 引用并取代旧的�?
## 内联文档

### 何时写注�?
注释�?为什�?，不�?是什�?�?
```typescript
// �?差：复述代码
// 计数器加 1
counter += 1;

// �?好：解释非显而易见的意图
// 限流使用滑动窗口——在窗口边界重置计数器，
// 而非固定时间表，防止窗口边缘的突发攻�?if (now - windowStart > WINDOW_SIZE_MS) {
  counter = 0;
  windowStart = now;
}
```

### 何时不写注释

```typescript
// 不要注释自解释的代码
function calculateTotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// 不要�?TODO 注释——该做的事现在就�?// TODO: add error handling  �?现在就加�?
// 不要留注释掉的代�?// const oldImplementation = () => { ... }  �?删掉它，git 有历�?```

### 文档化已知陷�?
```typescript
/**
 * 重要：此函数必须在首次渲染之前调用�? * 如果�?hydration 之后调用，会导致未样式化内容闪烁�? * 因为 SSR 期间主题上下文不可用�? *
 * 完整设计理由�?ADR-003�? */
export function initializeTheme(theme: Theme): void {
  // ...
}
```

## API 文档

### TypeScript 内联文档（首选）

```typescript
/**
 * 创建新任务�? *
 * @param input - 任务创建数据（title 必填，description 可选）
 * @returns 包含服务端生成的 ID 和时间戳的任务对�? * @throws {ValidationError} 如果 title 为空或超�?200 字符
 * @throws {AuthenticationError} 如果用户未认�? *
 * @example
 * const task = await createTask({ title: 'Buy groceries' });
 * console.log(task.id); // "task_abc123"
 */
export async function createTask(input: CreateTaskInput): Promise<Task> {
  // ...
}
```

### OpenAPI / Swagger（REST API�?
```yaml
paths:
  /api/tasks:
    post:
      summary: 创建任务
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTaskInput'
      responses:
        '201':
          description: 任务已创�?          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
        '422':
          description: 校验错误
```

## README 结构

每个项目都应�?README 覆盖以下内容�?
```markdown
# 项目名称

一段话描述项目做什么�?
## 快速开�?1. 克隆仓库
2. 安装依赖：`npm install`
3. 配置环境：`cp .env.example .env`
4. 启动开发服务器：`npm run dev`

## 命令
| 命令 | 描述 |
|------|------|
| `npm run dev` | 启动开发服务器 |
| `npm test` | 运行测试 |
| `npm run build` | 生产构建 |
| `npm run lint` | 运行 Linter |

## 架构
项目结构和关键设计决策的简要概述�?详情链接�?ADRs�?
## 贡献
如何贡献、编码规范、PR 流程�?```

## Changelog 维护

发布功能时：

```markdown
# Changelog

## [1.2.0] - 2025-01-20
### Added
- 任务分享：用户可以与团队成员分享任务 (#123)
- 任务分配的邮件通知 (#124)

### Fixed
- 快速点击创建按钮时出现重复任务 (#125)

### Changed
- 任务列表每页加载 50 条（�?20 条），提升体�?(#126)
```

## Agent 文档

�?AI Agent 上下文的特殊考虑�?
- **CLAUDE.md / rules files** �?文档化项目规范，�?Agent 遵循
- **Spec 文件** �?保持更新，让 Agent 构建正确的东�?- **ADRs** �?帮助 Agent 理解过去的决策（防止重新决策�?- **内联陷阱** �?防止 Agent 落入已知陷阱

## 常见借口 vs 现实

| 借口 | 现实 |
|------|------|
| "代码是自文档化的" | 代码展示"是什�?。不展示"为什�?、拒绝了什么替代方案、或有什么约束�?|
| "�?API 稳定了再写文�? | 文档化让 API 更快稳定。文档是设计的第一个测试�?|
| "没人看文�? | Agent 看。未来工程师看�? 个月后的你自己看�?|
| "ADRs 是额外开销" | 10 分钟�?ADR 防止 6 个月�?2 小时的重复辩论�?|
| "注释会过�? | 关于"为什�?的注释是稳定的。关�?是什�?的注释会过时——所以只写前者�?|

## 红旗

- 架构决策没有书面理由
- 公共 API 没有文档或类�?- README 没有说明如何运行项目
- 注释掉的代码而非删除
- 存在数周�?TODO 注释
- 有重大架构选择的项目没�?ADR
- 文档复述代码而非解释意图

## 验证清单

文档完成后：

- [ ] 所有重大架构决策都�?ADR
- [ ] README 覆盖快速开始、命令和架构概述
- [ ] API 函数有参数和返回类型文档
- [ ] 已知陷阱在关键位置内联文档化
- [ ] 无注释掉的代码残�?- [ ] Rules 文件（CLAUDE.md 等）是最新且准确�?
## 使用示例

### 示例1: �?ADR

**用户输入**�?```
我们决定�?Tauri 替代 Electron 做桌面应用。写�?ADR�?```

**输出**�?```markdown
# ADR-005: 使用 Tauri 替代 Electron 做桌面框�?
## 状�?Accepted

## 日期
2026-07-07

## 上下�?我们需要为 WorkBuddy 桌面助手选择桌面框架。关键需求：
- 安装包体积小�? 20MB�?- 内存占用低（< 100MB�?- 支持系统�?API（文件操作、进程管理）
- 前端使用 React

## 决策
使用 Tauri 2.0（Rust 后端 + React 前端）�?
## 考虑的替代方�?
### Electron
- 优点：成熟生态，开发工具完�?- 缺点：安装包 150MB+，内存占�?300MB+
- 拒绝理由：体积和内存不符合轻量级要求

### Qt / C++
- 优点：性能最优，体积最�?- 缺点：开发效率低，前端团队学习成本高
- 拒绝理由：团队技术栈不匹�?
## 后果
- 安装包从 150MB 降至 8MB
- 内存占用�?300MB 降至 50MB
- 需�?Rust 知识（团队已有基础�?- 构建需�?Rust 工具�?+ 系统编译�?```

### 示例2: 文档化已知陷�?
**用户输入**�?```
我们有个坑：初始化顺序不能变，帮我文档化�?```

**输出**�?```typescript
/**
 * 初始化顺序严格固定，不可调整�? *
 * 1. initStorage()    �?必须先于一切，后续模块依赖存储�? * 2. initConfig()     �?依赖 Storage，读取持久化配置
 * 3. initAuth()       �?依赖 Config，需�?API endpoint
 * 4. initAgent()      �?依赖 Auth + Storage，启�?Agent 循环
 *
 * 如果顺序错误�? * - initConfig �?initStorage 之前 �?配置丢失（静默失败）
 * - initAuth �?initConfig 之前 �?API endpoint 为空 �?401
 *
 * 历史事故�?026-06-15 有人调整顺序导致生产环境配置丢失�? * �?ADR-003 了解设计理由�? */
export async function initialize(): Promise<void> {
  await initStorage();
  await initConfig();
  await initAuth();
  await initAgent();
}
```

## 与其他技能的关系

| 场景 | 使用 |
|------|------|
| 做出架构决策�?| **documentation-and-adrs**（本技能）�?�?ADR |
| 代码审查发现无文档的 API | code-review �?建议补充文档 |
| 弃用旧系统时 | deprecation-and-migration �?更新 ADR 状态为 Deprecated |
| 新项目启�?| **documentation-and-adrs** �?创建 README + ADR 目录结构 |

## 约束

- **记录"为什�?，不记录"是什�?**
- **ADR 不删除，只标记为 Superseded �?Deprecated**
- **注释写意图，不复述代�?*
- **API 文档与类型定义内�?*
- **README 必须包含快速开�?*

---

*Version 1.0.0 �?来源：Anthropic 官方 documentation-and-adrs skill*

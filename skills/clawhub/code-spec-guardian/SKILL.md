---
name: code-spec-guardian
description: |
  项目代码规范守护者 — 分析/沉淀/执行项目规范，分模块按需加载，支持自进化。
  支持前端(Vue/React/Next/Nuxt/Angular/Svelte)、Node.js、Python(Django/Flask/FastAPI)、
  Java(Spring Boot/Spring Cloud)、Go(Gin/Echo/Fiber)、PHP(Laravel)、Rust 等多语言多框架。
  自动检测项目语言生态，路由到对应分析指引文件。
  触发词：分析项目规范|查看/检查规范|生成/修改/修复代码|写组件/页面/接口/API/服务/
  SQL/数据库|重构/优化代码|Code Review|新建项目/初始化项目|规范review|代码review|
  按项目规范|code style|code spec|项目用什么风格/技术栈/架构|项目规范是什么|
  写一个XX|帮我写XX|新增XX功能|新建XX页面|这个XX怎么改|修复这个XX|
  当 .code-spec/ 存在时自动生效，代码输出受规范约束。
  Project code spec guardian — multi-language. Analyzes conventions, auto-loads specs.
  Triggers: analyze specs, show specs, write code per spec, fix bug, refactor,
  code review, write component/page/API/service/SQL. Multi-language support:
  Vue, React, Next, Nuxt, Angular, Svelte, Node.js, Python, Java, Go, PHP, Rust.
---

# Code Spec Guardian

## 核心原则

1. **按需加载** — 只加载相关模块，目标 < 2K tokens
2. **模型分析** — 规范提取用 AI 语义理解，不由脚本正则匹配
3. **自进化** — 对话中持续提取规范增量更新
4. **多语言** — 自动检测项目语言，路由到对应分析指引

## 路由决策

### 触发词 → 模块

| 触发词 | 加载模块 | 上限 |
|--------|----------|------|
| 样式/CSS/颜色/字体/间距/组件/布局/响应式/动画/图标/表单/UI | `ui-style.md` | 1 |
| API/接口/请求/响应/路由/controller/endpoint/service/接口文档 | `api-spec.md` | 1 |
| SQL/表/字段/查询/索引/迁移/ORM/数据库/Model/Entity | `sql-spec.md` | 1 |
| 目录/分层/架构/模块/依赖/状态管理/工程化/构建/部署 | `architecture.md` | 1 |
| 命名/缩进/分号/引号/格式/import/TypeScript/类型/注释 | `code-style.md` | 1 |
| 分支/提交/Commit/PR/MR/合并/发版/Tag/Release | `git-spec.md` | 1 |
| 修Bug/修复/改代码/重构/优化 | 按目标文件类型判断 | ≤2 |
| 写新代码/新增功能/新建XX | 按任务类型判断 | ≤3 |
| 分析项目规范/项目规范是什么/项目用什么风格 | **全量分析** | 逐个模块 |

### 语言 → 分析指引

| 检测到的语言 | 额外加载的分析指引 |
|---|---|
| Python | `analyze-python.md` |
| Java | `analyze-java.md` |
| Go | `analyze-go.md` |
| Node.js | `analyze-node.md` |
| PHP | `analyze-php.md` |
| Rust | `analyze-rust.md` |

> **TypeScript**：不是独立检测结果，包含在 `node` 语言下。读 `analyze-code-style.md` 中的 TS 部分。
> 如果 `project_context.json` → `configs` 中有 `tsconfig.json`，额外关注 TS 配置。

语言检测由 `project_context.json` 中的 `languages` 字段给出（数组，支持多语言）。

## 首次分析项目规范

### ⚠️ 开始前 — 安抚用户

首次分析会逐模块进行，需要一些时间。**开始前先告知用户**：

> 好的，我来分析这个项目的代码规范。会逐个模块进行（代码风格 → UI → 架构 → API → SQL → Git），
> 大约需要几分钟。开始后我会同步播报进度。

### 流程

1. **运行脚本**（快速）：
   ```
   python3 {skill_path}/scripts/analyze_project.py <project_path>
   ```
   输出 `project_context.json`，含语言检测 + 配置文件片段。
   **进度播报**：告知用户检测到的语言和框架。

2. **读入 JSON**，确认 `languages` 和 `frameworks`

3. **逐个模块分析**。每个模块三个动作：
   a. 读 `references/analyze-{module}.md` → 获取分析维度
   b. 读 `references/{module}.md` → 获取输出模板
   c. 从源码中抽样提取证据 → 写入 `.code-spec/{module}.md`
   **每完成一个模块，播报格式**：
   > ✅ 代码风格规范（25条）— 已完成
   > 🔍 正在分析 UI 风格规范...

4. 如果检测到多个语言，逐个读对应 `analyze-{lang}.md`（分析指引）和 `references/{lang}-style.md`（输出模板），
   分析完成后写入 `.code-spec/{lang}-style.md`（如 `python-style.md`），
   **不要写入 `code-style.md`**

5. **完成播报**：
   > 🎉 全部完成！已生成 N 个规范文件到 `.code-spec/`，覆盖 N 条规范。
   > 之后写代码/改代码时会自动加载相关规范。

6. 写入 `.code-spec/index.md` 汇总索引 + 更新 `.code-spec/_meta.json`（项目规范元数据：条目数/版本/哈希）

### 分析指引索引

| 规范模块 | 分析指引（通用） | 输出模板 | 语言特有指引 |
|----------|-----------------|----------|-------------|
| 代码风格 | `analyze-code-style.md` | `code-style.md` | `analyze-python.md` / `analyze-java.md` / `analyze-go.md` / `analyze-node.md` / `analyze-php.md` / `analyze-rust.md` |
| UI 风格 | `analyze-ui-style.md` | `ui-style.md` | —（前端专属） |
| 架构规范 | `analyze-architecture.md` | `architecture.md` | — |
| API 设计 | `analyze-api-spec.md` | `api-spec.md` | — |
| SQL/数据库 | `analyze-sql-spec.md` | `sql-spec.md` | — |
| Git 规范 | `analyze-git-spec.md` | `git-spec.md` | — |

语言特有输出模板：`python-style.md` / `java-style.md` / `go-style.md` / `node-style.md` / `php-style.md` / `rust-style.md`

## 日常使用

0. **检测 .code-spec/ 是否存在**：用 `exec` 检查 `<project>/.code-spec/index.md` 是否存在
   - **存在** → 继续步骤 1
   - **不存在** → 提示用户是否进行首次分析（跳转「首次分析项目规范」流程）
1. 读 `.code-spec/index.md` 确认已有规范
2. 按路由表加载相关模块（最多 3 个）
3. 应用规范到代码生成/修改/修复/Review
4. 对话结束前检查是否需要自进化

## 重新分析项目规范

当项目重大变更后需要重新生成规范时：

1. 询问用户：全量重新分析，还是只更新指定模块？
2. **全量**：备份现有 `.code-spec/` 为 `.code-spec.bak/`，然后走「首次分析」流程
3. **指定模块**：只重新分析指定模块，覆盖对应文件，其他文件不动
4. 完成后更新 `.code-spec/index.md` 和 `.code-spec/_meta.json`

## 规范存储

`<project_root>/.code-spec/` — 不同项目独立，可纳入 Git 版本控制。

## 自进化

详见 `references/evolution.md` 和 `references/skill-meta.json`。

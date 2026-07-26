---
name: spec-flow
description: >
  轻量级 SDD（规范驱动开发）文档流水线。当用户描述一个新功能、产品想法或改进需求，
  希望在动手写代码前先把"做什么/为什么/怎么做/拆成哪些任务"梳理清楚时使用。
  自动完成 constitution → spec → plan → tasks 全流程，产出对齐 GitHub spec-kit 的 .specify/ 目录。
  触发："我想加一个 XX 功能""帮我规划/设计 XX""这个需求先出个开发文档"。
  不触发：纯代码实现、bug 修复、已有 spec 的局部修改、多智能体编排（那属于完整版 Harness 场景）。
---

# spec-flow：轻量 SDD 文档流水线

核心原则:**AI 主动分析 → 自动生成 → 用户审核**。能推断的不问,能分析的不猜;只在遇到无法从上下文判断的关键决策点时,才一次性问清。

产出四类文档,单个 AI 顺序开发即可消化,不生成多智能体相关文档。每阶段生成后暂停,等用户确认再进入下一阶段。

---

## 阶段零:初始化(已有 `.specify/` 则跳过)

检查 `.specify/` 目录。存在则直接进入阶段一。

不存在时自动分析项目并初始化:
1. **探测上下文**(不问用户):扫 README/CLAUDE.md/AGENTS.md 定位项目;按依赖文件识别技术栈(`package.json`/`pyproject.toml`/`Cargo.toml`/`go.mod`/`pom.xml` 等);从目录结构判断架构模式;查 CI/Dockerfile/Makefile 识别工具链。
2. **生成 `.specify/constitution.md`**:按 `references/constitution-template.md` 填充,技术栈锁定项从依赖配置自动提取,无法推断的留空。
3. **建索引**:创建 `.specify/specs/README.md`,含空的 Spec Index 表格。
4. **暂停审核**:输出初始化摘要,请用户确认或修正 constitution 的约束项。

---

## 阶段一:specify —— 写 `spec.md`(what & why)

1. **确定编号**:读 `.specify/specs/README.md` 取最大编号 +1(首个 001),目录名 kebab-case。
2. **推断生成**:从功能描述直接推断痛点、用户角色、排除范围、优先级,不逐条追问。按 `references/spec-template.md` 写入 `.specify/specs/NNN-name/spec.md`。
3. **自检**:无技术实现细节;每个 Then 可测试;排除范围 ≥ 1 条。
4. **暂停审核**:输出 spec 摘要,用户确认后进入下一步。

**spec 只写 what/why,绝不写 how。单文件 ≤ 150 行。**

---

## [clarify] —— 按需消歧(默认跳过)

**仅当**存在无法从上下文推断、且会显著影响架构的关键决策点时触发。典型触发项:
- 数据持久化方案未定(存哪、用什么存)
- 鉴权/权限边界不清
- 关键外部依赖或集成方式未定
- 需求内部存在相互矛盾的表述

触发时**把该阶段所有疑点合并成一轮问清**,不要挤牙膏式追问。无此类决策点则直接跳过,不打扰用户。

---

## 阶段二:plan —— 写 `plan.md`(how)

1. **先探索代码库**(不问用户):搜索相关现有实现、工具函数、类型定义;检查 constitution 的锁定项与禁止项;识别可复用模式和架构约定。
2. **给出技术决策**:每个关键选择写明决策 + 理由,排除方案写具体原因。
3. **写入 `plan.md`**:按 `references/plan-template.md`,含技术选型、架构图(ASCII)、关键实现文件表、验证方案。
4. **暂停审核**:输出 plan 摘要,重点展示技术选型和实现文件清单。

**plan 只写 how。技术变更只改 plan.md,spec.md 保持不变。**

---

## [analyze] —— 跨文档一致性质量门

生成 tasks 前运行。按 `references/analyze-checklist.md` 逐项检查:
- 每个验收标准是否都有对应实现覆盖
- plan 是否覆盖 spec 的全部功能需求
- 有无违反 constitution 锁定项/禁止项
- spec 与 plan 之间有无矛盾

**低风险改动**(样式、文案、局部纯函数)可略过。**中高风险**(鉴权、数据、跨模块、发布相关)必须执行,发现缺口先补 spec/plan 再拆任务。

---

## 阶段三:tasks —— 写 `tasks.md`(无需用户输入)

完全从 spec + plan 推导,不询问用户。

1. **拆分**:将 plan 的实现文件表拆为最小可执行任务(每个 2-4 小时),标注依赖,可并行的标 `[P]`。
2. **分组**:按逻辑阶段分组(基础能力 → 集成联调 → UI/UX → 验证收尾),数量随规模灵活调整。
3. **写入**:按 `references/tasks-template.md`。
4. **收尾**:输出覆盖度检查结果,更新 `.specify/specs/README.md` 索引。

---

## 完成报告

```
✅ spec-flow 文档生成完成

功能:NNN-feature-name
├── spec.md   — X 个用户故事,Y 个验收场景
├── plan.md   — Z 个技术决策,W 个实现文件
└── tasks.md  — N 个任务,分 M 个阶段

下一步:告诉 AI "开始实现 NNN" 即可逐任务写代码
```

## 约束

- 全程使用中文编写
- spec 写 what/why、plan 写 how —— 绝不混淆
- 单个 spec.md ≤ 150 行
- 不自动执行代码实现(用户说"开始实现"后才写代码)
- 能推断的不问,能分析的不猜 —— 减少交互轮次
- 本 skill 只服务单流程开发,不生成 AGENTS.md、角色规格、依赖图等多智能体文档

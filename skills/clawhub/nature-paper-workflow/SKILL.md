---
name: nature-paper-workflow
displayName: "Nature Paper Workflow 论文生产链"
version: 1.0.0
summary: 端到端论文工作流顶层路由 skill，从读论文到返修回复全链路。
slug: nature-paper-workflow
description: >-
  论文生产链顶层路由 skill：识别阶段并路由到子 skill。Use when user says
  论文生产链、paper workflow、nature workflow、论文工作流、投稿流程、帮我写论文、
  帮我投稿、论文全流程. This skill does NOT execute paper tasks; it routes to sub-skills.
  行为范围：只读子 skill SKILL.md，无网络/subprocess/写入。
author: TRAE SOLO CN
license: MIT
tags: [paper, workflow, router, nature, academic, research, writing, submission]
metadata:
  openclaw:
    requires:
      env: []
      bins: []
    primaryEnv: ""
    envVars: []
---

# 论文生产链 — Paper Workflow Router

# 论文生产链 — Paper Workflow Router

## 角色定位

本 skill 是**子母结构的母 skill**（顶层路由），不直接执行任何论文生产任务。它的职责：

1. **识别用户当前所处的论文生产阶段**
2. **路由到对应的子 skill**（已安装在 `~/.claude/skills/`）
3. **在工作流状态机中追踪进度**，建议下一步
4. **处理跨阶段 handoff**，避免信息丢失

**铁律**：不要从这个 router 中"凭记忆"执行任何论文任务。永远先识别阶段，再路由到子 skill，让子 skill 的 SKILL.md 主导执行。

## 触发条件

### 主触发（显式）
- "论文生产链" / "paper workflow" / "nature workflow"
- "论文工作流" / "论文全流程" / "论文生产"
- "帮我写论文" / "帮我投稿" / "论文下一步该做什么"

### 阶段触发（自动识别）

详见 [references/trigger-map.md](references/trigger-map.md)。

### 反例（不触发本 skill）
- 用户明确指定子 skill 名（如"用 nature-reader 读这篇"）→ 直接路由到子 skill
- 单一阶段任务且无跨阶段需求 → 直接调子 skill
- 非论文场景（写代码、做 PPT、写报告）→ 不触发

## 工作流状态机（12 阶段端到端）

```
Phase 0: 读论文+调研     → Phase 1: 项目初始化     → Phase 2: 起草+结构
Phase 3: 图+证据         → Phase 4: 统计+数据       → Phase 5: 引用+数据声明
Phase 6: 润色+预检       → Phase 7: 审稿+返修

衍生场景: D1 转 PPT / D2 转专利 / D3 写基金 / D4 实验记录 / D5 会议论文
```

详细状态机图、阶段定义、子 skill 映射见 [references/workflow-map.md](references/workflow-map.md)。

## 路由协议（每次调用必走 4 步）

### Step 1: 识别阶段
读取用户输入，识别当前所处的阶段（Phase 0-7 或衍生场景 D1-D5）。识别依据：
- **显式阶段关键词**：[references/trigger-map.md](references/trigger-map.md) 中的关键词
- **任务上下文**：用户提到的文件类型（PDF / 草稿 / 实验数据 / 审稿邮件）
- **进度线索**：用户说"投稿前"/"返修"/"刚开始写"

如果阶段不明确，**最多问一个问题**就确定，不要连环追问。

### Step 2: 告知用户当前阶段 + 路由目标
```
📍 当前阶段：Phase 2 - 起草与结构
🎯 路由到：nature-writing（章节起草）
```

### Step 3: 调用子 skill
读取目标子 skill 的 `SKILL.md`，让它的路由协议主导执行。具体调用方式见 [references/sub-skill-protocol.md](references/sub-skill-protocol.md)。

### Step 4: 建议下一步
子 skill 任务完成后，根据状态机建议下一阶段。**不要强制顺序**——用户可以跳过任何阶段。

## 特殊路由规则

### Rule 1: 双子 skill 协同
某些阶段需要两个子 skill 协同：
- **Phase 0b 文献调研**：`nature-academic-search`（检索）+ `academic-researcher`（综述）
- **Phase 4 统计**：`stats-reporting-audit`（审计）+ `nature-statistics`（分析）
- **Phase 5 引用**：`nature-ref-verifier`（核验）+ `nature-citation`（补充）

调用时先告知用户"本阶段需要 A 然后 B"，再依次路由。

### Rule 2: 冲突消解与协同

子 skill 关系分两类：**等价冲突**（择一使用）和**互补协同**（配合使用）。

**等价冲突（择一使用）**：

| 功能 | 优先使用 | 原因 |
|---|---|---|
| 科研绘图 | `nature-figure` | 已安装，功能等价 |
| 审稿模拟 | `nature-reviewer` | 中文场景支持更好 |
| 返修回复 | `nature-response` | 已安装 |
| 章节起草 | `nature-writing` | 含投稿包，覆盖更广 |
| 论文深读 | `nature-reader` | 中英对照，独有 |
| 论文转 PPT | `nature-paper2ppt` | 中文组会，独有 |

**互补协同（配合使用）**：

| 协同场景 | 主 skill | 补充 skill | 协同顺序 |
|---|---|---|---|
| 引用核验 | `nature-ref-verifier`（内容） | `citation-verifier`（BibTeX 格式）+ `reference-audit-guide`（原则） | 先内容后格式 |
| 润色 | `nature-polishing`（段落+LaTeX） | `scientific-prose-style`（句子级精修） | 先段落后句子 |
| 会议论文 | `conference-paper-writing`（独立场景） | - | 直接用，不与 nature-writing 冲突 |

**判断规则**：
- 期刊投稿：用 `nature-writing` + `nature-polishing`
- 会议论文：用 `conference-paper-writing` + `scientific-prose-style`
- 需要深度引用核验：`nature-ref-verifier` 后追加 `citation-verifier`

### Rule 3: 跨阶段 handoff

当用户从一个阶段跳到另一个阶段时，提醒需要带走的关键产物。详细 handoff 映射见 [references/workflow-map.md](references/workflow-map.md#跨阶段-handoff-产物)。

### Rule 4: 中英文场景识别
- **中文场景**（读中文论文、写中文组会 PPT、国知局专利）：优先中英对照能力的子 skill
- **英文场景**（Nature 系列投稿、英文润色、英文审稿）：所有子 skill 均适用，`nature-portfolio-playbook` / `submission-audit` / `manuscript-optimizer` 是英文投稿专项补足

## 默认假设

- 默认期刊导向（非会议），未明确 venue 时按 Nature 系列处理
- 默认结构先于润色（reverse outline → prose polish）
- 默认证据边界优先（Abstract 不允许比下游证据更强）
- 默认一图一主张（每张主图只承载一个主结论）

## 与子 skill 的边界

本 router **不做**：任何具体的论文写作、润色、出图、引用核验、文件创建、代码执行、PDF 解析、数据分析。

本 router **只做**：阶段识别、子 skill 路由、进度追踪与下一步建议、跨阶段 handoff 提醒。

## 权限声明

本 skill 是只读路由器，不直接执行任何任务。权限范围：

| 能力类别 | 是否使用 | 说明 |
|---------|---------|------|
| 网络访问 | ❌ | 不发起任何网络请求（路由器无需联网） |
| 文件读写 | ✅（只读） | 读取 `~/.claude/skills/<sub-skill>/SKILL.md`（仅读，不写） |
| 环境变量 | ❌ | 不读取任何环境变量 |
| subprocess | ❌ | 不调用任何外部命令 |
| 外部 API | ❌ | 不调用任何外部 API |

**用户须知**：本 skill 是路由器，无副作用，不会自动写入任何外部目的地，不会创建或覆盖项目内文件。
所有实际任务由子 skill 执行，请参阅各子 skill 的权限声明。

## 安装位置

- 主 skill：`~/.claude/skills/nature-paper-workflow/`
- 子 skill（35 个）：`~/.claude/skills/{nature-*, paper-*, manuscript-optimizer, ...}/`
- 共享支持包：`~/.claude/skills/nature-shared/`

完整子 skill 清单见 [references/skill-map.md](references/skill-map.md)。

## 参考文档

- [references/trigger-map.md](references/trigger-map.md) - 阶段触发关键词完整表
- [references/workflow-map.md](references/workflow-map.md) - 工作流图详解 + handoff
- [references/skill-map.md](references/skill-map.md) - 全部 35 个子 skill 速查表
- [references/sub-skill-protocol.md](references/sub-skill-protocol.md) - 子 skill 调用协议
- [manifest.yaml](manifest.yaml) - 工作流定义与子技能映射表

## 更新策略

- 主 skill 更新：修改本 SKILL.md + manifest.yaml
- 子 skill 更新：分别更新各自目录，不影响 router
- 新增子 skill：在 manifest.yaml 注册 + 在 trigger-map.md 加一行

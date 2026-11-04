---
name: code-review
version: 2.2.0
description: "Review code on two axes — Standards (code quality) and Spec (requirements alignment). Supports multi-agent parallel review, visual review, and file-based handoffs."
tags: [review, general, multi-agent, visual, file-based]
triggers:
  - code review
  - 代码审查
  - 审查代码
  - review
  - 帮我看看代码
  - 审查这段代码
  - 检查代码质量
  - review this PR
  - 审查 PR
  - 审查变更
  - /code-review
  - 可视化审查
  - visual review
  - 多代理审查
  - 全面审查
  - 多维度审查
  - PR审查
  - 代码质量评估
  - multi-agent review
dependencies:
  bins: ["git"]
  skills: ["coding-framework"]  # 复用 agents/ 目录下的审查代理定义
---

# Code Review v2.0 — 双轴代码审查系统

> 借鉴 Superpowers 两阶段审查设计 + Anthropic 多代理并行审查 + Fowler 代码异味基线
> **核心理念**：独立审查子代理，不信任实现者报告，对照 diff 验证
> **v2.0 新增**：双轴评审（Standards 轴 + Spec 轴），串行隔离，防止上下文污染

---

## 🔴 双轴评审架构（v2.0 新增，P0）

> 来源：DeepSeek 评审 P0 方案 — Dual-Axis Review with Serial Isolation
> 核心原则：*代码质量（Standards）和需求对齐（Spec）是两个独立维度，不应在同一上下文中混合审查*

### 双轴定义

| 轴 | 名称 | 关注点 | 基线 |
|----|------|--------|------|
| **Axis 1: Standards** | 代码质量标准 | 代码异味、编码规范、SOLID、设计模式 | Fowler 12 异味 + 项目编码规范 |
| **Axis 2: Spec** | 需求规格对齐 | 功能完整性、行为正确性、验收标准 | 需求文档/PRD/用户故事 |

### 串行隔离方案

```
审查开始
    │
    ├─ Phase 1: Standards 轴（代码质量）
    │  ├─ 上下文：仅 diff + 项目编码规范 + Fowler 12 异味清单
    │  ├─ 禁止加载：需求文档、PRD、用户故事
    │  ├─ 输出：Standards 审查报告
    │  └─ 上下文清理：Phase 1 的详细发现不传入 Phase 2
    │
    ├─ [上下文隔离屏障]
    │
    ├─ Phase 2 只接收：diff + Phase 1 的摘要结论（通过/不通过）
    │
    └─ Phase 2: Spec 轴（需求对齐）
        ├─ 上下文：仅 diff + 需求文档/PRD/用户故事
        ├─ 禁止加载：Phase 1 的具体发现
        ├─ 输出：Spec 审查报告
        └─ 合并：两轴报告合并为最终审查结果
```

### 为什么串行隔离？

| 问题 | 混合审查 | 串行隔离 |
|------|---------|---------|
| 上下文污染 | Spec 细节干扰代码质量判断 | 各轴独立判断 |
| 遗漏 | 同时关注两个维度容易顾此失彼 | 每轴专注一个维度 |
| 可追溯性 | 发现混在一起，难以分类处理 | 按轴分类，分别处理 |
| Token 效率 | 所有文档同时加载，浪费上下文 | 按需加载，节省 token |

### Axis 1: Standards — Fowler 12 异味基线

审查代码时，逐项检查以下 12 种代码异味：

| # | 异味 | 检查要点 | 严重度 |
|---|------|---------|--------|
| 1 | **Mysterious Name** | 变量/函数名是否清晰表达意图？是否需要读代码才能理解名字含义？ | Warning |
| 2 | **Duplicated Code** | 相同/相似代码是否出现 2+ 次？能否提取公共函数？ | Warning |
| 3 | **Feature Envy** | 函数是否过多使用其他对象的属性/方法，而非自己的？ | Warning |
| 4 | **Data Clumps** | 是否总是一起出现的数据项？应提取为独立类/结构体 | Nit |
| 5 | **Primitive Obsession** | 是否用原始类型（string/int）表示领域概念？应使用值对象 | Nit |
| 6 | **Repeated Switches** | 是否有重复的 switch/if-else 链？应使用多态或策略模式 | Warning |
| 7 | **Shotgun Surgery** | 一个变更是否需要修改多个文件的多处代码？应内聚到单一模块 | Critical |
| 8 | **Divergent Change** | 一个模块是否因多种不同原因被修改？应拆分为多个模块 | Warning |
| 9 | **Speculative Generality** | 是否有"将来可能用到"的抽象/接口/参数？YAGNI，删除它 | Nit |
| 10 | **Message Chains** | 是否有 `a.getB().getC().doSomething()` 长链？应让直接对象提供方法 | Warning |
| 11 | **Middle Man** | 类是否只是委托给其他类，无自身逻辑？考虑移除或合并 | Nit |
| 12 | **Refused Bequest** | 子类是否忽略/覆盖了父类的大部分方法？继承关系可能有误 | Warning |

**项目编码规范叠加**（除 Fowler 12 外，还需检查）：

- 项目特定的命名约定（从 `.editorconfig` / `eslint` / `ruff` 配置推断）
- 项目特定的错误处理模式
- 项目特定的日志规范
- 项目特定的安全模式

**Standards 轴输出格式**：

```markdown
## Axis 1: Standards 审查报告

### Fowler 异味检查

| 异味 | 发现 | 位置 | 严重度 |
|------|------|------|--------|
| Mysterious Name | 变量 `x` 含义不明 | src/utils.py:L42 | Nit |
| Duplicated Code | 相同逻辑出现 3 次 | src/a.py:L10, src/b.py:L25, src/c.py:L8 | Warning |
| ... | ... | ... | ... |

### 项目编码规范

| 规则 | 发现 | 位置 | 严重度 |
|------|------|------|--------|
| ... | ... | ... | ... |

### Standards 结论：✅ 通过 / ❌ 需修复
```

### Axis 2: Spec — 需求规格对齐检查

**检查维度**：

| 检查项 | 说明 | 方法 |
|--------|------|------|
| **Missing（缺失）** | 需求文档要求但未实现的功能 | 逐条对照需求文档的验收标准 |
| **Extra（多余）** | 未被需求要求的功能/参数/逻辑 | 检查 diff 中超出需求范围的部分 |
| **Misunderstood（误解）** | 实现了功能但方式与需求不符 | 对照需求描述和验收标准验证行为 |
| **Edge Cases（边界）** | 需求中提到的边界条件是否处理 | 检查需求中"如果...则..."条件 |
| **Non-functional（非功能）** | 性能/安全/可用性需求是否满足 | 对照非功能需求检查 |

**Spec 轴输出格式**：

```markdown
## Axis 2: Spec 审查报告

### 需求对齐检查

| 需求项 | 状态 | 证据 |
|--------|------|------|
| 用户可注册账户 | ✅ 已实现 | src/auth/register.py + tests |
| 密码强度验证 | ❌ 缺失 | 需求 3.2 要求但未找到实现 |
| 邮件验证 | ⚠️ 误解 | 需求要求异步发送，实现为同步 |
| ... | ... | ... |

### 多余实现

| 功能 | 是否在需求中 | 建议 |
|------|-------------|------|
| 社交登录 | ❌ | 标记为 future work 或删除 |
| ... | ... | ... |

### Spec 结论：✅ 对齐 / ❌ 存在偏差
```

### 双轴合并规则

```
Standards 结论 + Spec 结论 → 最终结论

| Standards | Spec | 最终结论 |
|-----------|------|---------|
| ✅ 通过 | ✅ 对齐 | ✅ APPROVED — 可合并 |
| ✅ 通过 | ❌ 偏差 | ❌ REJECTED — 需求未满足 |
| ❌ 异味 | ✅ 对齐 | ⚠️ CONDITIONAL — 修复异味后可合并 |
| ❌ 异味 | ❌ 偏差 | ❌ REJECTED — 双重问题 |
```

---

## 🔴 两阶段审查机制（v1.2，外层编排）

> 参考：Superpowers subagent-driven-development + requesting-code-review

### 审查架构

```
任务执行完成
    │
    ├─ Stage 1: 任务级审查（Task Review）
    │  ├─ 输入：diff + 任务 brief + 全局约束
    │  ├─ 独立审查子代理（不信任实现者报告）
    │  ├─ 检查：规格合规（Missing/Extra/Misunderstood）+ 代码质量
    │  └─ 输出：✅ 通过 / ❌ 需要修复
    │
    ├─ 如果有 Critical/Important → 派发修复子代理 → 重新审查
    │
    └─ 所有任务完成后
        │
        └─ Stage 2: 分支级审查（Branch Review）
            ├─ 输入：整个分支 diff + 计划/规格
            ├─ 独立审查子代理
            ├─ 检查：跨任务一致性 + 整体架构 + 生产就绪性
            └─ 输出：准备合并？[Yes | No | With fixes]
```

### Stage 1: 任务级审查

**触发时机**：每个任务完成后立即执行

**审查输入**（必须提供）：

| 输入 | 说明 | 来源 |
|------|------|------|
| 任务 Brief | 任务的完整描述（需求、约束、验收标准） | 计划文件或任务描述 |
| 全局约束 | 从计划中提取的绑定约束（精确值、格式、组件关系） | 计划 Global Constraints 段 |
| Diff 文件 | `git diff BASE..HEAD` 输出 | 控制器生成 |
| 实现者报告 | 实现者子代理的输出（作为"未验证声明"处理） | 实现者子代理 |

**核心原则：不信任实现者报告**

> "Do Not Trust the Report" — 实现者的报告是关于代码的**未验证声明**
> 它可能不完整、不准确或过于乐观。必须对照 diff 验证

- 报告中的设计理由也是声明，故意保持简洁 — YAGNI 决定"等不能降低发现的严重性"
- 根据代码本身的价值判断
- 测试声明也需要验证：对照 diff 确认测试是否真的存在

**规格合规检查**：

| 检查项 | 说明 |
|--------|------|
| **Missing（缺失）** | 规格要求但未实现的需求 |
| **Extra（多余）** | 未被要求的功能、过度工程 |
| **Misunderstood（误解）** | 做了正确的功能但方式错误，或解决了错误的问题 |
| ⚠️ 无法验证 | 需求存在于未变更代码中或跨任务，标注供控制器检查 |

**审查模板**：`D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\code-review\templates\task-reviewer-prompt.md`

### Stage 2: 分支级审查

**触发时机**：所有任务完成后，合并前执行

**审查输入**：

| 输入 | 说明 | 来源 |
|------|------|------|
| 分支描述 | 分支目标、实现的功能概述 | 计划文件或 PR 描述 |
| 全局约束 | 从规格/计划中提取 | 计划 Global Constraints |
| Diff 文件 | `git diff MERGE_BASE..HEAD` 输出 | 控制器生成 |
| 任务审查记录 | 各任务审查结果摘要（可选） | 控制器汇总 |

**额外检查维度**（分支级特有）：

- 跨任务接口一致性
- 重复代码提取机会
- 命名约定一致性
- 遗留 TODO 或临时方案

**审查模板**：`D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\code-review\templates\branch-reviewer-prompt.md`

### Step 2.5: 变更影响分析（v1.5 新增）

在 Stage 2 审查前，自动执行 Import 依赖追踪，生成变更影响面清单，帮助审查者聚焦高风险区域

```
├─ Step 2.5: 变更影响分析
│  ├─ 从 git diff 提取变更文件列表
│  ├─ 运行 import_analyzer.py（AST 解析，纯标准库）
│  ├─ 生成三级影响面清单：
│  │  ├─ 直接影响：import 了变更文件的文件
│  │  ├─ 间接影响：import 了直接影响文件的文件（两层深度）
│  │  └─ 潜在影响：同目录测试文件、配置文件
│  ├─ 输出风险等级（low/medium/high）
│  └─ 附加影响面报告到审查输入
```

**执行方式**：

```bash
# 获取变更文件列表
git diff --name-only MERGE_BASE..HEAD -- '*.py'

# 运行影响分析（JSON 输出）
python D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\code-review\scripts\import_analyzer.py --changed-json '["file1.py", "file2.py"]' --root /project

# 以 Markdown 格式输出
python D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\code-review\scripts\import_analyzer.py --changed file1.py file2.py --root /project --format markdown
```

**风险等级与审查策略**：

| 风险等级 | 含义 | 审查策略 |
|---------|------|---------|
| `low` | 无直接影响 | 变更影响范围可控，正常审查 |
| `medium` | 有直接影响但无间接影响 | 建议审查直接影响文件的接口兼容性 |
| `high` | 有间接影响 | ⚠️ 重点审查间接影响文件的接口兼容性 |

**脚本位置**：`D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\code-review\scripts\import_analyzer.py`
**报告模板**：`D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\code-review\templates\impact-report.md`

### 文件交接规范

> 参考：Superpowers File Handoffs

所有产物通过**文件**传递，不粘贴到上下文：

```bash
# 生成 diff 文件
git diff BASE..HEAD > review_diff_BASE_HEAD.txt

# 生成任务 brief
# （从计划文件中提取任务描述到单独文件）
# 审查子代理读取文件，而非接收粘贴内容
```

**原因**：粘贴到上下文的内容会一直驻留，消耗后续 token。文件交接让审查子代理读取一次即可，不污染控制器上下文。

### 修复流程

```
审查发现 Critical/Important
    │
    ├─ 派发修复子代理
    │  ├─ 输入：审查发现 + 覆盖测试文件列表
    │  ├─ 修复 → 运行测试 → 报告结果
    │  └─ 报告必须包含：覆盖测试文件、运行命令、输出
    │
    └─ 重新审查（re-review）
        ├─ 确认修复覆盖所有 Critical/Important
        └─ Minor 记录到进度清单，留给分支级审查处理
```

**规则**：

- 一个修复子代理处理所有发现（不是每个发现一个）
- 修复子代理必须重新运行覆盖测试
- 重新审查前确认：覆盖测试文件、运行命令、输出三项齐全

---

## 审查模式选择（与两阶段并存）

| 模式 | 触发条件 | 代理数 | 耗时 | 适用场景 |
|------|---------|--------|------|---------|
| **快速审查** | 单文件 / <100行 / 用户说"快速看看" | 1 | 30秒 | 日常代码片段 |
| **标准审查** | 多文件 / <500行 / 默认模式 | 3 | 1-2分钟 | 常规PR/功能开发 |
| **深度审查** | >500行 / 关键模块 / 用户说"深度审查" | 5 | 3-5分钟 | 核心模块/安全敏感 |

## Step 1: 获取变更上下文

```bash
# 未暂存变更
git diff HEAD

# 已暂存变更
git diff --cached

# 指定文件
git diff HEAD -- path/to/file.py

# PR审查（如有gh CLI）
gh pr diff <number>
```

如果变更超过上下文限制：先生成文件列表，分批审查后汇总。

**完成条件**：已获取完整 diff 输出，确认变更文件数和行数，diff 已保存为文件（超过 500 行时）

## Step 2: 并行审查（核心流程）

### 快速审查（1个代理）

直接用 code-reviewer 角色审查，输出发现列表

### 标准审查（3个代理并行）

spawn 3个子代理，各自独立审查，返回发现列表

| 代理 | 视角 | 关注点 |
|------|------|--------|
| **Agent #1: Bug Hunter** | 代码正确性 | 只看diff，大bug优先，忽略nitpick。逻辑错误、边界条件、空值处理、错误处理缺失 |
| **Agent #2: Security & Performance** | 安全+性能 | 注入风险、权限校验、敏感信息泄露、N+1查询、内存泄漏 |
| **Agent #3: Maintainability** | 可维护性 | 命名规范、函数长度、重复代码、YAGNI决策阶梯、SOLID原则 |

### 深度审查（5个代理并行）

在标准审查基础上增加：

| 代理 | 视角 | 关注点 |
|------|------|--------|
| **Agent #4: History Context** | Git历史 | `git blame` 看修改历史，识别回归风险、历史bug模式 |
| **Agent #5: Spec Compliance** | 规范合规 | AGENTS.md/CLAUDE.md/项目规范是否被遵守，代码注释中的guidance是否被遵循 |

**并行执行方式**：使用 `sessions_spawn` 同时启动多个子代理，每个子代理独立返回发现列表

**完成条件**：所有代理均已返回发现列表（或超时跳过），发现已按文件/行号归组。快速模式：至少扫描了 diff 中所有变更行。标准模式：3 个代理各自独立返回。深度模式：5 个代理各自独立返回

## Step 3: 置信度验证（借鉴 Anthropic 核心设计）

对 Step 2 收集的每个 issue，独立评估置信度

### 置信度评分标准（0-100）

| 分数 | 含义 | 处理 |
|------|------|------|
| 0-24 | 假阳性，经不起推敲 | ❌ 过滤 |
| 25-49 | 可能是真的，但无法验证 | ❌ 过滤 |
| 50-74 | 确认是真的，但是nitpick | ⚠️ 标准/快速模式过滤，深度模式保留 |
| 75-89 | 高度确信，实际会发生 | ✅ 输出 |
| 90-100 | 绝对确认，证据直接支持 | ✅ 必须输出 |

### 验证检查清单

对每个 issue 逐项确认：

1. **是否预存在？** — PR未引入的问题不算
2. **是否真bug？** — 看起来像bug但实际不是的，降25分
3. **是否lint可捕获？** — typechecker/compiler/linter能发现的，降50分（假设CI会跑）
4. **是否被显式静默？** — 有 lint-ignore 注释的，降0分
5. **是否在修改范围内？** — 用户未修改的行上的问题，降0分
6. **是否有规范依据？** — 如果声称违反规范，必须找到具体条款，找不到降25分
7. **高级工程师会指出吗？** — 不会的nitpick，降20分

### 实现方式

快速/标准模式：主代理自行评估置信度（内部思考，不输出过程）
深度模式：为每个 issue spawn 独立验证子代理（Haiku/轻量模型），独立打分

**完成条件**：每个 issue 均有 0-100 的置信度评分，评分依据 7 项检查清单逐项扣分，低置信度 issue 已标记待过滤

## Step 4: 假阳性过滤清单

以下类型的发现**必须过滤**，无论置信度多高：

1. **预存在的问题** — PR未引入的
2. **伪bug** — 看起来像bug但实际是有意设计
3. **高级工程师不会指出的nitpick** — 如多余空格、import顺序（除非项目规范明确要求）
4. **构建工具可捕获的** — 类型错误、import缺失、格式问题（假设CI会跑）
5. **通用代码质量** — 缺乏测试覆盖、通用安全问题（除非项目规范明确要求）
6. **被显式静默的** — 有 lint-ignore / eslint-disable 注释的
7. **未修改行上的问题** — 用户PR未触碰的代码
8. **有意为之的变更** — 功能变更与PR目标一致

**完成条件**：所有 8 类假阳性均已检查，剩余 issue 均不属于任何过滤类别，过滤结果已记录

## Step 5: 严重性标签（细化版）

对每个发现使用以下标签，让作者知道什么是必须修复的：

| 前缀 | 含义 | 作者行为 |
|------|------|---------|
| (无前缀) | 必须修改 | 合并前必须解决 |
| **Critical:** | 阻塞合并 | 安全漏洞、数据丢失、功能损坏 |
| **Required:** | 必须修改 | 合并前必须解决 |
| **Nit:** | 次要、可选 | 作者可忽略——格式、风格偏好 |
| **Optional:** / **Consider:** | 建议 | 值得考虑但不强制 |
| **FYI** | 仅供参考 | 无需行动——为未来参考提供上下文 |

**排序原则**：按影响力排序，不要用小问题淹没真正的问题。一个高置信度的结构性问题比十个 nitpick 更重要

**完成条件**：每个发现均已标注严重性前缀（Critical/Required/Nit/Optional/FYI），按影响力降序排列，无重复发现

---

## Step 6: 输出格式

### 有高置信度发现时

```markdown
## 🔍 Code Review

审查模式：[快速/标准/深度] | 审查文件：X个 | 变更行数：+N/-N

发现 N 个问题：

### 1. [🔴Critical/🟡Warning/🔵Info] 问题标题（置信度：XX/100）

**位置**：`path/to/file.py:L42-L47`

**问题**：具体描述
**建议**：修复方案（附代码示例）

---

### 2. ...

### 评分

| 维度 | 分数 |
|------|------|
| 代码质量 | X/10 |
| 安全性 | X/10 |
| 可维护性 | X/10 |
| 代码精简度 | X/10 |
```

### 无高置信度发现时

```markdown
## 🔍 Code Review

审查模式：[快速/标准/深度] | 审查文件：X个 | 变更行数：+N/-N

✅ 未发现高置信度问题。代码审查通过。
```

**完成条件**：审查报告已输出，包含审查模式、文件数、变更行数、发现列表（或"通过"声明），每个发现有位置/问题/建议

## 链接格式规范

引用代码时必须提供可定位的链接：

- **Git仓库**：`https://github.com/owner/repo/blob/<full-sha>/path/file.py#L42-L47`
- **本地文件**：`path/to/file.py:L42-L47`
- 必须使用完整SHA（非缩写）
- 行范围至少包含 2 行上下文

## 与 coding-framework 的关系

| 场景 | 使用 |
|------|------|
| 写完代码后自查 | coding-framework → Rubber Duck 自审 |
| PR审查 / 他人代码审查 | **code-review skill**（本技能） |
| 深度安全审计 | coding-framework → security-auditor 代理 |
| 多代理并行审查 | **code-review skill**（本技能，自动编排） |

本技能复用 `D:\Users\yindb2\AppData\Roaming\mx\openclaw-home\yindb2\.openclaw\workspace\skills\coding-framework\agents\` 下的代理定义：

- `code-reviewer.yaml` → Bug Hunter + Maintainability
- `security-auditor.yaml` → Security & Performance
- `architecture-critic.yaml` → History Context（架构层面）
- `performance-analyst.yaml` → Security & Performance（性能层面）
- `maintainability-reviewer.yaml` → Maintainability

## 错误处理

| 情况 | 处理 |
|------|------|
| 非Git仓库 | 降级为单文件审查，跳过git blame |
| 变更过大（>2000行） | 分批审查，每批≤500行 |
| 子代理超时 | 跳过该维度，输出已完成维度的结果 |
| 无高置信度发现 | 输出"审查通过"，不硬凑问题 |

## 使用示例

```
# 快速审查
"帮我快速看看这段代码"
→ 快速审查模式，1个代理，30秒出结果

# 标准审查（默认）
"审查一下我的变更"
→ 标准审查模式，3个代理并行，1-2分钟

# 深度审查
"深度审查这个PR"
→ 深度审查模式，5个代理并行，3-5分钟

# 指定文件
"审查 src/auth.py 的变更"
→ 只审查指定文件

# PR审查
"审查 PR #42"
→ 通过 gh pr diff 获取变更，标准审查
```

---

## 补充规范（v1.1 新增，来源：Anthropic 官方）

### 变更大小指南

小规模的、聚焦的变更更容易审查、更快合并、部署更安全。目标大小：

| 变更行数 | 评价 | 说明 |
|---------|------|------|
| ~100 行 | ✅ 良好 | 一次审查可完成 |
| ~300 行 | ⚠️ 可接受 | 如果是单一逻辑变更 |
| ~1000 行 | ❌ 太大 | 必须拆分 |

**文件大小也要关注**：不仅是 diff 大小。一个小 diff 仍可能将文件推过健康边界——单文件超 1000 行是常见的检查信号（不是硬上限）。当变更显著增长一个已经很大的文件时，先考虑提取辅助函数、子组件或模块，再添加新功能。—*先分解，再添加*

**什么算"一个变更"**：一个独立的修改，解决一件事，包含相关测试，提交后系统保持可用。功能的一部分——不是整个功能。

**拆分策略**：

| 策略 | 方法 | 适用场景 |
|------|------|---------|
| 堆叠 | 提交小变更，基于它开始下一个 | 顺序依赖 |
| 按文件分离 | 为需要不同审查者的文件组分离变更 | 跨领域关注点 |
| 水平拆分 | 先创建共享代码/stub，再创建消费者 | 分层架构 |
| 垂直拆分 | 将功能拆分为更小的全栈切片 | 功能开发 |

**大变更可接受的场景**：完整的文件删除和自动化重构，审查者只需验证意图，而非每一行。

**将重构与功能工作分离**。既重构现有代码又添加新行为的变更是两个变更——分别提交。

---

### 变更描述规范

每个变更都需要一个在版本控制历史中独立的描述。

**第一行**：简短、祈使句、独立成句。"删除 FizzBuzz RPC" 而非 "正在删除 FizzBuzz RPC"。必须信息量足够，让搜索历史的人无需阅读 diff 就能理解变更。

**正文**：变更了什么以及为什么。包含代码中不可见的上下文、决策和推理。链接到 bug 编号、基准测试结果或设计文档。承认方法的不足之处。

**反模式**："修复 bug"、"修复构建"、"添加补丁"、"将代码从 A 移动到 B"、"第一阶段"、"添加便利函数"。

---

### 死代码清理

在任何重构或实现变更后，检查孤立代码：

1. 识别现在不可达或未使用的代码
2. 明确列出
3. 删除前询问："我应该删除这些现在未使用的元素吗：[列表]？"

不要让死代码四处散落——它会混淆未来的读者和代理。但不要默默删除你不确定的东西。有疑问时，先问。

```
发现死代码：
- formatLegacyDate() — src/utils/date.ts — 已被 formatDate() 替代
- OldTaskCard 组件 — src/components/ — 已被 TaskCard 替代
- LEGACY_API_URL 常量 — src/config.ts — 无剩余引用

→ 可以安全删除这些吗？
```

---

### 审查速度

缓慢的审查会阻塞整个团队。上下文切换审查的成本低于对他人造成的等待成本。

- **在一个工作日内响应**——这是最大值，不是目标
- **理想节奏**：收到审查请求后尽快响应，除非深度专注于编码。典型变更应在一天内完成多轮审查
- **优先快速个人响应而非快速最终批准**。即使需要多轮，快速反馈也能减少挫败感
- **大变更**：要求作者拆分，而非审查一个巨大的变更

---

### 争议处理

解决审查争议时，应用以下层级：

1. **技术事实和数据** 优先于观点和偏好
2. **风格指南** 是风格问题的绝对权威
3. **软件设计** 必须基于工程原则评估，而非个人偏好
4. **代码库一致性** 是可接受的，前提是不降低整体健康度

**不接受"我以后会清理"的经验**。经验表明延迟清理很少发生。要求提交前清理，除非是真正的紧急情况。如果周围问题无法在此变更中解决，要求提交 bug 并自我分配。

---

### 审查中的诚实

审查代码时——无论是你自己、另一个代理还是人类写的：

- **不要橡皮图章**。没有审查证据的"LGTM"对任何人都没有帮助
- **不要软化真正的问题**。当它是一个会进入生产环境的 bug 时，说"这可能是一个小问题"是不诚实的
- **尽可能量化问题**："这个 N+1 查询将为列表中的每个项目增加约 50ms" 比 "这可能会很慢" 更好
- **对有明确问题的方法推荐替代**。谄媚是审查中的一种失败模式。如果实现有问题，直接说出来并提出替代方案
- **优雅地接受覆盖**。如果作者有完整上下文并不同意，尊重他们的判断。评论代码，而非人——将个人批评重新聚焦到代码本身

---

### 依赖审查

代码审查的一部分是依赖审查：

**添加任何依赖之前**：

- 现有堆栈能解决这个问题吗？（通常可以。）
- 依赖有多大？（检查包大小影响。）
- 是否积极维护？（检查最后提交、开放问题。）
- 是否有已知漏洞？（npm audit）
- 许可证是什么？（必须与项目兼容。）

**规则**：优先使用标准库和现有工具而非新依赖。每个依赖都是一项负债。

---

### 完整审查清单

```markdown
## 审查：[PR/变更标题]

### 上下文
- [ ] 我理解这个变更做什么以及为什么

### 正确性
- [ ] 变更符合规范/任务要求
- [ ] 边界情况已处理
- [ ] 错误路径已处理
- [ ] 测试充分覆盖变更

### 可读性
- [ ] 名称清晰且一致
- [ ] 逻辑直接
- [ ] 无不必要的复杂性

### 架构
- [ ] 遵循现有模式
- [ ] 无不必要的耦合或依赖
- [ ] 抽象级别适当
- [ ] 重构减少复杂性而非重新定位它
- [ ] 无功能逻辑在共享模块中；文件保持在健康大小内

### 安全性
- [ ] 代码中无密钥
- [ ] 输入在边界处验证
- [ ] 无注入漏洞
- [ ] 认证检查到位
- [ ] 外部数据源被视为不可信

### 性能
- [ ] 无 N+1 模式
- [ ] 无无界操作
- [ ] 列表端点有分页

### 验证
- [ ] 测试通过
- [ ] 构建成功
- [ ] 手动验证完成（如适用）

### 结论
- [ ] **批准** → 准备合并
- [ ] **请求变更** → 必须解决问题
```

---

### 常见借口 vs 现实

| 借口 | 现实 |
|------|------|
| "能跑就行" | 能运行但不可读、不安全或架构错误的代码会累积技术债务 |
| "我自己写的，我知道是对的" | 作者对自己的盲点视而不见。每个变更都受益于另一双眼睛 |
| "我们以后会清理" | 以后永远不会来。审查是质量门禁——使用它。要求合并前清理，而非之后 |
| "AI 生成的代码可能没问题" | AI 代码需要更多审查，而非更少。它自信且合理，即使是错的 |
| "测试通过了，所以没问题" | 测试是必要但不充分的。它们不捕捉架构问题、安全问题或可读性问题 |
| "重构让它更干净了" | 重新定位复杂性不等于减少它。如果读者仍需持有相同数量的概念，结构就没有改进——寻找让分支消失的版本 |
| "这只是对文件的小添加" | 即使 diff 仍会将文件推过健康大小，并将分支添加到不相关的流程中。判断结果结构，而非 diff 大小 |

---

### 红旗

- PR 未经任何审查就合并
- 审查只检查测试是否通过（忽略其他维度）
- 没有审查证据的"LGTM"
- 安全敏感变更没有安全聚焦的审查
- "太大无法仔细审查"的大 PR（拆分它们）
- Bug 修复 PR 没有回归测试
- 没有严重性标签的审查评论——不清楚什么是必需的 vs 可选的
- 接受"我以后会修复"——永远不会发生
- 重新定位复杂性而非减少它的重构
- 增长已经很大的文件而非分解它的变更
- 散布到不相关代码路径中的新条件（缺失的抽象）
- 复制现有规范辅助函数的定制辅助函数，或功能逻辑放在共享模块中

---

### 验证

审查完成后：

- [ ] 所有 Critical 问题已解决
- [ ] 所有 Required（无前缀）变更已解决或明确延迟并有理由
- [ ] 测试通过
- [ ] 构建成功
- [ ] 验证故事已记录（变更了什么，如何验证的）
- [ ] **前端任务必须包含浏览器验证**（v1.3 新增，借鉴 snarktank/ralph）：
  - 检测条件：修改了 `.tsx/.jsx/.vue/.html/.css` 或 `src/components/` 目录
  - 强制要求：acceptance_criteria 包含 "Verify in browser"
  - 缺少浏览器验证 → 标记为 Critical

**假定阻塞性**：为以下情况提出并建议更简单的设计；仅当变更主动使结构变差时才升级为 Required：重新定位复杂性而非减少它的重构；将文件推过大小边界而没有分解的变更；功能逻辑添加到共享模块；现有规范辅助函数的近似重复；隐藏不明确不变量的静默回退

---

*Version 1.3.0 — 新增前端任务浏览器验证强制检查（借鉴 snarktank/ralph）*

---

## 🎨 可视化审查增强（v1.4 新增）

> 方案A：自研增强版，零外部依赖，将Plannotator设计理念重新实现
> 作为Stage 2分支级审查的**并行增强通道**，opt-in模式，不替换默认审查路径

### 架构

```
scripts/
├── visual_review.py       # CLI入口（4.6KB）
├── diff_parser.py         # diff解析器（12.6KB）
├── diff_renderer.py       # 终端彩色diff渲染（4KB）
├── annotation_store.py    # 行级标注存储（6.5KB）
└── report_generator.py    # HTML报告生成器（20.8KB）
```

### CLI命令

```bash
# 终端彩色diff
visual_review.py diff HEAD~1              # 查看上一个commit的diff
visual_review.py diff --cached            # 查看暂存区变更
visual_review.py summary HEAD~3           # 最近3个commit的文件摘要

# 行级标注
visual_review.py annotate src/main.py 42 -s warning -m "Null check needed"
visual_review.py annotate src/utils.py 10 -s suggestion -m "Use pathlib"
visual_review.py annotations list         # 列出所有标注
visual_review.py annotations summary      # 标注汇总

# 报告生成
visual_review.py report --html report.html        # 生成HTML报告（GitHub Dark风格）
visual_review.py report --json report.json        # 导出JSON结构化数据
visual_review.py export --format json             # 导出diff为JSON

# Canvas集成
visual_review.py serve                    # 生成HTML供canvas展示
```

### 标注严重级别

| 级别 | 含义 | 是否阻塞合并 |
|------|------|-------------|
| `critical` | 必须修复，阻塞合并 | ✅ 是 |
| `warning` | 建议修复，不阻塞 | ❌ 否 |
| `suggestion` | 可选优化 | ❌ 否 |
| `nit` | 细节问题 | ❌ 否 |

### 与Stage 2集成

```
Stage 2 分支级审查（默认路径不变）
    │
    ├─ Track A: 子代理自动审查（始终执行）
    │
    └─ Track B: 可视化审查（opt-in，用户追加 --review=visual）
        ├─ 生成终端彩色diff
        ├─ 人工添加行级标注
        ├─ 导出JSON/HTML报告
        └─ 标注结果回流到审查流程
```

### HTML报告特性

- GitHub Dark风格（0d1117背景）
- 彩色diff（绿色增加/红色删除）
- 标注气泡（按严重级别着色）
- 文件导航侧边栏
- 响应式布局

### 使用示例

```bash
# 场景1：快速查看变更
visual_review.py diff HEAD~1

# 场景2：详细审查并标注
visual_review.py annotate src/api.py 15 -s warning -m "Missing auth check"
visual_review.py annotate src/api.py 28 -s suggestion -m "Extract to helper"
visual_review.py report --html review.html  # 生成报告

# 场景3：导出结构化数据供其他skill消费
visual_review.py export --format json > review_data.json
```

---

*Version 1.4.0 — 新增可视化审查增强（方案A自研，零外部依赖）*

---

## 重型模式：多代理并行审查（合并自multi-agent-review v1.0.0）

> 当代码变更涉及5+文件或1000+行时，启用6代理并行审查模式。
> 来源：multi-agent-review skill，借鉴 Claude Code pr-review-toolkit。

### 触发条件

- 用户明确要求"全面审查"/"多代理审查"/"多维度评估"
- 变更规模超过5个文件或1000+行
- PR合并前的最终评估

### 审查代理定义

| 代理 | 职责 | 关注点 |
|------|------|--------|
| architecture-critic | 架构批评员 | 模块划分、依赖关系、扩展性 |
| security-auditor | 安全审计员 | 漏洞、敏感信息、权限风险 |
| test-engineer | 测试工程师 | 覆盖率、边界条件、测试质量 |
| performance-analyst | 性能分析师 | 时间/空间复杂度、资源泄漏 |
| maintainability-reviewer | 可维护性审查员 | 代码清晰度、文档、命名 |
| documentation-checker | 文档检查员 | API文档、注释完整性 |

### 智能选择规则

根据文件类型自动选择相关代理：

| 文件类型 | 选择代理 |
|---------|---------|
| `.py` / `.js` / `.ts` / `.java` | 全部代理 |
| `.sql` | security-auditor + performance-analyst |
| `.md` / `.rst` | documentation-checker |
| `Dockerfile` / `docker-compose` | security-auditor + architecture-critic |
| `test_*` / `*_test.*` | test-engineer |

### 并行审查流程

```
用户提交代码审查请求
  → ├─ 1. 解析目标代码（文件范围、语言、框架）
  → ├─ 2. 并行 spawn 6 个子代理
  →    ├→ architecture-critic
  →    ├→ security-auditor
  →    ├→ test-engineer
  →    ├→ performance-analyst
  →    ├→ maintainability-reviewer
  →    └→ documentation-checker
  → ├─ 3. 收集各代理结构化结果（JSON格式）
  → ├─ 4. 置信度过滤（≥80分的发现才纳入报告）
  → ├─ 5. 冲突解决（多代理意见不一致时）
  → └─ 6. 生成汇总报告
```

### 编排逻辑

**Step 1：解析输入** — 提取目标文件/目录、审查范围（全量/增量）、特殊关注点

**Step 2：并行spawn** — 对每个代理使用 sessions_spawn 同时发起，不等待前一个完成

**Step 3：收集结果** — 每个代理返回JSON格式：

```json
{
  "agent": "architecture-critic",
  "findings": [
    {
      "severity": "high",
      "title": "模块耦合度过高",
      "location": "src/service.py:45",
      "description": "Service 类直接依赖 Database 实现",
      "suggestion": "引入 Repository 接口解耦",
      "confidence": 85
    }
  ],
  "score": 6,
  "summary": "架构存在耦合问题，建议重构"
}
```

**Step 4：置信度过滤** — ≥80纳入报告，60-79标记"待确认"，<60丢弃

**Step 5：冲突解决** — 严重性优先 → 置信度加权 → 标注分歧 → 人工裁决

**冲突检测逻辑**：
- 同一文件 + 相近行号（±5 行）= 同一位置
- 一个代理说"没问题"而另一个说"有问题" = 矛盾
- 两个代理给出相反的修复建议 = 冲突

**Step 6：汇总报告** — 各维度评分表 + 关键发现（按严重性排序）+ 冲突项 + 建议行动

### 降级策略

| 场景 | 降级方案 |
|------|----------|
| 部分代理spawn失败 | 继续已成功的代理结果，标注失败的代理 |
| 所有代理spawn失败 | 回退到单代理模式（主会话直接审查） |
| 代理超时（>5分钟） | 终止超时代理，使用已完成代理的结果 |
| 并发代理数受限 | 分批spawn（每批3个） |
| 结果数量过多（>50条） | 只展示Critical + High，其余折叠为摘要 |

### 与coding-framework集成

| 维度 | 标准审查（Stage 1/2） | 重型模式（多代理并行） |
|------|----------------------|----------------------|
| 代理数 | 1-3个（按需选择） | 6个（全量） |
| 适用场景 | 日常代码审查 | PR合并前全面评估 |
| 耗时 | 短（<2分钟） | 长（2-5分钟） |
| 输出 | 简洁发现列表 | 完整多维度报告 |

### 调度规则

```
用户请求代码审查
  → daily-agent 判断任务复杂度
  ├─ 小改动（<3文件） → 标准审查流程
  └─ 大改动（≥5文件）或用户要求"全面审查" → 重型模式（多代理并行）
```

### 与code-review-visualizer配合

重型模式审查完成后，将汇总报告输出给code-review-visualizer生成可视化HTML页面。

---

## 任务完成后

完成任务后，做任务总结，将操作记录更新到 record.md 中。

---

*Version 2.2.0 — 重型模式增强：智能选择规则（根据文件类型自动选择代理）+ 冲突检测逻辑（同文件±5行=同位置）*

# Pattern: Reviewer（审查员）

> 控制的不确定性：**质量不确定**——审查结果靠感觉，不可复现。

## 何时用

当手里已经有一套人类审查标准时。判断标准：**一个任务可以由人拿着检查清单完成**，那它大概率能设计成 Reviewer Skill。

典型场景：
- 代码审查 / 安全审计 / 架构评审
- 文档风格审查 / 合规检查
- Prompt 审查 / 数据质量检查
- 发布前检查

## 目录结构

```
skill-name/
├── SKILL.md                       # 审查协议（怎么检查、怎么输出）
└── references/
    └── review-checklist.md        # 检查什么（具体规则）
```

**关键拆分**：checklist 文件定义**检查什么**；SKILL.md 定义**怎么检查、怎么输出**。

## 核心要素：证据 4 要素（强制）

好的 Reviewer 强制每个发现必须含：

| 要素 | 说明 |
|---|---|
| **位置** | 行号或大致位置 |
| **严重程度** | error（必须修复）/ warning（应该修复）/ info（考虑） |
| **原因** | 解释**为什么**是问题，不只**什么**错了 |
| **影响/修复方案** | 具体修复建议，必要时给修正后的代码 |

发现按 **error → warning → info** 分组。最后给评分 + 前三条建议。

## 最小 SKILL.md 骨架

```markdown
---
name: code-reviewer
description: 审查 Python 代码的质量、风格和常见错误。当用户提交代码审查或请求代码反馈时使用。
agent_created: true
---

你是 Python 代码审查员。严格遵循此审查协议：

步骤1：加载 `references/review-checklist.md` 获取完整的审查标准。

步骤2：仔细阅读用户代码。在批评前先理解其目的。

步骤3：将检查清单中的每条规则应用到代码上。对每个发现的违规：
- 记录行号（或大致位置）
- 分类严重程度：error / warning / info
- 解释为什么是问题
- 建议具体的修复方案，附带修正后的代码

步骤4：生成结构化审查：
- 摘要：代码做什么，整体质量评估
- 发现：按严重程度分组（error 优先，然后 warning，然后 info）
- 评分：1-10 分，附带简要理由
- 前 3 条建议：最有影响力的改进
```

## references/review-checklist.md 示例

```markdown
# Python Code Review Checklist

## Correctness (Severity: error)
- [ ] No undefined variables or missing imports

## Style (Severity: warning)
- [ ] Functions use snake_case, classes use PascalCase

## Security (Severity: error)
- [ ] No hardcoded secrets (passwords, API keys, tokens)

## Performance (Severity: info)
- [ ] No unnecessary nested loops (O(n^2) when O(n) is possible)
```

## 常见坑

| 坑 | 后果 | 修正 |
|---|---|---|
| 没有证据要求 | 输出泛泛而谈的建议 | 强制 4 要素：位置/严重度/原因/修复 |
| 不分组严重程度 | 无法快速定位必修项 | error→warning→info 分组 |
| checklist 和协议混一起 | 改规则连流程也动 | checklist→references/，协议→SKILL.md |
| 先批评再理解意图 | 误判设计意图 | "在批评前先理解其目的"放步骤2 |

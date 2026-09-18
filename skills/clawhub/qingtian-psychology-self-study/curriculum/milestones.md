# 里程碑定义与检测规则

> 里程碑在 Onboarding 时初始化进 `progress.json` 的 `milestones[]`（定义见 `roadmap.json`）。每次写操作后由处理器检查 `condition`，达标则 `reached=true` 并触发祝贺。

## 10 个里程碑

| ID | 文本 | 触发条件（condition） |
|---|---|---|
| m1 | 学完第一个流派（CBT/精神分析/人本主义任选） | modules.counseling.completed >= 1 |
| m2 | 完成第一次 TPR 咨询练习 | stats.practiceCount >= 1 |
| m3 | 读完第一本心理学教材 | stats.booksRead >= 1 |
| m4 | 完成第一次对话分析 | stats.analyses >= 1 |
| m5 | 累计学习 50 小时 | stats.totalHours >= 50 |
| m6 | 累计学习 100 小时 | stats.totalHours >= 100 |
| m7 | 完成第一次费曼输出 | stats.feynmanOutputs >= 1 |
| m8 | 完成第一篇案例分析报告 | modules.cases.completed >= 1 |
| m9 | 累计 20 次 TPR 练习 | stats.practiceCount >= 20 |
| m10 | 读完 10 本心理学书 | stats.booksRead >= 10 |

## 检测时机

- 在以下处理器写操作末尾调用 `checkMilestones(data)`：
  - learn（modules 变化）、practice/逐字稿分析（practiceCount/dialogues/analyses）
  - assess、summary（reflections）、query（不写但可展示）
  - 任何更新 stats.totalHours / stats.booksRead 的地方
- 新点亮里程碑 → 在回复中插一句祝贺，如：「🎉 里程碑达成：完成第一次 TPR 咨询练习！继续加油。」

| ID | 文本 | 条件 |
|---|---|---|

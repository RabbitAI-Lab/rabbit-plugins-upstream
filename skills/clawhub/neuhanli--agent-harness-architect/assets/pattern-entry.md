# 模式条目模板（patterns/<name>.md）

> 跨领域设计模式：从别的领域（数据库、软件工程、编程语言、安全……）借来的、可迁移到 harness 设计的思维模型。

```markdown
---
name: <模式名称，如 Event Sourcing>
domain: <来源领域，如 数据库 / 软件工程>
added: <YYYY-MM-DD>
confidence: verified               # verified / unverified
---

## 核心思想
<用几句话说清这个模式在解决什么问题、怎么解决>

## 可迁移到 harness 的哪一层
<对应 H 六层中的哪一层/哪几层，如 S 状态存储、V 评估>

## 典型应用案例
<真实案例（可指向 frameworks/core/ 中的案例），没有则写"待补">

## 对照问题（抛给用户，而非答案）
<设计时抛出的问题，如："你的状态存储是不是同一个问题？哪里像、哪里不像？">
```

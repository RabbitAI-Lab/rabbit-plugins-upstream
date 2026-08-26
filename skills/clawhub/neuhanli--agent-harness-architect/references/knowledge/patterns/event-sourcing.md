---
name: Event Sourcing（事件溯源）
domain: 数据库 / 软件工程
added: 2026-08-23
confidence: verified
---

## 核心思想

不存储"当前状态"，只追加存储"发生了什么事件"。状态由事件流重放推导。事件流是不可变的单一真相源，天然支持审计、回放、时间旅行、fork。

## 可迁移到 harness 的哪一层

S（状态存储）、V（评估/可回放）

## 典型应用案例

DeepSeek Harness 的 append-only session log（"model-visible means logged"）；Codex Harness 的 Item/Turn/Thread 事件流。

## 对照问题（抛给用户，而非答案）

你的状态是"直接存当前值"还是"存发生了什么"？如果你的会话需要可回放、可 fork、可审计，把"日志"从顺便记录提升为"唯一真相源"会带来什么？

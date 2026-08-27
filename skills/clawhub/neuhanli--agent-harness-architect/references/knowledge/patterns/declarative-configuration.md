---
name: Declarative Configuration（声明式配置）
domain: DevOps / 基础设施
added: 2026-08-23
confidence: verified
---

## 核心思想

用配置（YAML/JSON/schema）描述"想要什么状态"，而非用代码写"怎么做"。配置可 diff、可版本化、可覆盖（patch/overlay），运行时照着配置执行。

## 可迁移到 harness 的哪一层

P（配置方式）、T（工具装配）

## 典型应用案例

DeepSeek Harness 的 cordis.yml / patch（可替换任意配置行）；OpenClaw 的可视化配置 + hot-reload。

## 对照问题（抛给用户，而非答案）

你的用户"配置一个 agent"是写代码还是写配置？团队想覆盖某个默认行为时，需要 fork 源码还是改一行配置？声明式和命令式的边界应该划在哪？

---
name: Capability Security（能力安全 / 最小权限）
domain: 安全
added: 2026-08-23
confidence: verified
---

## 核心思想

不按"身份"授权，按"能力"授权（capability-based security）。每个主体只拿到它完成任务所需的最小能力集，能力不可越界、不可伪造。最小权限要在结构层强制，而非只在 prompt 层"请求"模型配合。

## 可迁移到 harness 的哪一层

L（生命周期钩子/安全）、T（工具注册）

## 典型应用案例

OpenClaw 的 Reader/Actor 双代理权限分离（工具级 ACL，抗 prompt 注入）；Claude Code 的权限模式（allow/ask/deny）+ PreToolUse hook deny。

## 对照问题（抛给用户，而非答案）

你的工具权限是按"整个 agent"给，还是按"子任务/子代理"细分？你的安全边界是靠 prompt 提示，还是靠结构强制？如果模型被注入，结构层能不能兜住？

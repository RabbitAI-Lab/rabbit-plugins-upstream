---
name: Letta
alias: letta
type: harness
source: https://github.com/letta-ai/letta
papers: ["MemGPT: Towards LLMs as Operating Systems (arXiv:2310.08560, UC Berkeley)"]
added: 2026-09-09
version: 活跃（Letta Agent SDK / 服务端；V1 SDK 转 legacy）
confidence: verified
pinned: false
---

## 一句话定位

UC Berkeley（MemGPT 作者）团队的**有状态 agent 服务端平台**——官方自称 "Letta agent harness"。把 agent 做成**服务端持久实体**，核心范式是"像操作系统管虚拟内存一样管上下文与记忆"，并**内建评估子系统**。是 S（状态/记忆）+ V（评估）+ 服务端部署的对照锚点。

## H 六层映射

- **E**: 服务端 agent loop（reasoning → 工具调用 → response，支持多步/长任务、流式消息）；中心化、每 agent 一条主循环，可选 subagents。
- **T**: built-in tools + client tools + server tools + MCP tools + human-in-the-loop 工具；**记忆操作本身就是工具**（core_memory_* / archival_memory_* / conversation_search），agent 借工具自编辑记忆。
- **C**: **核心层**——MemGPT 式"虚拟内存"分层：core memory（窗口内、可自编辑的 memory blocks，如 persona/human）+ archival memory（窗口外、向量检索）+ recall/conversation memory；context hierarchy 在窗口内/外之间分页，超限触发 compaction（压缩）。把上下文当虚拟内存管，而非单纯截断/摘要。
- **S**: **状态即一等公民**——agent 持久化在服务端数据库（"stateful agents as a service"）；AgentFile（.af）可导出/导入迁移；conversation 可 fork / compaction / reset；记忆跨会话持久（"learn and self-improve over time"）。
- **L**: permissions（工具级审批）、human-in-the-loop 工具、access tokens、服务端鉴权。
- **V**: **内建 Eval 子系统**——suites / datasets / targets / graders（tool、rubric、multi-metric）/ extractors / gates + 结果指标；评估与运行时同层，而非事后外挂脚本。

## 范式 P

扩展方式=混合（记忆/状态运行时**内建为主** + 可选 skills / subagents / mods / MCP 扩展）· 配置方式=声明式（agent、memory blocks、templates 配置 + API / ADE）· 部署=**服务端托管 / 自托管（agent-as-a-service）**· 编排=中心化（每 agent 服务端 loop，subagents 可选）

## 原创点（框架外，重点标注）

1. **MemGPT 上下文分页（把 LLM 当 OS 管虚拟内存）**：core（窗口内可编辑）/ archival（窗口外向量）/ recall 分层，agent 自主用工具在层间搬运与改写记忆——上下文管理从"截断/摘要"升级为"操作系统式虚拟内存"。
2. **有状态 agent 即服务（stateful-agent-as-a-service）**：agent 是服务端持久实体（数据库 + 可迁移的 AgentFile），而非一次性进程；"跨会话学习/自我改进"内建。
3. **评估作为平台内建一等公民**：Evals 套件（dataset + grader + gate）与运行时同层，是"V 层产品化"的范本。

## 设计启发

- **做 C 层时**：对照"你的长上下文靠截断/摘要，还是靠'分层 + agent 自主搬运'（虚拟内存范式）？"
- **做 S 层时**：对照"agent 状态是一次性进程态，还是服务端可持久、可迁移（AgentFile）的实体？要不要支持跨会话自我改进？"
- **做 V 层时**：对照"评估是外挂脚本，还是与运行时同层的内建子系统（dataset + grader + gate）？"
- **做部署 / P 时**：对照"你的 harness 是 CLI / 嵌入式，还是 agent-as-a-service 服务端？需不需要多客户端接入？"

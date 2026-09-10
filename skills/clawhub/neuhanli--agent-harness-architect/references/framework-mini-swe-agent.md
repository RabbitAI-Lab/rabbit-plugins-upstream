---
name: mini-SWE-agent
alias: mini-swe
type: harness
source: https://github.com/SWE-agent/mini-swe-agent
papers: ["SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (NeurIPS 2024, arXiv:2405.15793, 前身/ACI 思想来源)"]
added: 2026-09-09
version: 活跃维护（前身 SWE-agent 已转 maintenance-only，官方推荐 mini）
confidence: verified
pinned: false
---

## 一句话定位

Princeton 的极简 coding agent harness：核心约 100 行 Python，**除 bash 外不提供任何工具、不使用 function-calling**，靠精心设计的提示与交互（ACI 思想的极简版）在 SWE-bench Verified 上跑出 >74%。是"激进极简 / 反插件"的对照锚点。

## H 六层映射

- **E**: 极简扁平控制循环——官方称"very simple control flow"；单一 agent loop，无策略选择器、无子代理编排；核心约 100 行（+ env / model / script 各约 100）。刻意"少即是多"。
- **T**: **只有一个 bash 工具，且不用 function-calling**（官方原话："Does not have any tools other than bash"）。把"工具注册"压到极致：不给模型一堆工具，而给一个通用 bash + 设计良好的交互约定。
- **C**: 依赖模型长上下文 + 简单截断；不建复杂记忆层级（与 Letta 正好相反）。
- **S**: 轻量——状态主要落在被操作的仓库/环境与运行日志，不强制持久化记忆库。
- **L**: 以执行环境沙箱隔离为主（官方强调"simpler & more stable sandboxing"），拦截点是运行环境，而非多层 hook。
- **V**: 以 SWE-bench Verified 跑分作为客观验证接口（>74%，用强模型如 Gemini 3 Pro）；benchmark 即评估。

## 范式 P

扩展方式=**嵌入式（极简，反插件）**· 配置方式=命令式为主（脚本 + 少量参数，"no huge configs"）· 部署=本地 / CLI 单机 · 编排=中心化（单循环，无多代理）

## 原创点（框架外，重点标注）

1. **"激进极简"作为架构立场**：用约 100 行 + 单 bash 工具达到 >74% SWE-bench Verified，反证"能力 ≠ 复杂度"。与 DeepSeek Harness「一切皆插件」、OpenClaw「3200+ skills」直接对立，是**架构克制（restraint）**的活样本。
2. **ACI 的极简收敛**：与其暴露原始能力或堆工具，不如设计"模型友好"的窄接口——mini 把它推到极致："干脆只给 bash + 好提示"。

## 设计启发

- **做 T 层时**：对照"你真的需要工具注册表 / 插件机制吗？一个精心设计的通用工具（bash）+ 好提示能不能打平？"（克制）
- **做 P·扩展方式时**：对照"插件化带来的可扩展性，值不值它引入的复杂度？你的场景有没有'让第三方随便加插件'的真实需求？"（**反插件偏见**的对照物）
- **纠结要不要上多代理 / 复杂编排时**：对照 mini 的单循环——"扁平、简单、一眼能看懂的控制流够不够？"

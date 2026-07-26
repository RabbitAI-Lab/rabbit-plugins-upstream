# CMS Project Governance 中文治理协议

版本：2.0.0

本 Skill 是 AI 辅助开发的人机控制层。它帮助非技术或技术用户把概念、问题和方向整理成可确认的结果，选择最小可用交付，控制长时间开发的偏差，并把“Developer 已完成”与“QA 已验收”分开。

机器可读的 frontmatter 字段和状态枚举必须保留英文，以便与 `agent-loop-engineering` 和校验脚本互通。

## 核心原则

1. 用户负责目的、优先级和重大决策；
2. AI 负责需求分析、选项、建议、拆分和推进方法；
3. 不要求非技术用户设计架构、选择框架或编写测试；
4. 治理的目标是减少不确定性和返工，而不是增加文书；
5. Milestone 是连贯、用户可感知的能力，不是短任务或计时阶段；
6. `Developer Complete` 不等于已验收；
7. 证据高于状态文字；
8. 局部达标不能掩盖整体目标偏离；
9. 使用足以控制真实风险的最轻治理方式；
10. Owner、Controller、Developer 和 QA 权限必须分开。

## 与 Agent Loop Engineering 的关系

- 本 Skill 负责发现、评估、授权、复核和验收；
- `agent-loop-engineering` 负责执行已授权编码目标；
- 两者通过 contract version `2.0` 的 `Docs/ACTIVE_PACKET.md` 交接；
- 两个 Skill 都可独立使用；同时安装时，本 Skill 管理目标与验收权限，执行 Skill 管理实现证据。

创建或检查 Active Packet 前，读取 `{baseDir}/references/zh-CN/execution-contract.md`。

## 每次只选择一个模式

| 用户需求 | 模式 | 读取 |
| --- | --- | --- |
| 只有想法，不知道如何实现 | 目标发现 | `references/zh-CN/goal-discovery.md` |
| 把明确目标变成适当规模的交付 | 计划与规模评估 | `references/zh-CN/planning-and-sizing.md` |
| 创建 Milestone、Program 或授权工单 | Dispatch | `references/zh-CN/governance-profiles.md`、`references/zh-CN/controller-qa.md` |
| 只检查最新交付或 Handoff | 最新交付审查 / QA | `references/zh-CN/controller-qa.md` |
| 检查当前工作是否仍服务原始目的 | 方向对齐 | `references/zh-CN/alignment-and-rebaseline.md` |
| 把新需求与当前目标比较 | 目标重基线 | `references/zh-CN/alignment-and-rebaseline.md` |
| 全项目审计或阶段结束线 | 审计 / 路线图 | `references/zh-CN/alignment-and-rebaseline.md` |

模式边界：

- 目标发现只能生成 Intent Brief，不能开始编码；
- 计划与 Dispatch 可以授权工作，不能实现产品代码；
- 最新交付审查只检查当前授权范围，不能变成全项目审计；
- 方向对齐检查偏差，不能静默改写 Target；
- Target 或 Non-Goals 只有 Owner 授权的重基线模式可以修改；
- 审计和路线图默认只读，后续状态修改需要另行授权。

## 通用流程

```text
概念或问题
  -> 明确期望结果
  -> 定义最简单有用流程
  -> 标明假设与边界
  -> 定义可观察成功
  -> Ready for Planning
  -> 评估 Small / Medium / Large
  -> 选择 Lite / Standard / Full
  -> 创建 Active Packet
  -> 授权执行
  -> 方向检查
  -> QA 决策
  -> 验收、修复、拆分、重基线或停止
```

不要求需求完美。可逆的不确定项可以在明确记录假设后继续；只有可能改变核心目标、产生重大风险或浪费大量工作的未知项才停止。

## 状态维度

这些状态必须分开记录：

| 维度 | 允许值 |
| --- | --- |
| 目标准备度 | `Concept`、`Direction`、`Ready for Planning`、`Ready for Execution`、`Owner Decision Required` |
| 执行 | `Ready`、`In Progress`、`Ready for Review`、`Needs Fix`、`Blocked`、`Invalid State` |
| 对齐 | `Aligned`、`At Risk`、`Locally Compliant, Globally Misaligned`、`Owner Review Required` |
| QA 决策 | `Not Reviewed`、`Accepted`、`Accepted With Risk`、`Failed`、`Blocked`、`Not Required` |
| 项目 | `Active`、`Needs Fix`、`Blocked`、`Accepted`、`Accepted With Risk`、`Invalid State` |

不能用一个状态掩盖另一个状态。例如自动检查通过，但结果不再服务原始目标时，可以同时存在“局部合规”和“全局偏离”。

## 必须门禁

- 期望结果、最小范围、Non-Goals、验收证据和重大约束不够清楚时，不授权执行；
- `qa_required: true` 时，不能根据 Developer 自述直接验收；
- QA 失败后保留同一个 Milestone 和 Work Order，设置 `project_state: Needs Fix`，并针对失败标准创建有界修复；
- 核心流程失败不能改写成 `Accepted With Risk`；
- Core Target、Non-Goals、受保护架构/数据边界、生产访问、凭据、部署、破坏性操作、付费资源或不可逆选择必须交 Owner；
- 第 10 阶段必须验收、修复、拆分或重基线，不能自动续期。

## 最小读取

按以下顺序开始：

1. 存在时读取 `Docs/ACTIVE_PACKET.md`；
2. 只读取 Packet 明确链接的文件；
3. 读取最新相关证据和 QA 决策；
4. 只有发生偏差、矛盾或全项目审计时才读取历史文件。

旧项目没有 Active Packet 时，读取当前 `TARGET.md`、`ACCEPTANCE.md`、活动 `WORK_ORDER*.md`、最新 `STATUS.md`、一个立即下一步、阻塞和近期证据，不默认扫描所有历史 Milestone。

冲突时报告 `Invalid State`。权限顺序：

```text
Owner 已批准的 TARGET / Non-Goals
  -> ACCEPTANCE
  -> 当前 WORK_ORDER
  -> ACTIVE_PACKET 的当前阶段投影
  -> 状态、下一步和日志
```

## 文档纪律

创建文件前读取 `{baseDir}/references/zh-CN/governance-profiles.md`。

- 早期想法讨论默认不创建文件；
- 不为每个阶段、失败测试、修复或对话创建文件；
- 保持一份规范 Active Packet，以链接引用证据；
- 只有权限边界、独立 QA、Owner 决策、跨 Agent 交接、正式重基线或归档边界才创建新文件；
- 活动文件难以扫描时归档旧历史，不能让状态文件变成永久日志。

## 输出合同

每次治理响应必须以以下内容结束：

```text
模式：
当前准备度/状态：
决策：
原因：
现在做：
以后做：
暂时不做：
需要 Owner 决策：
下一项证据：
创建或更新的文件：
```

目标发现使用 Intent Brief；QA 必须列出标准、证据、决定、修复、负责人和重新验证。输出应让非技术 Owner 也能理解。


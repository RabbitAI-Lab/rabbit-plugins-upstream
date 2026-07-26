# Agent Loop Engineering 中文执行协议

版本：2.0.0

本 Skill 是 AI 编码工作的执行层。它接收一个已获授权、可以验收的目标，通过有边界的实现、验证、修复和记录持续推进，直到工作可交给 QA、需要修复，或触发真实停止条件。

机器可读的 frontmatter 字段和状态枚举必须保留英文，以便与 `cms-project-governance` 和校验脚本互通。

## 入口门禁

只有以下内容足够清楚时才开始编码：

- 用户可感知的期望结果；
- 当前范围和 Non-Goals；
- 可观察的验收标准；
- 允许修改与受保护边界；
- 必须提供的证据；
- 当前唯一下一步。

优先使用 contract version `2.0` 的 `Docs/ACTIVE_PACKET.md`。执行前读取 `{baseDir}/references/zh-CN/execution-loop.md`。

如果用户只有概念、方向或问题，不要自行猜出完整技术目标。优先使用 `cms-project-governance` 的目标发现模式；如果没有安装，每轮最多询问三个会影响结果、风险或成本的问题，并为可逆的不确定项推荐默认方案。

## 权限边界

在受治理项目中：

- Owner 或 Controller 负责期望结果、Non-Goals 和重大决策；
- Controller 负责规模、阶段计划和工单范围；
- Developer 或执行 Agent 负责实现、执行状态和证据；
- QA 负责验收。

不能从聊天、日志、状态备注或实现便利中扩大范围。受治理工作完成实现后，只能设置 `execution_state: Ready for Review`，不能自行签署 QA 或项目验收。

只有 Lite 独立任务明确设置 `qa_required: false`，且修改低风险、可回退、自动和功能验证都通过、没有 Owner 门禁时，同一个 Agent 才能自验收。

## 必需状态

推荐的 v2 状态文件：

- `Docs/ACTIVE_PACKET.md`
- `Docs/LOOP_RUNS.jsonl`

明确的独立任务可使用：

- `{baseDir}/templates/zh-CN/ACTIVE_PACKET.md`
- `{baseDir}/templates/zh-CN/LOOP_RUNS.example.jsonl`

旧项目的 `TARGET.md`、`ACCEPTANCE.md`、`WORK_ORDER.md`、`LOOP_STATE.md`、`STATUS.md`、`NEXT_ACTIONS.md`、`PENDING.md`、`EVALUATION.md` 和 `LOOP_RUNS.jsonl` 可以继续读取，不强制立即迁移。参见 `{baseDir}/references/zh-CN/migration.md`。

文件发生冲突时，设置 `execution_state: Invalid State` 并停止。权限优先级：

```text
Owner 已批准的 TARGET / Non-Goals
  -> ACCEPTANCE
  -> 当前 WORK_ORDER
  -> ACTIVE_PACKET
  -> 日志、状态、下一步和聊天
```

## 阶段与循环

每个已授权目标最多十个阶段：

| 规模 | 单阶段上限 | 复核边界 |
| --- | ---: | ---: |
| Small | 30 分钟 | 5 小时 |
| Medium | 60 分钟 | 10 小时 |
| Large | 120 分钟 | 20 小时 |

阶段是有时间上限的成果检查点；Loop 是阶段内部的一次“实现—验证—评估”循环。不能为每个阶段或 Loop 创建一份文件。

第 3、6、10 阶段结束时进行正式方向对齐。执行 Agent 提供用户价值、目标关联和证据，Controller 或 Owner 决定重大方向变化。

第 10 阶段必须停止并返回以下之一：

- `Ready for Review`
- 带有界修复项的 `Needs Fix`
- `Blocked`
- `Locally Compliant, Globally Misaligned`
- 拆分或重基线建议

不能静默开始下一组十个阶段。

## 单次 Loop

```text
读取当前 Active Packet
  -> 确认阶段目标和唯一下一步
  -> 只检查相关代码与证据
  -> 实现最小而完整的修改
  -> 运行针对性自动验证
  -> 运行功能或用户流程验证
  -> 检查差异与风险
  -> 更新状态并追加一条 Loop 记录
  -> 继续、送审、修复或停止
```

详细规则见 `{baseDir}/references/zh-CN/execution-loop.md`。

默认规则：

- 始终只保留一个立即下一步；
- 优先交付用户可感知的垂直切片；
- 不顺手清理无关代码；
- 可行时先复现缺陷再修复；
- 验证失败后先诊断，再扩大修改；
- 连续两次核心验证失败且没有新进展证据时停止；
- 修复后重跑受影响回归；
- 不能用耗时、文件数或代码量证明完成。

## 证据门禁

没有证据就不能完成。

至少需要两类证据：

1. 自动证据：测试、类型检查、构建、lint、静态检查、Schema 验证等；
2. 功能证据：真实命令、API、浏览器流程、产物检查、用户工作流或目标环境 smoke。

自动证据与功能证据冲突时，以较差结果为准。构建成功不能覆盖用户流程失败。

声明 `Ready for Review`、独立完成或带风险完成前，读取 `{baseDir}/references/zh-CN/evidence-and-completion.md`。

## 状态写回

每个 Loop 结束时：

1. 更新 `execution_state`；
2. 只有阶段成果完成或正式放弃时才推进阶段编号；
3. 更新验收项与简短证据链接；
4. 保留阻塞、假设和决策；
5. 保持一个下一步；
6. 向 `Docs/LOOP_RUNS.jsonl` 追加一条 JSON 记录。

不要把同一状态复制到多个文件。不要保存大日志、完整聊天、密钥、隐私数据或隐藏推理。

## 停止门禁

以下情况必须先停止：

- 密钥、凭据、OAuth 会话或账号登录；
- 生产数据或未脱敏客户数据；
- 付费外部资源或生产部署；
- 系统级安装、管理员权限、驱动或主机配置；
- 破坏性 Git、历史重写、删除、迁移、覆盖或不可逆操作；
- 技术栈替换或受保护架构变化；
- 与 Target 或 Non-Goals 冲突；
- 缺少决策权限；
- 阶段、失败或上下文预算耗尽。

项目规则可以更严格，配置开关不能绕过硬停止。参见 `{baseDir}/references/zh-CN/safety-and-context.md`。

## 自动化与多 Agent

外层 Runner 可以重复启动单次 Loop，但必须：

- 每次从磁盘重新读取状态；
- 使用单写锁；
- 遇到非 Continue 状态立即停止；
- 执行时间、阶段和失败预算；
- 不能自动替人批准；
- 原始日志与精简 Docs 状态分开保存。

多个 Agent 不能并发写同一 Active Packet 或日志。参见 `{baseDir}/references/zh-CN/automation-and-handoff.md`。

## 可选校验器

环境有 Node.js 时，可只读检查状态：

```text
node {baseDir}/scripts/validate-loop-state.mjs --workspace <项目路径>
```

使用 `--json` 输出机器可读结果。校验器通过只代表状态一致，不代表产品正确。

## 用户报告

每个用户可感知的工作周期结束后报告：

```text
执行状态：
阶段：
与目标的关联：
已完成工作：
自动验证：
功能验证：
风险或阻塞：
修改文件：
下一步：
需要的治理或 QA 动作：
```

当前权限不允许时，不得声称项目已验收。


# 治理档位与文件

选择足以控制风险的最轻档位。文件数量不是严谨程度。

## Lite

用于 Small、可回退、可直接验收且不需要独立 QA 的工作。

必需：

- `Docs/ACTIVE_PACKET.md`
- `Docs/LOOP_RUNS.jsonl`

目标、范围、验收、阶段、证据摘要和下一步保存在 Active Packet。只有 `qa_required: false`、自动和功能证据都通过、且不涉及 Owner 门禁时，独立 Agent 才能自验收。

不要创建 Program、Dispatch、每阶段 Handoff、状态日志或独立 QA 文件。

## Standard

用于 Medium、重要用户流程、中等不确定性或需要独立评估的工作。

必需：

- `Docs/ACTIVE_PACKET.md`
- `Docs/LOOP_RUNS.jsonl`
- 一份 `Docs/QA_DECISION_{ID}.md`

只有确实承载稳定权威信息时才选用：

- `Docs/TARGET.md`
- `Docs/ACCEPTANCE.md`
- 一份合并的 `Docs/WORK_ORDER_{ID}.md`

除非负责人、依赖、回退或验收边界不同，不拆分 Work Order。

## Full

用于 Large、高风险、多 Agent、架构、迁移、生产、安全、数据完整性或 Release 工作。

按需必需：

- `Docs/TARGET.md`
- `Docs/ACCEPTANCE.md`
- `Docs/ACTIVE_PACKET.md`
- `Docs/PROGRAM_{ID}.md`
- 有顺序的 `Docs/WORK_ORDER_{ID}.md`
- `Docs/LOOP_RUNS.jsonl`
- 独立 `Docs/QA_DECISION_{ID}.md`
- 记录 Owner 决策与风险债务的 `Docs/DECISIONS.md`

只有真实权限边界才建立独立 Handoff 或 Rebaseline 文件。

## 创建文件测试

至少满足一项才建立新文件：

- 新权限或负责人边界开始；
- 独立 QA 决策需要持久化；
- Owner 决策改变授权；
- 跨 Agent/团队无法仅用 Active Packet 交接；
- 正式 Target 重基线已批准；
- 当前规范文件达到归档阈值。

否则更新规范文件。

## 防止文档膨胀

- 一个事实只有一个权威位置；
- 链接日志和产物，不复制到多个 Markdown；
- `ACTIVE_PACKET.md` 保持约 200 行以内；
- 只保留一个立即下一步；
- 按 Release 或月份归档已关闭工作；
- 日常阶段记录不写进 `TARGET.md` 或 `ACCEPTANCE.md`；
- 测试失败或修复不能建立新 Milestone；
- 不重复维护内容相同的 status、pending、next action 和 evaluation。

## 旧项目兼容

现有 `STATUS.md`、`NEXT_ACTIONS.md`、`PENDING.md`、`COMPLETED.md`、`EVALUATION.md`、Handoff 和 Milestone 历史可以保留，但只作为兼容输入；除非审计或监管流程要求，不再同时扩展全部文件。

采用 v2：

1. 建立一份当前 Active Packet；
2. 链接已有权威 target、acceptance 和 Work Order；
3. 把过时或冲突文件标记为归档，不改写历史；
4. 新执行证据写入 `LOOP_RUNS.jsonl`。


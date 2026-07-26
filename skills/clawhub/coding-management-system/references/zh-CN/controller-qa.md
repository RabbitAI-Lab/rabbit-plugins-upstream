# Controller 与 QA

计划权限、实现权限和验收权限必须分开。

## Dispatch

Dispatch 前：

1. 确认 Goal Readiness 是 `Ready for Execution`；
2. 确认规模和治理档位；
3. 创建或更新 Active Packet；
4. 写明允许范围、受保护边界、验收标准、证据和停止条件；
5. 设置 `execution_state: Ready`、`qa_decision: Not Reviewed` 和第一阶段成果。

Developer 可以不在每个 Loop 后询问而继续执行已授权阶段，但必须满足：

- 下一步仍在同一 Packet 内；
- 证据显示有效进展；
- 没有停止规则或 Owner 门禁；
- 对齐仍是 `Aligned`；
- 重复失败未达到上限。

Developer 可以设置 `execution_state: Ready for Review`，但 Standard 或 Full 中不能修改 QA 或项目验收。

## 最新交付审查

只检查：

- Active Packet 和当前 Work Order；
- 最新交付修改的文件；
- 该交付影响的验收标准；
- 提交的证据；
- 必需的回归范围。

不能把最新交付审查变成全项目审计。

检查：

1. 是否保持授权范围；
2. Non-Goals 和受保护边界是否完整；
3. 每个 Must Pass 是否有可复现证据；
4. 自动检查与功能/用户流程证据是否一致；
5. 跳过检查是否有明确且合理的原因；
6. 已知风险是否可追踪且确实不阻塞；
7. 结果是否仍服务用户可感知目标。

## QA 决策

- `Accepted`：Must Pass 和所需证据充分；
- `Accepted With Risk`：核心结果可用，非阻塞边缘风险明确、有负责人和时限；
- `Failed`：仍有可执行的实现或证据缺陷；
- `Blocked`：验收需要 Owner 权限、不可用环境、凭据、受保护访问或其他硬门禁。

`Accepted With Risk` 不能替代核心流程失败、主要环境缺失或功能证据缺失。

## QA 失败

1. 保持相同 Milestone 和 Work Order；
2. 设置 `qa_decision: Failed`；
3. 设置 `execution_state: Needs Fix` 和 `project_state: Needs Fix`；
4. 建立与失败标准 ID 关联的有界修复；
5. 写明重新验证和受影响回归；
6. 返回适当阶段，不能重置为新 Milestone。

使用 `{baseDir}/templates/zh-CN/QA_DECISION.md`。

## 自验收

只有 Lite 且满足以下条件才允许：

- `qa_required: false`；
- 修改局部、低风险、可回退；
- 自动和功能证据都通过；
- 没有重大已知限制；
- Active Packet 明确允许独立执行。

其他情况必须独立 QA。


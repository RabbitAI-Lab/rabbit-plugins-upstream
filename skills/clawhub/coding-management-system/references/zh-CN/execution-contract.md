# 执行合同 2.0

`Docs/ACTIVE_PACKET.md` 是治理层与执行层之间的当前授权和交接。

## 必需 Frontmatter

```yaml
---
contract_version: "2.0"
packet_id: "GOAL-001"
goal_readiness: "Ready for Execution"
project_state: "Active"
execution_state: "Ready"
alignment_state: "Aligned"
qa_required: true
qa_decision: "Not Reviewed"
size: "Medium"
governance: "Standard"
stage: 1
max_stages: 10
stage_minutes: 60
updated_at: "YYYY-MM-DDTHH:mm:ssZ"
---
```

## 必需章节

- Desired Outcome / 期望结果
- User And Situation / 用户与场景
- Current Stage Outcome / 当前阶段成果
- Scope / 范围
- Non-Goals / 非目标
- Acceptance Criteria / 验收标准
- Allowed Changes / 允许修改
- Protected Boundaries / 受保护边界
- Evidence Required / 所需证据
- Stop Conditions / 停止条件
- Assumptions And Decisions / 假设与决策
- Current Evidence / 当前证据
- One Next Action / 唯一下一步

使用 `{baseDir}/templates/zh-CN/ACTIVE_PACKET.md`。

## 权限所有者

| 字段/内容 | 负责人 |
| --- | --- |
| 期望结果、Core Target、Non-Goals | Owner / 已授权 Controller |
| 规模、治理、阶段计划、Work Order 范围 | Controller |
| 执行状态、实现记录、证据链接 | Developer / 执行 Agent |
| 对齐结论 | Controller 或指定 Reviewer |
| QA 决策 | QA；只有 Lite 明确允许时可自验 |
| 项目状态 | QA 决策后的 Controller |

Agent 不能修改当前角色权限之外的字段。

## 状态转换

```text
Ready
  -> In Progress
  -> Ready for Review
  -> QA Accepted / Accepted With Risk

In Progress
  -> Needs Fix
  -> In Progress

任意活动状态
  -> Blocked
  -> 只有明确门禁解除后恢复

任意矛盾
  -> Invalid State
```

QA `Failed` 必须映射为 `execution_state: Needs Fix` 和 `project_state: Needs Fix`，不能创建新 Milestone。

## 冲突规则

Standard 或 Full 中，Active Packet 是当前投影：

```text
Owner 已批准的 TARGET / Non-Goals
  -> ACCEPTANCE
  -> 当前 WORK_ORDER
  -> ACTIVE_PACKET
  -> 日志和聊天
```

Packet 与更高权限文件冲突时，设置 `Invalid State`。

Lite 中，Active Packet 可以是唯一权限文件。

## 写入规则

- 尽可能原子更新 Packet；
- 保持一个下一步；
- 链接证据，不粘贴大日志；
- 不保存密钥、隐私数据、完整聊天或隐藏推理；
- 使用 ISO 8601 时间；
- 每个执行 Loop 向 `Docs/LOOP_RUNS.jsonl` 追加一条 JSON。

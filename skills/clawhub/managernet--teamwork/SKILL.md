---
name: "teamwork"
description: "多 Agent 团队协作规范：工作组长调度，子 agent 按 soul 选任务，审计兜底，立即 git push。"
author: Michael + Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [multi-agent, orchestration, openclaw, teamwork, side-research, serial, git-push]
    related_skills: [subagent-driven-development, team-orchestration, vault-research-workflow]
---

# Teamwork：OpenClaw 多智能体团队协作规范

## Overview

本技能规范 OpenClaw 多 agent 协作的项目执行方式。核心不是“一个 agent 做完所有事”，而是“工作组长调度、子 agent 按 soul 自选任务、审计兜底、cron 持续推进”。

## 原则性规则

### 任务分块与上下文隔离

- 建立子 agent 分别执行的目的是**避免单个任务上下文溢出**。
- 大任务必须拆成小块，按块分派；每个块只携带必要上下文，禁止把整段历史/无关文件全塞进 prompt。
- 子 agent 应只处理当前块，产出后交回工作组长汇总，再推进下一块。

### 分派与通知

- 每个任务文件必须包含可选的 `notify.dingtalk_id` 或 `notify.user_id`，用于执行结果通知人类负责人。
- 分派时不强制要求每个任务都有独立子 agent；但**当任务会显著增长上下文、需要隔离并行、或需要不同 soul 时**，应拆分子 agent。
- 工作组长读取任务后，判断是否需要再分派；若直接执行，也必须遵守分块原则。

### 通知规则补充

- 从 `team-directory.json` 按 `en` 或 `name` 字段匹配负责人 `dingtalk_id`。
- 子 agent 完成/阻塞时，工作组长负责触发钉钉通知，内容包含 `task_id`、`title`、`状态`、`产出简述`。
- 钉钉仅通知人类，不用于 agent 间通信；agent 间通信只通过 `.agent-coordination/` 文件。

## 角色定义

### side-research：工作组长/进度推手

- 不是执行型子 agent，而是**本智能体内的协调者**。
- 职责：读取 `.agent-coordination/tasks/`，按规则分发给对应子 agent，推动其执行，记录结果，发现阻塞。
- 每个 OpenClaw 智能体（technical_team、export_team 等）内部建议至少有一个 side-research。
- 触发方式：**cron 定时反复触发** 或 **项目负责人手动推进**。
- 侧线子 agent soul/IDENTITY 中应包含能力边界与任务偏好，用于自主选择。

### 子 Agent：按 soul 执行

- 子 agent 读取分配给自己的 `task-*.json`，按自身 soul/IDENTITY/能力边界选择是否承接。
- 承接后改 `status: in_progress`，写 `updated_at` 与 `audit`。
- 完成后写回 `result`，改 `status: completed`，并 **自行 `git add -A && git commit -m "<agent名> <产品>: <产出简述>" && git push`**。
- 阻塞时改 `status: blocked`，在 `result.error` 写明原因与建议。

### 项目审计：兜底编排

- 审计角色扫描 `.agent-coordination/tasks/`，识别长期 `pending` 任务。
- 若原分配 agent 无法承接或已超时，审计有权修改 `assigned_to`、调整依赖、拆分任务后重新分发。
- 审计发现异常时通知人类（钉钉/邮件），但**不代替 agent 执行**。

### 项目负责人：编排与确认

- 创建初始任务文件，指定 `assigned_to` 与 deadline。
- 通过 `.agent-coordination/` 协议下发，不在会话中口头派活。
- 定期查看 Gitee 提交记录与任务状态文件，确认执行进度。

## 任务协议：`.agent-coordination/`

所有任务交接必须通过目录文件完成，禁止会话假设。

```
.agent-coordination/
├── SCHEMA.md
├── tasks/             # task-<id>.json
├── archive/           # 已完成/取消
├── scratch/           # 临时产物
└── README.md
```

任务 JSON 关键字段：
- `status`: `pending | in_progress | completed | blocked | cancelled`
- `assigned_to`: `agent名` 或 `agent1+agent2`
- `deadline`: ISO8601
- `payload.product`: `P1-P8 | T1-T7 | ...`
- `result.status`: `success | partial | failed | skipped`
- `audit[]`: 操作记录

## 执行铁律

1. **串行单跑**：同一时刻只跑 1 个侧线子 agent，轮次间隔 >=5h。并发触发 = 429 风险。
2. **立即推送**：Michael 看 Gitee，不看本地文件。未推送 = 未完成。
3. **提交格式**：`<agent名> <产品>: <产出简述>`
4. **单目录待确认**：所有需人工确认事项集中 `待Michael人工确认/`，完成后立即移入 `archive/`。
5. **子 agent 真实执行**：不能只写 `.agent-coordination/tasks/*.json` 就标记 completed；必须通过 heartbeat/cron 实际读取并执行。
6. **父级不自写自判**：父级/协调者不能代替子 agent 标记 completed。

## 触发与调度

### Cron 规则

- 建议触发点：`03:00 / 08:00 / 13:00 / 18:00 / 23:00`（明确到小时）
- 脚本：`.agent-coordination/scripts/side_research_run.sh`
- 脚本行为：
  - 读取 `tasks/` 下 `status=pending` 且 `scheduled_at <= 现在` 的任务
  - 按 `assigned_to` 分发到对应 agent
  - 检查执行输出关键字：`执行记录已写入|执行记录已更新|已完成`
  - 成功 → `completed`；429/timeout → `retry` + `next_retry`；其他 → `needs_review`
  - 任务间间隔 300s

### 手动推进

当 cron 不够及时时，项目负责人可直接调用脚本或分派单任务。

## 项目审计流程

1. 扫描 `tasks/`，识别 `pending` + `deadline 已过` 或 `needs_review > 24h`
2. 检查 `audit` 与 `result.error`
3. 调整 `assigned_to`、`deadline`、`dependencies`
4. 若阻塞原因明确，记录后通知人类
5. 更新 `updated_at` 并追加 `audit` 记录
6. 待下次 cron 或手动触发时重新分发

## 人类干预

- 通知渠道：钉钉 `dingtalk:<dingtalk_id>`
- 通知内容：`task_id`、`title`、`当前状态`、`需要什么决策/输入`、`deadline`
- 每次通知追加 `audit: human_escalation`
- 禁止在通知中暴露密钥/token

## Common Pitfalls

- 把 side-research 当成执行 agent：它只调度，不干活。
- 任务文件创建后无 cron 跟进：pending 永远不变。
- 并发派发多个子 agent：立刻触发 429。
- 子 agent 自写自判 completed：必须由执行者或脚本客观记录。
- commit message 不规范：缺少 agent 名或产品标识，无法追溯。

## Verification Checklist

- [ ] 每个智能体内至少有一个 side-research agent
- [ ] 每个子 agent 有 SOUL.md / IDENTITY.md 声明能力边界
- [ ] `.agent-coordination/tasks/` 下任务 `status` 真实反映执行情况
- [ ] 子 agent 成果已 `git add -A && git commit -m '<agent> <产品>: <产出>' && git push`
- [ ] Gitee 可见最新提交；未推送 = 未完成
- [ ] `待Michael人工确认/` 目录为空或内容已过时
- [ ] cron 已明确到小时，无“明天”模糊表述
- [ ] side_research_run.sh 能按 `assigned_to` 分发到真实子 agent

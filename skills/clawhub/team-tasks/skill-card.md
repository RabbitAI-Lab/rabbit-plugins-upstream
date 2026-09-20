## Description:

在用户明确要求管理团队任务台账或调用 team-tasks 时，提供本地 JSON 任务存储、更新、评论、归档、备份、受限恢复、提醒风险解析和可重试的提醒同步事件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[djoldwang](https://clawhub.ai/user/djoldwang)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external teams, developers, and integration maintainers use this skill to manage a shared local team-task ledger, generate task status views or exports, and coordinate reminder scheduling through trusted external adapters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task records, history, reminder receipts, and backups persist in the configured local data directory.

Mitigation: Deploy only to a trusted local-only directory with appropriate filesystem ownership and permissions, and account for retained backups during data handling and review.

Risk: The storage scripts do not authenticate users or authorize notification recipients.

Mitigation: Require a trusted adapter or integration layer to enforce team identity, business permissions, notification authorization, and delivery target validation before invoking the skill.

Risk: Reminder text is user-facing and currently Chinese-only.

Mitigation: Use this release where Chinese reminder output is acceptable, or add a reviewed localization layer before broader deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/djoldwang/skills/team-tasks)
- [安全存储接口与接入步骤](artifact/references/storage.md)
- [调度适配器契约](artifact/references/reminder-adapters.md)
- [OpenClaw 可选适配](artifact/references/openclaw.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell command examples, and text, JSON, or CSV task exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local task-ledger operations and reminder-planning guidance; actual notification delivery and authorization remain with trusted external adapters.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

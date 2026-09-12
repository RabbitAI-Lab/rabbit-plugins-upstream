## Description:

Chronos is a lightweight recurring-task engine for OpenClaw that manages scheduled tasks, reminders, monthly quotas, overdue completion, and legacy todo migration through a unified command interface.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mathlife](https://clawhub.ai/user/mathlife)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Chronos to create, list, complete, skip, and inspect recurring or one-shot scheduled work in an OpenClaw workspace. It is especially useful when reminders, monthly completion quotas, cron-backed notifications, and conservative migration of legacy todo rows need to be managed from agent-accessible shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reminder delivery or cron actions may affect the wrong OpenClaw workspace or chat if configuration is not reviewed.

Mitigation: Confirm the intended workspace and CHRONOS_CHAT_ID before installing or running reminder-related commands.

Risk: Migration, archive, cleanup, and overdue-completion commands can modify local scheduling state and legacy todo rows.

Mitigation: Run schema checks and dry-run modes first, then apply changes only after reviewing the planned operations.

Risk: System tasks using special_handler can execute documented Meta-Review or subagent-memory synchronization behavior and persist audit notes in workspace memory.

Mitigation: Review system tasks that use special_handler before enabling complete-overdue automation.

## Reference(s):

- [Chronos README](artifact/README.md)
- [Chronos changelog](artifact/CHANGELOG.md)
- [Chronos ClawHub listing](https://clawhub.ai/mathlife/skills/chronos)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and shell-command guidance for managing local task and reminder state]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command examples that read or update local Chronos database, cron, configuration, and workspace memory state.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

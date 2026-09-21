## Description:

团队任务管家 helps agents maintain a local JSON team-task ledger, produce Chinese-language task and reminder outputs, and emit retryable reminder-sync events for trusted external adapters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[djoldwang](https://clawhub.ai/user/djoldwang)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and their trusted agent adapters use this skill to create, update, query, export, archive, and reopen shared tasks in a local ledger. It also supports reminder analysis and synchronization contracts while leaving scheduling, notification delivery, identity checks, and business permissions to the integrating system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scripts do not authenticate team members or enforce business permissions.

Mitigation: Run the skill only behind a trusted adapter that verifies identity and permissions before invoking task operations.

Risk: The skill writes local ledger, lock, transaction, backup, and recovery files.

Mitigation: Grant write access only to the configured local data directory and require callers to use the bundled storage scripts.

Risk: The skill does not schedule jobs or send notifications itself.

Mitigation: Keep scheduler, notification, network, and credential authority in a separate adapter that re-reads current task state before delivery.

Risk: Built-in user-facing messages are Chinese-language templates.

Mitigation: Use an adapter-level localization layer when teams need another display language.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/djoldwang/skills/team-tasks)
- [安全存储接口](artifact/references/storage.md)
- [调度适配器契约](artifact/references/reminder-adapters.md)
- [OpenClaw 可选适配](artifact/references/openclaw.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Shell commands, Configuration, Guidance]

**Output Format:** [Chinese-language task summaries, structured JSON or CSV exports, Markdown guidance, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are derived from the local task ledger and reminder analysis; notification delivery is handled by external adapters.]

## Skill Version(s):

1.4.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

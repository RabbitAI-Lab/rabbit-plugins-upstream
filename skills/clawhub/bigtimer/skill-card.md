## Description:

BigTimer manages recurring cron-style tasks and message delivery across OpenClaw and DSH environments, with support for adding, listing, removing, testing, installing, and running scheduled shell-command tasks that can send results through OpenClaw messages, Feishu webhooks, or stdout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure, test, and install recurring task runs that execute shell commands and push their output to messaging destinations. It is suited for scheduled scans, reminders, reports, and integrations with other agent skills that need periodic message delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store recurring shell commands and install them into cron-like schedulers.

Mitigation: Review every scheduled action before installation, run cron-gen first, and install only tasks whose command behavior and working directory are understood.

Risk: Command output can be forwarded to OpenClaw messages or Feishu webhooks, which may expose sensitive results.

Mitigation: Prefer stdout or trusted delivery targets for sensitive output, and verify webhook, channel, and target settings before running or installing tasks.

Risk: Removing a saved task does not necessarily remove already installed scheduler entries.

Mitigation: Manually audit and remove crontab or OpenClaw cron entries after deleting tasks.

## Reference(s):

- [BigTimer ClawHub skill page](https://clawhub.ai/kobenfang/skills/bigtimer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates task and log files under workspace memory; DSH install mode can write crontab entries.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

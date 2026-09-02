## Description:

BigTimer manages scheduled cron tasks and message delivery across OpenClaw and DSH environments, including task creation, listing, removal, status checks, immediate runs, schedule generation, and Feishu or multi-channel push delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create, inspect, run, and install scheduled jobs that can send command output through OpenClaw messaging, Feishu webhooks, or stdout. It is suited for recurring reports, reminders, scans, and other trusted automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled tasks can persistently run arbitrary shell commands.

Mitigation: Only schedule commands and working directories that are fully trusted, and inspect generated cron or OpenClaw scheduler entries before installation.

Risk: Task output can be sent externally through Feishu webhooks or OpenClaw messaging.

Mitigation: Use stdout or scoped OpenClaw delivery for sensitive output, and verify push destinations before running or installing tasks.

Risk: Removing a task from the skill state does not remove an already installed system scheduler entry.

Mitigation: Manually remove matching crontab or OpenClaw scheduler entries when retiring a task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/bigtimer)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON command responses and Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write task state and logs under the workspace memory directory and may install scheduler entries in supported environments.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

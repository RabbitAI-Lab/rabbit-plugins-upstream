## Description:

Include Inbox tasks and habits in complete TickTick Today queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alexarevalo9](https://clawhub.ai/user/alexarevalo9)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate TickTick through the TickTick CLI, including task creation, updates, completion, Today views, and habit status checks. It is especially focused on complete Today queries that include Inbox tasks and habits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The TickTick CLI uses a full-access TickTick token for task and habit data.

Mitigation: Keep the token private, avoid echoing or logging it, and install only when full TickTick task and habit access is acceptable.

Risk: Task deletion and bulk task changes can remove or alter user planning data.

Mitigation: Confirm destructive deletes and multi-task changes with a numbered preview before running the CLI command.

Risk: Unquoted user task titles can become executable shell syntax when interpolated into commands.

Mitigation: Single-quote user-supplied text in shell commands and escape embedded single quotes before execution.

Risk: Today summaries can omit Inbox tasks or habits if project filtering is used incorrectly.

Mitigation: Query Today without a project restriction and report habit check-in status separately from task counts.

## Reference(s):

- [TickTick homepage](https://ticktick.com)
- [TickTick ClawHub skill page](https://clawhub.ai/alexarevalo9/skills/ticktick)
- [TickTick CLI reference](artifact/references/cli-reference.md)
- [Setup, install, auth, and OpenClaw wiring](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON CLI output for parsing and returns short plain-text task updates suitable for Telegram.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

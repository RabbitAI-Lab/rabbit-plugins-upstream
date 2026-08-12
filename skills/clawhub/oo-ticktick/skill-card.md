## Description:

Operate TickTick through an OOMOL-connected account for reading, creating, updating, completing, moving, and deleting tasks, projects, and habits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage TickTick projects, tasks, completed tasks, filtered task views, and habits through an OOMOL-connected TickTick account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions can expose TickTick task, project, completed-task, filtered-task, and habit data.

Mitigation: Use read actions only for user-requested TickTick data and avoid displaying unnecessary personal task details.

Risk: Write actions can alter TickTick projects, tasks, and habit check-ins.

Mitigation: Confirm the exact action, target, and payload with the user before running write actions.

Risk: Destructive actions can delete TickTick projects or tasks.

Mitigation: Require explicit user approval for the exact project or task before deleting it.

Risk: The skill uses OOMOL as an intermediary for a connected TickTick account.

Mitigation: Confirm the user is comfortable with OOMOL-connected account handling before installation and use.

## Reference(s):

- [TickTick homepage](https://ticktick.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [TickTick ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ticktick)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON responses containing connector data and execution metadata when run with --json.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

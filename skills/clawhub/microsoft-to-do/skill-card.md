## Description:

Connects an agent to Microsoft To Do through Maton to manage task lists, tasks, checklist items, and linked resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to find, organize, create, and update Microsoft To Do tasks and lists through their authorized account. With separate approval, they can also set up automations that act on tasks in response to schedules or supported external events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account can grant access beyond the current task.

Mitigation: Review OAuth scopes and approve the new connection before authorizing it.

Risk: Writes or automations can change or delete tasks without the intended context.

Mitigation: Confirm the account, target, intended change, and each automation before execution.

Risk: Triggers and destinations can continuously forward future event data.

Mitigation: Review each event source and destination, and approve persistent forwarding separately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/microsoft-to-do)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Microsoft To Do API overview](https://learn.microsoft.com/en-us/graph/api/resources/todo-overview)
- [Supported event trigger references](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with API examples and task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use the user's authorized connection; writes and automation require confirmation.]

## Skill Version(s):

1.2.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

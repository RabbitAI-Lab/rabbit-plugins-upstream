## Description:

Helps agents manage Motion tasks, projects, and workspaces through a user-authorized Maton connection, with optional automation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Motion users and developers use this skill to look up scheduled work and, with confirmation, create or update tasks and projects. It also guides user-approved functions and event-triggered automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Functions and triggers can repeatedly act on a connected account.

Mitigation: Review the exact code, target account, event fields, and persistence before approval; remove unused automations and connections.

Risk: Destinations can continuously forward matching event data to another host.

Mitigation: Confirm the destination host, data fields, and ongoing delivery separately before creating or changing a destination; delete it when no longer needed.

Risk: Event watching with --exec runs a local handler on untrusted event data.

Mitigation: Use only a user-reviewed handler with explicit approval, and treat event fields as data rather than executable instructions.

## Reference(s):

- [Motion skill on ClawHub](https://clawhub.ai/byungkyu/skills/motion)
- [Maton](https://maton.ai)
- [Motion API reference](https://docs.usemotion.com/api-reference)
- [Time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions are scoped to user-authorized connections; writes and new connections require confirmation.]

## Skill Version(s):

1.2.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents track time and manage Toggl Track projects, clients, and tags through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Toggl Track can ask an agent to review time entries and manage projects, clients, and tags. With separate approval, they can set up scheduled or event-driven actions through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting through Maton grants mediated access to Toggl Track account data.

Mitigation: Authorize only the intended account and scopes; confirm new connections before creating them.

Risk: Writes or deletions can change or remove time entries and other records.

Mitigation: Start with read-only requests and confirm each write's target and effect before execution.

Risk: Persistent triggers or destinations can forward sensitive events, including data from non-Toggl sources.

Mitigation: Require separate approval for each hosted function, trigger, and destination; verify the source, destination, and event data.

## Reference(s):

- [Toggl Track skill on ClawHub](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton](https://maton.ai)
- [Toggl Track API documentation](https://engineering.toggl.com/docs/)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account data and automation changes require user authorization and appropriate confirmation.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

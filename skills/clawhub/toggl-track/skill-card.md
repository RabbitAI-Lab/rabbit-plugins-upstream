## Description:

Guides agents in using Toggl Track to manage time entries, projects, clients, and tags through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to read and manage their Toggl Track time entries, projects, clients, and tags, with approval before connecting accounts or changing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account connections and changes to time entries or other records can grant access or modify user data.

Mitigation: Confirm each new connection and every write with the user; identify the target account, resource, and intended change first.

Risk: Hosted functions, triggers, destinations, and local event handlers can run persistently or forward data.

Mitigation: Require explicit approval of the exact code, destination URL, data fields, persistence, and deletion plan before enabling automation; avoid local event execution unless the user supplies and approves its handler.

## Reference(s):

- [Toggl Track skill on ClawHub](https://clawhub.ai/byungkyu/skills/toggl-track)
- [Maton homepage](https://maton.ai)
- [Toggl Track API documentation](https://engineering.toggl.com/docs/)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Text and Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API results depend on the user's authorized Toggl Track connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

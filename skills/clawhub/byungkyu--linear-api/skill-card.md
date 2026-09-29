## Description:

Helps agents query and manage Linear issues, projects, teams, cycles, labels, and comments through a managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to look up Linear work and, with explicit approval, create or update issues and other tracked resources. It also documents optional automations for approved Linear workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unapproved changes to Linear resources or connection permissions.

Mitigation: Default to read and list operations; confirm each write and new connection with the user.

Risk: Hosted functions, triggers, and destinations can run code, manage secrets, or forward events persistently.

Mitigation: Treat each automation action as separate and high impact; review its code, destination, data flow, and persistence before approving it.

Risk: Local event handlers may execute against untrusted event data.

Mitigation: Use local event execution only with a user-reviewed handler and separate explicit approval.

## Reference(s):

- [ClawHub Linear skill release](https://clawhub.ai/byungkyu/skills/linear-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Linear GraphQL documentation](https://linear.app/developers/graphql)
- [Linear trigger reference](references/linear/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with CLI commands and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the authorized Linear connection; writes require explicit approval.]

## Skill Version(s):

1.2.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

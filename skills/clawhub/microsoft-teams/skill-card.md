## Description:

Helps agents manage Microsoft Teams teams, channels, messages, and meetings through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams users and developers use this skill to find teams and channels, read messages, send approved updates, schedule meetings, and retrieve meeting information. It also describes optional user-approved automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Microsoft Teams data is accessed through Maton.

Mitigation: Use only if the user is comfortable with Maton as a gateway, and obtain approval for each new connection.

Risk: Writes, hosted functions, and triggers can change Teams data or automate actions.

Mitigation: Confirm each write, hosted function, and trigger separately before proceeding.

Risk: Trigger destinations may forward data to third-party services.

Mitigation: Approve each destination separately and avoid third-party destinations unless the forwarded data is understood.

Risk: A local event handler can execute code on incoming events.

Mitigation: Do not use --exec unless the local handler script has been reviewed and its execution approved.

## Reference(s):

- [Microsoft Teams skill on ClawHub](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Microsoft Teams API overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API reference](https://learn.microsoft.com/en-us/graph/api/overview)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can contain Microsoft Teams data; show only details needed for the user's task.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

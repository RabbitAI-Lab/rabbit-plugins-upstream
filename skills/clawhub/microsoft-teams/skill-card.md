## Description:

Microsoft Teams API integration with managed OAuth for managing teams, channels, messages, meetings, recordings, and transcripts through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to work with Microsoft Teams accounts via Maton OAuth, including listing teams and channels, sending messages, scheduling meetings, and retrieving meeting recordings or transcripts. It is best suited for Teams administration and collaboration workflows where read operations are preferred and writes require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw Microsoft Graph passthrough may reach beyond the Teams operations a user expects.

Mitigation: Review the skill before installation, avoid raw `maton api` calls to non-Teams Microsoft Graph resources unless explicitly trusted, and prefer typed Teams commands for routine work.

Risk: OAuth scopes and account selection can expose broader access or target the wrong Teams connection.

Mitigation: Use read-only OAuth scopes where possible, specify the intended connection when multiple connections exist, and revoke unused connections.

Risk: Write operations such as sending messages, creating channels, scheduling meetings, or deleting resources can affect users and Teams data.

Mitigation: Default to read and list operations first, then confirm the exact target, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Teams API Overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI commands, API paths, JSON examples, and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Microsoft Teams OAuth connection; typed commands and raw API calls may return JSON responses.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

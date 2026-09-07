## Description:

Microsoft Teams API integration with managed OAuth for managing teams, channels, messages, meetings, recordings, and transcripts through Microsoft Graph API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access Microsoft Teams data and perform Teams actions through managed OAuth, including listing teams and channels, sending messages, scheduling meetings, and retrieving meeting artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton acts as the OAuth and API gateway for the connected Microsoft Teams account.

Mitigation: Confirm trust in Maton before installation and grant only the Microsoft scopes needed for the task.

Risk: Write actions can send messages, change meetings, delete channels, or revoke connections.

Mitigation: Review the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Raw API passthrough can reach authorized Microsoft Graph endpoints beyond the documented examples.

Mitigation: Restrict passthrough calls to the current task and review sensitive endpoints before execution.

Risk: Teams responses may include personal data, messages, recordings, transcripts, or meeting details.

Mitigation: Extract only the fields needed for the task and avoid logging or storing raw responses unless explicitly required.

## Reference(s):

- [Microsoft Teams skill page](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Maton homepage](https://maton.ai)
- [Microsoft Teams API overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Maton docs](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Microsoft Teams connection.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

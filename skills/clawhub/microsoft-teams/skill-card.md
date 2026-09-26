## Description:

Microsoft Teams API integration with managed OAuth for listing teams, creating channels, sending messages, scheduling meetings, and accessing meeting recordings and transcripts through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Microsoft Teams data and Microsoft Graph actions through Maton-managed authentication. It supports read-first workflows and user-approved writes for teams, channels, messages, meetings, recordings, transcripts, and related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide access to Microsoft Teams business data through a connected Maton account.

Mitigation: Use OAuth, grant only task-required scopes during authorization, and confirm that the user is comfortable with the Teams data access before installing or connecting.

Risk: Write actions, new connections, functions, and triggers can change Teams state or create ongoing automation.

Mitigation: Confirm every write or automation setup with the user, summarize least-privilege access before execution, and delete unused connections, functions, and triggers when work is complete.

Risk: Long-lived API keys and third-party trigger destinations can increase credential or data exposure.

Mitigation: Prefer OAuth over API keys and keep trigger destinations on Maton-controlled hosts unless the user explicitly approves another host.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Maton Homepage](https://maton.ai)
- [Microsoft Teams API Overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Channel Resource](https://learn.microsoft.com/en-us/graph/api/resources/channel)
- [ChatMessage Resource](https://learn.microsoft.com/en-us/graph/api/resources/chatmessage)
- [Team Resource](https://learn.microsoft.com/en-us/graph/api/resources/team)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated Maton or Microsoft Graph API call patterns that require user approval before writes, connection creation, or automation setup.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

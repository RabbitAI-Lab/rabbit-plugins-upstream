## Description:

Microsoft Teams API integration with managed OAuth for managing teams, channels, messages, meetings, recordings, and transcripts through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to inspect and manage Microsoft Teams resources through Microsoft Graph, including teams, channels, messages, chats, meetings, recordings, and transcripts. It is suited to agent-assisted Teams administration and communication tasks where OAuth authorization, least-privilege access, and explicit confirmation for writes are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Microsoft Graph passthrough access with write-capable actions can send messages, create or update resources, schedule meetings, or delete Teams data through the connected account.

Mitigation: Review requested OAuth scopes, prefer read-only access, avoid generic Graph passthrough unless needed, and confirm every send, update, delete, meeting, or connection action with the exact target and payload.

Risk: OAuth tokens, API keys, and provider-issued credentials can expose Microsoft Teams or Microsoft Graph access if printed, persisted, or passed to untrusted hosts.

Mitigation: Use managed OAuth where possible, keep credentials in the operating system credential store, never inspect or export token values, and revoke unused connections after the task.

Risk: Teams messages, comments, transcripts, and other API responses may contain untrusted content that attempts to influence follow-up actions.

Mitigation: Treat fetched Teams content as data, validate identifiers before acting, and do not execute or interpolate API response content into shell commands or prompts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Teams API Overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Channel Resource](https://learn.microsoft.com/en-us/graph/api/resources/channel)
- [Microsoft Graph ChatMessage Resource](https://learn.microsoft.com/en-us/graph/api/resources/chatmessage)
- [Microsoft Graph Team Resource](https://learn.microsoft.com/en-us/graph/api/resources/team)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON/API request snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, OAuth or API-key authentication, and explicit user confirmation for connection creation and write operations.]

## Skill Version(s):

1.2.0 (source: release evidence; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

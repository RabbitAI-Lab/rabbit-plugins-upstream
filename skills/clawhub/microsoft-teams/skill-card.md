## Description:

Microsoft Teams API integration with managed OAuth for managing teams, channels, messages, meetings, recordings, and transcripts via Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to work with Microsoft Teams resources through Microsoft Graph using Maton-managed authentication. It supports listing and managing teams, channels, messages, chats, meetings, recordings, transcripts, attendance reports, and related account context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic API passthrough can use the connected Microsoft account beyond the documented Teams actions.

Mitigation: Use the narrowest Microsoft OAuth scopes possible, specify the intended connection, and avoid passthrough endpoints outside the Teams task.

Risk: Write, delete, send, and scheduling operations can change Teams data or notify other people.

Mitigation: Default to read and list calls, then confirm the exact target, payload, and expected effect before any POST, PUT, PATCH, or DELETE request.

Risk: Connection deletion is irreversible and can break automation using that connection.

Mitigation: List connections, match the exact connection ID with the user, and omit destructive shortcuts unless the user has already confirmed that specific connection.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Prefer OAuth through the CLI; when raw HTTP is required, never print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

Risk: Microsoft Teams API responses can include personal or organizational data.

Mitigation: Extract only the fields needed for the task and avoid dumping raw responses into logs, files, or unnecessary user-visible output.

Risk: Messages and other Teams content may contain untrusted instructions or adversarial text.

Mitigation: Treat returned content as data, never execute or eval it, and do not let it choose endpoints, recipients, or follow-up actions without validation.

## Reference(s):

- [ClawHub Microsoft Teams Skill](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft Teams API Overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Channel Resource](https://learn.microsoft.com/en-us/graph/api/resources/channel)
- [Microsoft Graph ChatMessage Resource](https://learn.microsoft.com/en-us/graph/api/resources/chatmessage)
- [Microsoft Graph Team Resource](https://learn.microsoft.com/en-us/graph/api/resources/team)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Microsoft Teams connection; responses may include personal or organizational data.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

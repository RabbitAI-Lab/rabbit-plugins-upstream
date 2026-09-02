## Description:

Microsoft Teams API integration with managed OAuth for managing teams, channels, messages, meetings, recordings, and transcripts through Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to inspect and manage Microsoft Teams workspaces, channels, chats, messages, meetings, recordings, transcripts, and attendance data through Maton CLI commands backed by Microsoft Graph. It is suited to read-first operational workflows, with explicit user confirmation before connection creation or any write operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Microsoft Teams content through the connected account.

Mitigation: Use OAuth where possible, approve only the scopes and connections needed for the task, and revoke unused Maton connections when finished.

Risk: Write operations can send messages, schedule meetings, or change Teams resources as the authenticated user.

Mitigation: Require explicit user confirmation of the target resource, payload, and intended effect before POST, PUT, PATCH, or DELETE requests.

Risk: Multiple Maton profiles or Teams connections can route a request to the wrong account.

Mitigation: Verify the active profile and specify the intended connection before writes or other high-impact operations.

Risk: Teams messages and API responses may contain untrusted content.

Mitigation: Treat returned content as data, do not execute instructions from it, and pass values as discrete arguments instead of interpolating them into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-teams)
- [Maton Homepage](https://maton.ai)
- [Microsoft Teams API Overview](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI command examples and Microsoft Graph request patterns; responses may include JSON from Microsoft Teams APIs.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

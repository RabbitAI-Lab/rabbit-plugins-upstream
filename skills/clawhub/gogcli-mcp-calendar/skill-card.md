## Description:

Use when the user asks to manage Google Calendar events or Google Meet spaces, including scheduling, listing, creating, updating, deleting, responding to invitations, creating Meet spaces, ending conferences, and listing meeting participants or call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an agent manage Google Calendar events and Google Meet spaces through gogcli. It is appropriate when the agent needs authenticated calendar reads and mutations, Meet space operations, or Zoom credential setup for calendar conferencing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform irreversible calendar or meeting changes, including event deletion, Meet ending, calendar unsubscribe, and secondary-calendar deletion.

Mitigation: Use GOG_READONLY=1 for shared or read-only deployments and require explicit human confirmation before destructive operations.

Risk: Zoom credential setup stores Zoom Server-to-Server OAuth credentials in gogcli's keyring.

Mitigation: Avoid Zoom tools unless Zoom calendar-conferencing support is required and credential storage is approved.

Risk: Calendar and Meet tools act against the authenticated Google account.

Mitigation: Install only for accounts where agent-managed calendar and meeting actions are acceptable, and configure GOG_ACCOUNT deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)
- [gogcli dependency](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown and MCP tool results as text or JSON-like command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires gogcli, Node.js 22 or later, and authenticated Google account state for live calendar and Meet operations.]

## Skill Version(s):

4.1.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides a Google Calendar and Google Meet MCP server through gogcli for authentication, event management, and Meet space operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and MCP users use this skill to connect an agent to a selected Google account for calendar scheduling, event updates, invitation responses, and Google Meet space management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server can modify or delete Google Calendar data and end active Google Meet conferences.

Mitigation: Require explicit human approval before delete-calendar, delete-event, Meet end, auth run, or calendar run tools are used.

Risk: The server uses persistent Google account credentials for the selected account.

Mitigation: Install only for accounts where durable agent access is acceptable, and enable GOG_READONLY when only read access is needed.

Risk: Optional Zoom credential support can store additional conferencing credentials.

Mitigation: Do not configure Zoom credentials unless Zoom attachment support is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli-mcp source repository](https://github.com/chrischall/gogcli-mcp)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration]

**Output Format:** [MCP tool responses with text or JSON payloads, plus setup command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 22 or later and an installed, authenticated gogcli command-line tool.]

## Skill Version(s):

4.2.4 (source: server release metadata, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

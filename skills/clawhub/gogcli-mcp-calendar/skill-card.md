## Description:

Use when the user asks to manage Google Calendar events or Google Meet spaces, including scheduling, listing events, creating, updating, deleting, responding to invitations, creating Meet spaces, ending conferences, and listing meeting participants or call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this MCP skill to let an agent interact with Google Calendar and Google Meet through gogcli. It supports account authorization, event management, invitation responses, Meet space operations, and optional Zoom meeting attachment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent access to read and change Google Calendar and Google Meet data for the configured account.

Mitigation: Install only for accounts where this access is acceptable, review the full manifest tool list before use, and set GOG_READONLY=1 for read-only deployments when possible.

Risk: The tool set includes destructive calendar and meeting actions, including deleting events, deleting owned secondary calendars, updating Meet spaces, and ending active conferences.

Mitigation: Require human review or agent approval gates before destructive actions and limit installation to trusted workspaces.

Risk: Broad command escape hatches and optional remote runner configuration can expand what the agent can execute through gogcli.

Mitigation: Avoid configuring GOG_RUNNER_URL unless the runner is trusted, and restrict agent policies around generic auth or calendar run tools.

Risk: Google OAuth tokens and Zoom Server-to-Server OAuth credentials represent sensitive persistent account access.

Mitigation: Store credentials only in trusted environments, treat them as secrets, and revoke or rotate credentials if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli project](https://github.com/openclaw/gogcli)
- [gogcli-mcp repository](https://github.com/chrischall/gogcli-mcp)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [MCP tool responses as text or JSON-like command output, with setup guidance in Markdown or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calendar, Meet, and Zoom-related results depend on the configured gogcli account, OAuth credentials, and selected tool permissions.]

## Skill Version(s):

2.29.0 (source: server release metadata, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

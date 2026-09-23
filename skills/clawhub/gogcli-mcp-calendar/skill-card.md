## Description:

Extends an agent with Google Calendar and Google Meet management tools through gogcli, including event scheduling, invitations, calendar administration, Meet spaces, and Zoom meeting attachment support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users can use this skill to let an agent manage Google Calendar events, Google Meet spaces, invitations, calendar metadata, and related Zoom meeting attachments through a local gogcli-backed MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants high-impact Google Calendar and Meet control, including delete and conference-ending actions.

Mitigation: Install only when the agent is trusted for calendar write access, and enable write or delete tools only where event deletion, calendar deletion, invitation responses, or Meet termination are acceptable.

Risk: Some actions bypass the underlying CLI confirmation without adding a separate server-side final approval gate.

Mitigation: Use read-only operation where possible, prefer GOG_READONLY=1 for shared or read-only use, and require human review before destructive calendar or Meet actions.

Risk: The skill depends on local Google and Zoom credentials and can be pointed at a custom gog binary path.

Mitigation: Protect Google and Zoom credentials, avoid untrusted GOG_PATH values, and verify the gog executable before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli](https://github.com/openclaw/gogcli)
- [gogcli-mcp repository](https://github.com/chrischall/gogcli-mcp)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [MCP tool responses with text output and setup guidance in Markdown or JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tools may invoke gogcli against configured Google Calendar, Google Meet, and Zoom credentials.]

## Skill Version(s):

4.2.5 (source: server release metadata, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

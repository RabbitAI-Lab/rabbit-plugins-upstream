## Description:

Use when the user asks to manage Google Calendar events or Google Meet spaces, including scheduling, listing events, creating, updating, deleting, responding to invitations, creating Meet spaces, ending conferences, and listing meeting participants or call history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users connect an agent to Google Calendar, Google Meet, and optional Zoom conferencing through gogcli so it can list, create, update, delete, and respond to calendar and meeting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent write access to Google Calendar and Meet, including creating, updating, deleting, moving, responding to invitations, unsubscribing from calendars, and ending meetings.

Mitigation: Use read-only mode with GOG_READONLY=1 when write access is not needed and require explicit human confirmation before destructive or state-changing operations.

Risk: The skill can use persistent Google auth state and optional Zoom credential storage.

Mitigation: Install only for trusted accounts, review stored credentials regularly, and avoid Zoom setup unless calendar event Zoom attachment is required.

Risk: Remote runner behavior can expand where calendar and credential operations execute.

Mitigation: Keep GOG_RUNNER_URL unset unless the runner is controlled and trusted, and prefer a pinned reviewed release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Repository URL declared in artifact metadata](https://github.com/chrischall/gogcli-mcp)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [MCP tool text responses and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires gogcli authentication and may use configured Google account, gog executable path, and optional Zoom credentials.]

## Skill Version(s):

2.29.1 (source: evidence.release.version, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides a Google Calendar and Google Meet MCP server via gogcli for authentication, calendar event management, and Meet space operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to let an MCP client schedule, search, update, delete, and respond to Google Calendar events and manage Google Meet spaces through an authenticated gogcli setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad control over Google Calendar and Meet data, including creating, updating, deleting, moving, and responding to events.

Mitigation: Install only for accounts where that level of access is intended, review high-impact tool requests before approval, and use GOG_READONLY=1 when only read access is needed.

Risk: Zoom Server-to-Server OAuth credential tools can store sensitive Zoom credentials for meeting attachment workflows.

Mitigation: Configure Zoom credentials only in trusted environments and avoid exposing credential-bearing inputs, logs, or tool transcripts.

Risk: Runtime remote-runner configuration can send Google or Zoom credentials to a configured endpoint.

Mitigation: Leave remote-runner settings unset unless required, and restrict any configured remote runner to a trusted HTTPS endpoint.

Risk: Escape-hatch and destructive tools can perform unexpected calendar or Meet changes if approved without review.

Mitigation: Prefer pinned package versions and manually confirm delete, unsubscribe, end-conference, move, and escape-hatch requests before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Configuration]

**Output Format:** [MCP tool responses from gogcli, typically text or JSON-like command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or later and an authenticated gogcli setup; tool effects depend on the requested Calendar, Meet, auth, or Zoom operation.]

## Skill Version(s):

2.30.0 (source: package.json, manifest.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides an MCP server for managing Google Calendar events and Google Meet spaces through gogcli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to connect an agent to a Google account for calendar event management, invitation responses, Meet space operations, and related calendar queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calendar and Meet tools can perform high-impact actions such as deleting events, deleting owned secondary calendars, moving events, or ending active conferences without enough enforced confirmation.

Mitigation: Use a dedicated Google account or narrow OAuth scopes where possible, set GOG_READONLY=1 for read-only use, and require human review before enabling destructive actions.

Risk: Raw run tools and stored Google or Zoom credentials can expand the impact of mistakes or misuse in a trusted host environment.

Mitigation: Avoid raw run tools unless necessary, restrict GOG_FILE_ROOTS, and store credentials only in environments trusted to access the connected accounts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/gogcli-mcp-calendar)
- [gogcli Project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, API Calls, Configuration]

**Output Format:** [MCP tool results as text or JSON, plus setup configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reflect live Google Calendar, Google Meet, or Zoom-connected account state depending on configured credentials and tool inputs.]

## Skill Version(s):

4.5.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides an agent with Gmail tools for reading, organizing, drafting, sending, and managing messages and mailbox settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

People and developers use this skill to work with Gmail through an agent, including threads, labels, drafts, attachments, bulk mailbox actions, and settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server has broad access to read and change Gmail data.

Mitigation: Grant access only if appropriate; set GOG_READONLY=1 for read-only tasks.

Risk: Some delete and settings changes can proceed without a separate user-bound confirmation step.

Mitigation: Review the affected messages or settings and explicitly confirm destructive actions before calling those tools.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli CLI documentation](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [MCP tool responses, including message text, structured Gmail data, and attachment downloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attachments may be returned inline, as a file path, or through a signed download link.]

## Skill Version(s):

4.6.1 (source: server release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

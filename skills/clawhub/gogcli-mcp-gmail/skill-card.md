## Description:

Extended Gmail MCP server via gogcli with auth and full Gmail support for threads, labels, drafts, attachments, forwarding, autoreply, and bulk operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to connect an agent to Gmail through gogcli for reading mail, managing threads and labels, creating and sending drafts, forwarding messages, running autoreplies, and handling attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad Gmail, authentication, and local server-file capabilities.

Mitigation: Install only from a trusted publisher, pin the package version, and use GOG_READONLY when only read access is needed.

Risk: OAuth scope choices and extra services can expand the authority available to the agent.

Mitigation: Avoid broad OAuth services or extraScopes unless they are required for the intended workflow.

Risk: Attachment workflows can use server-side paths or signed download links.

Mitigation: Run the MCP server under a dedicated OS account with limited filesystem access and review attachment delivery settings before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON MCP tool responses and shell command or configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform Gmail side effects such as sending, drafting, deleting, labeling, forwarding, filtering, and attachment delivery.]

## Skill Version(s):

2.30.0 (source: server release metadata, manifest.json, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

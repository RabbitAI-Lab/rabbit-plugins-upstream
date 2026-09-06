## Description:

gogcli-mcp-gmail is an extended Gmail MCP server via gogcli for reading, organizing, drafting, forwarding, autoreplying, and bulk-managing Gmail messages, threads, labels, drafts, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an agent work with Gmail through gogcli, including search and read workflows, labels, drafts, attachments, replies, forwarding, autoreplies, settings, and bulk operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise substantial Gmail authority, including reading mail, sending replies, changing labels and settings, creating filters or aliases, and deleting messages or drafts.

Mitigation: Install only for trusted workflows, review requested Gmail actions before execution, and use GOG_READONLY=1 when only read access is needed.

Risk: Escape-hatch tools and forwarding or filter features can perform broad account actions beyond narrow read or draft workflows.

Mitigation: Use gog_gmail_run, gog_auth_run, forwarding, and filter tools cautiously and require explicit user confirmation for high-impact actions.

Risk: A remote runner can execute Gmail operations through infrastructure outside the local host.

Mitigation: Configure a remote runner only when it is trusted and appropriate for the account and data being accessed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Agent-facing MCP tool results, Markdown instructions, JSON configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read, send, modify, delete, or configure Gmail account data depending on the selected tool and configured permissions.]

## Skill Version(s):

2.29.0 (source: server release metadata, package.json, and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Use when the user asks to read, organize, draft, forward, autoreply, or otherwise work with Gmail in depth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Gmail through an MCP server, including reading threads, managing labels, working with drafts and attachments, forwarding mail, autoreplying, and running bulk mailbox actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Gmail authority can expose or modify sensitive mailbox content.

Mitigation: Install only for accounts where broad Gmail access is acceptable, and use read-only mode for shared or read-only deployments.

Risk: Signed attachment URLs can be fetched by anyone with the link until they expire.

Mitigation: Use signed URL delivery only when necessary and treat generated links as sensitive during their lifetime.

Risk: Persistent file-keyring deployments can expose credentials on untrusted shared hosts.

Mitigation: Avoid persistent file-keyring deployments on untrusted shared hosts and keep file roots narrowly scoped.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration]

**Output Format:** [MCP tool results, Gmail data, file paths, signed URLs, markdown guidance, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create, update, send, delete, archive, label, download, or expose Gmail content depending on tool choice and account permissions.]

## Skill Version(s):

4.3.0 (source: server release metadata, package.json, and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

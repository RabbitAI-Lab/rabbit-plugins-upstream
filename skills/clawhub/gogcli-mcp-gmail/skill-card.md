## Description:

gogcli-mcp-gmail is an extended Gmail MCP server via gogcli for reading, organizing, drafting, forwarding, autoreplying, and bulk-managing Gmail messages, threads, labels, drafts, attachments, and settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to give an MCP-capable assistant authenticated Gmail operations beyond basic search, retrieval, and sending. It is suited for mailbox triage, draft workflows, attachment handling, label and filter management, forwarding, autoreply, and bulk message actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can receive broad Gmail account access, including high-impact send, forwarding, delete, batch-delete, auth, and escape-hatch actions.

Mitigation: Install only when broad Gmail access is intended, prefer GOG_READONLY for read-only use, and manually review draft-send, forwarding-filter, delete, batch-delete, auth, and gog_gmail_run actions before allowing them.

Risk: Weak host isolation or exposed gog credentials could increase Gmail account access risk.

Mitigation: Avoid shared or weakly isolated hosts and protect the gog keyring and data directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [gogcli project](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [MCP tool results as text or JSON, with setup snippets and occasional file paths or signed URLs for attachment delivery.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authenticated gogcli/Gmail access; attachment delivery may return inline content, a local path, a Drive upload, or a signed URL.]

## Skill Version(s):

4.1.0 (source: package.json, manifest.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

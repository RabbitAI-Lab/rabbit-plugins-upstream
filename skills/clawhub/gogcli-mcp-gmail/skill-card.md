## Description:

gogcli-mcp-gmail lets an agent read, organize, draft, forward, autoreply, and manage Gmail through gogcli, including threads, labels, drafts, attachments, bulk actions, forwarding, and settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to connect an agent to a selected Gmail account for mail triage, message and thread reading, draft preparation, replies, forwards, label management, settings changes, and controlled bulk operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad Gmail access, including reading mail, sending replies, modifying labels and settings, and deleting account objects.

Mitigation: Install only for accounts where this level of access is acceptable; use GOG_READONLY=1 for read-only workflows and manually review destructive or mutating Gmail actions.

Risk: Attachment delivery can expose sensitive mailbox content through server-side file paths, signed URLs, or Drive delivery.

Mitigation: Restrict GOG_FILE_ROOTS and avoid signed URL or Drive delivery for highly sensitive attachments unless that delivery mode is specifically needed.

Risk: Raw command escape hatches can run broader gog auth or Gmail subcommands than the dedicated tools expose.

Mitigation: Review tool permissions before deployment and require human approval for raw command use in sensitive accounts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, files, links, configuration]

**Output Format:** [MCP tool responses as text or JSON; attachment tools may return inline content, server file paths, signed URLs, or Drive links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the Gmail account configured through gogcli; mutating tools depend on confirmation and read-only settings.]

## Skill Version(s):

4.5.0 (source: evidence release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

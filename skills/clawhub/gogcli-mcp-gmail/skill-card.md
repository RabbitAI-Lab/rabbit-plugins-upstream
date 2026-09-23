## Description:

Use when the user asks to read, organize, draft, forward, autoreply, or otherwise work with Gmail in depth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, developers, and agents use this skill to work with Gmail through gogcli for reading threads, managing labels and drafts, handling attachments, sending or forwarding mail, and performing bulk mailbox operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic Gmail command tool can bypass safer confirmation paths for sending or mutating mail.

Mitigation: Prefer dedicated Gmail tools, avoid using gog_gmail_run for sending, replying, forwarding, autoreply, or mailbox mutations, and require human review before high-impact actions.

Risk: The skill can act on a user's mailbox, including sending mail, changing labels, deleting messages, and changing settings.

Mitigation: Use GOG_READONLY when only reads are needed, keep OAuth services scoped to Gmail, and grant the agent only the mailbox permissions required for the task.

Risk: OAuth refresh-token and keyring state can persist on the host.

Mitigation: Store credentials in the intended keyring or persistent data directory, protect keyring secrets, rotate tokens when access changes, and review host persistence before shared deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, API calls, Guidance]

**Output Format:** [MCP tool responses with text, Markdown, Gmail API JSON, attachment file paths or links, and action status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, update, send, delete, label, archive, trash, import, or download Gmail content depending on tool permissions and configuration.]

## Skill Version(s):

4.2.5 (source: package.json, manifest.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

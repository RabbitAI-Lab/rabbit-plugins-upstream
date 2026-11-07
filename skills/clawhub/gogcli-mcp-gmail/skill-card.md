## Description:

Use when the user asks to read, organize, draft, forward, autoreply, or otherwise work with Gmail in depth. Triggers for requests involving threads, labels, drafts, attachments, bulk archive/trash/mark-read operations, forwarding messages, or any Gmail operation beyond simple search/get/send. Includes auth and Gmail tools only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers use this Gmail MCP server to search and read email, manage threads, labels, drafts, and attachments, and perform actions such as sending, forwarding, bulk changes, or mailbox settings updates through agent tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some deletion tools bypass confirmation, and mailbox settings can be changed without an approval step.

Mitigation: Start with GOG_READONLY=1 and require client approval before enabling deletion or mailbox-setting tools.

Risk: The integration can access Gmail data and files through the authorized Google account.

Mitigation: Authorize only the Google services needed and keep allowed file directories narrow.

Risk: A hosted attachment link can be used by anyone who has it until it expires, and read-only mode does not block hosted uploads.

Mitigation: Treat hosted links as bearer links, share them only with intended recipients, and do not rely on read-only mode to prevent hosted uploads.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [gogcli project documentation](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Links]

**Output Format:** [MCP tool results containing text or JSON, with attachment files or download links when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attachment delivery depends on size and mode; hosted download links are temporary.]

## Skill Version(s):

4.10.0 (source: package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

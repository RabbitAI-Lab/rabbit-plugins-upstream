## Description:

gogcli-mcp-gmail provides a Gmail MCP server via gogcli for authentication, search, messages, threads, labels, drafts, attachments, forwarding, autoreply, and bulk operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an agent read, organize, draft, forward, reply to, and manage Gmail through a gogcli-backed MCP server. It is suited for deep Gmail workflows involving threads, labels, drafts, attachments, bulk mailbox actions, and Gmail settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can require broad Gmail authority and may expose or change sensitive mailbox content.

Mitigation: Install only for trusted accounts, protect the gog keyring and keyring password, and prefer GOG_READONLY=1 for read-only use.

Risk: Some send and delete actions can run without a separate user confirmation.

Mitigation: Use an MCP host or policy layer that requires explicit user confirmation before draft-send, permanent delete, settings deletion, forwarding, autoreply, and bulk mailbox actions.

Risk: Attachment delivery can produce local file paths or hosted signed links that may expose message attachments outside the original Gmail session.

Mitigation: Use hosted URL or Drive delivery only in trusted contexts, keep signed links short-lived, and avoid sharing attachment outputs with untrusted tools or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, files, configuration]

**Output Format:** [MCP tool responses as text or JSON, with optional local file paths, hosted URLs, or Drive links for attachment delivery.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can reflect Gmail mailbox state and can include results from actions that send, delete, label, archive, or modify messages and drafts.]

## Skill Version(s):

4.2.4 (source: evidence.release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

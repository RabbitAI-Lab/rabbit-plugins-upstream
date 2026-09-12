## Description:

Provides an MCP Gmail agent skill for reading, organizing, drafting, forwarding, autoreplying, and bulk-managing Gmail through gogcli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to give an agent broad Gmail capabilities, including authenticated search, thread and label management, draft workflows, attachments, forwarding, autoreply, and bulk mailbox operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad Gmail and account control.

Mitigation: Install only for agents that need broad Gmail authority; use the narrowest Google scopes and a dedicated account where possible.

Risk: The skill can forward Google access tokens to a configurable remote runner.

Mitigation: Do not set GOG_RUNNER_URL unless it points to infrastructure you control and trust.

Risk: The generic gog_gmail_run escape hatch can perform deliberate admin or settings actions.

Mitigation: Avoid gog_gmail_run unless a dedicated tool is unavailable and the requested action has been reviewed.

Risk: Attachment delivery through Drive can create another copy of email content.

Mitigation: Treat Drive delivery as content duplication and confirm that sharing email attachments through Drive is acceptable.

Risk: Send, forwarding, settings changes, and permanent deletes can have user-visible or irreversible effects.

Mitigation: Confirm these operations carefully before execution and prefer read-only mode with GOG_READONLY when write access is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text responses, with structured Gmail MCP tool results when the agent calls Gmail operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Gmail API JSON, Gmail web URLs, inline attachment content, Drive links for larger attachments, draft updates, sent mail, label changes, settings changes, or destructive mailbox actions depending on the invoked tool.]

## Skill Version(s):

2.29.1 (source: evidence release, package.json, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

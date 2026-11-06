## Description:

Use when the user asks to read, organize, draft, forward, autoreply, or otherwise work with Gmail in depth. Triggers for requests involving threads, labels, drafts, attachments, bulk archive/trash/mark-read operations, forwarding messages, or any Gmail operation beyond simple search/get/send. Includes auth and Gmail tools only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers can connect an AI assistant to an authorized Gmail account to search and read messages, manage threads and labels, create drafts and replies, send or forward messages, handle attachments, and manage Gmail settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some destructive Gmail actions can proceed without asking for confirmation.

Mitigation: Use GOG_READONLY=1 for read-only use, and configure host approval for destructive deletion and account-setting changes before enabling writes.

Risk: Hosted attachment delivery can create a persistent Drive copy or a URL that anyone holding it can access for one hour.

Mitigation: Choose attachment delivery deliberately, limit access to hosted URLs, and account for persistent Drive copies when handling sensitive mail.

Risk: External CLI behavior, hosted retention, and dependency vulnerability status remain unverified; attachment tools can access configured file locations.

Mitigation: Keep allowed file roots narrow, authorize only the Google services needed, and review the external CLI and hosting retention before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/gogcli-mcp-gmail)
- [gogcli project](https://github.com/openclaw/gogcli)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, URLs]

**Output Format:** [Text and JSON responses, with attachment content or delivery links when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested Gmail operation and may include message data, attachment content, file paths, or links.]

## Skill Version(s):

4.9.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

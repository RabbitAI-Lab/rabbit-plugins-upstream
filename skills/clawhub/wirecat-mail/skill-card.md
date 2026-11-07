## Description:

Read and organise the owner's mailbox through mail, a WireCat CLI — sync mail over IMAP into the shared store, search it, read an email whole with its attachments' text and follow its thread; mark, move, copy, delete to Trash and undo, keep the owner's mail rules, write drafts, and send, reply and forward over SMTP, with JSON answers. Use when a task needs the owner's mail. It never asks for or prints a password, and over MCP it mails only the owner unless the owner allows more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill on behalf of a mailbox owner to sync, search, read, organize, export, and manage messages and drafts. Sending and other mailbox changes follow the owner's request and the configured profile permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox writes, bulk changes, or sends can affect the owner's mail, while the external CLI's permission enforcement was outside the supplied artifact review.

Mitigation: Use a least-privilege profile, preview changes with dry-run or the returned preview, and confirm recipients and content before sending.

Risk: Synced mail, memo integration, and exported attachments can contain sensitive information.

Mitigation: Limit mailbox permissions and handle retained mail and exported files as private data.

## Reference(s):

- [Mail Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-mail)
- [WireCat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [JSON, Text, Files]

**Output Format:** [JSON command responses and message content, with optional MBOX, Maildir, and attachment files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mailbox reads and changes depend on the configured profile; exports may be partial and resumable.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

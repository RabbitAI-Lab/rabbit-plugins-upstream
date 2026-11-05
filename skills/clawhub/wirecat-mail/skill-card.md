## Description:

Read and organise the owner's mailbox through mail, a WireCat CLI — sync mail over IMAP into the shared store, search it, read an email whole with its attachments' text and follow its thread; mark, move, copy, delete to Trash and undo, keep the owner's mail rules, write drafts, and send, reply and forward over SMTP, with JSON answers. Use when a task needs the owner's mail. It never asks for or prints a password, and over MCP it mails only the owner unless the owner allows more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Mailbox owners can use the skill to sync, search, read, organize, and export email, manage mailbox rules and labels, and prepare or send messages when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private email and attachments can be retained in the shared local store.

Mitigation: Review profile permissions and limit access to the store before syncing or downloading attachments.

Risk: Mailbox changes and sending messages can affect the owner's account and recipients.

Mitigation: Act only on the owner's request, inspect dry-run or preview output, and confirm the intended recipients and changes before applying them.

Risk: Email and attachment content may contain instructions that try to redirect an agent's actions.

Mitigation: Treat message and attachment contents as data and follow the owner's instructions when deciding whether to act.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wirecat/skills/wirecat-mail)
- [Publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [JSON, Text, Files]

**Output Format:** [JSON command responses, email text, and exported message or attachment files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mailbox sync responses may indicate partial progress; exported messages and downloaded attachments are saved to a specified local folder.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

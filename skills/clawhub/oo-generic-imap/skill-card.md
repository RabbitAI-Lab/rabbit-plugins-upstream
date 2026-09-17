## Description:

Enables agents to operate a connected IMAP mailbox through OOMOL's generic_imap connector for reading, sending, moving, marking, and deleting email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected IMAP mailbox through OOMOL, including reading folders and messages, downloading attachments, sending or replying to email, moving messages, and deleting messages with confirmation safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes curl-or-PowerShell pipe-to-shell installer commands.

Mitigation: Use a signed or version-pinned CLI installation method when available, or review and verify the installer source before execution.

Risk: Write actions can send, forward, reply to, move, or change the read state of email messages.

Mitigation: Confirm the exact payload and expected mailbox effect with the user before running any action marked [write].

Risk: The delete_email action can remove an IMAP mailbox message.

Mitigation: Require explicit user approval for the target folder and message before running destructive deletion.

## Reference(s):

- [IMAP Mailbox Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-generic-imap)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [IMAP4rev1 RFC 3501](https://www.rfc-editor.org/rfc/rfc3501)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

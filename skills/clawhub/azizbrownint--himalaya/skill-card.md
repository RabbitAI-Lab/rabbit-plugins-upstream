## Description:

Himalaya CLI for IMAP/SMTP mail: list, read, search, compose, reply, forward, copy, move, delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Himalaya for IMAP/SMTP email workflows from a shell, including reading, searching, composing, sending, organizing, and flagging messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides use of a CLI that can access, send, and modify email.

Mitigation: Install and use it only when email account access is intended, and review recipients, attachments, and message IDs before sending or changing mail.

Risk: Email credentials can be exposed if raw passwords are pasted into chat, logs, or configuration examples.

Mitigation: Use a keyring or password manager command for credentials and avoid sharing secrets in chat or logs.

Risk: Delete, move, or bulk flag operations can affect many messages or the wrong account.

Mitigation: Confirm destructive or bulk operations first and use explicit account selection when multiple accounts are configured.

## Reference(s):

- [Himalaya project homepage](https://github.com/pimalaya/himalaya)
- [Himalaya Configuration Reference](references/configuration.md)
- [Message Composition with MML](references/message-composition.md)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/himalaya)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator guidance for an installed Himalaya CLI and configured mail account.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Himalaya helps agents use the Himalaya CLI to list, read, write, reply, forward, search, and organize email through configured IMAP/SMTP, Notmuch, or Sendmail accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent prepare and run Himalaya email CLI workflows for mailbox reading, search, composition, reply, forwarding, folder organization, and configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email account credentials can be exposed if raw passwords are placed in Himalaya configuration files.

Mitigation: Use pass, system keyring, OAuth, or another secret manager instead of raw password fields.

Risk: Send, reply-all, forward, move, and delete commands can change mailbox state or contact recipients unexpectedly.

Mitigation: Require human review before executing any command that sends mail or modifies messages.

Risk: Attachment download or composition workflows can expose sensitive files or message content.

Mitigation: Confirm attachment paths, recipients, and message body content before attachment or send operations.

## Reference(s):

- [Himalaya project homepage](https://github.com/pimalaya/himalaya)
- [Himalaya Configuration Reference](references/configuration.md)
- [Message Composition with MML](references/message-composition.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and TOML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Himalaya CLI and a configured email account.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

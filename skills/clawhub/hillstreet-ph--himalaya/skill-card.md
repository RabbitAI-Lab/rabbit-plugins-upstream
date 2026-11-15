## Description:

Himalaya CLI for IMAP/SMTP mail: list, read, search, compose, reply, forward, copy, move, delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to operate IMAP/SMTP email from the shell, including reading, searching, composing, sending, and organizing messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mail account credentials could be exposed if stored or shared insecurely.

Mitigation: Use a password manager, system keyring, or command-based credential lookup, and keep secrets out of chat and logs.

Risk: Sending, moving, or deleting messages can make unintended changes to an email account.

Mitigation: Check recipients and message content before sending, and verify message IDs and destination folders before changing messages.

## Reference(s):

- [Himalaya project](https://github.com/pimalaya/himalaya)
- [Account configuration reference](references/configuration.md)
- [Message composition with MML](references/message-composition.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples and TOML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes email account setup, message operations, and MML composition guidance.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

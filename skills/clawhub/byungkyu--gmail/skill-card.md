## Description:

Gmail API integration with managed OAuth for reading, sending, and managing emails, threads, labels, and drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Gmail account through Maton-managed OAuth, inspect mailbox data, send or draft messages, manage labels and threads, and create user-approved Gmail automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Gmail data and perform write actions such as sending emails, modifying labels, drafts, or trashing messages.

Mitigation: Use the narrowest Gmail authorization scopes available, default to read and list operations, and require explicit user approval before any write, deletion, new connection, or hosted automation.

Risk: Hosted functions, triggers, and destinations can create persistent automated actions or forwarding.

Mitigation: Approve only exact destination URLs the user trusts, keep Gmail-derived data within Maton-controlled destinations unless separately approved, and remove automations when they are no longer needed.

Risk: Maton API keys or OAuth-derived credentials could be exposed through logs, command arguments, destination headers, or files.

Mitigation: Prefer OAuth through the Maton CLI, never print or persist credentials, do not place Maton or Gmail credentials in destination headers, and rotate any key that was exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/gmail)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Gmail API Overview](https://developers.google.com/gmail/api/reference/rest)
- [Gmail Trigger Reference](references/google-mail/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Gmail authorization.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

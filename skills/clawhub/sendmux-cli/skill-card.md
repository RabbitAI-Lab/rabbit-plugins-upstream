## Description:

Use the Sendmux CLI for durable agent inbox registration, owner invites, profiles, and terminal-driven Management, Mailbox, and Sending workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the Sendmux CLI to register agent inboxes, manage profiles and account resources, read mailboxes, and send email from a terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox reads, sends, attachments, and account-management commands can access private data or change external resources.

Mitigation: Review each mailbox-read, send, attachment-upload, and account-management command before execution; confirm destructive operations explicitly.

Risk: Credentials and persistent profiles can retain access beyond the immediate task.

Mitigation: Use scoped profiles or tokens, keep secrets in a secret store rather than chat or command arguments, and revoke or log out profiles when no longer needed.

## Reference(s):

- [Sendmux CLI on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-cli)
- [Sendmux skills homepage (listed in skill metadata)](https://github.com/Sendmux/skills)
- [Sendmux OAuth for REST APIs](https://sendmux.ai/docs/developer-tools/oauth)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can request JSON-formatted CLI responses.]

## Skill Version(s):

1.0.11 (source: ClawHub release; skill frontmatter: 1.7.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Zoho Mail API integration with managed OAuth for sending, receiving, searching, and managing emails, folders, and labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Zoho Mail through Maton's managed OAuth gateway, including reading mail, searching messages, sending mail, and managing folders, labels, and attachments. It is intended for mailbox tasks where the user can authorize the connection and confirm any write or destructive action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned external package installation can fetch a different CLI or SDK version over time.

Mitigation: Install only from Maton's official package sources and avoid administrator privileges during package installation.

Risk: Mailbox writes, sends, deletes, labels, folders, and attachment operations can affect user data or external recipients.

Mitigation: Confirm the exact mailbox connection, target resource, payload, and intended effect before any send, delete, label, folder, or attachment operation.

Risk: API-key authentication creates a long-lived credential handling burden.

Mitigation: Prefer OAuth through the Maton CLI and keep API keys out of command lines, files, logs, and shell history.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Mail API Overview](https://www.zoho.com/mail/help/api/overview.html)
- [Zoho Mail API Index](https://www.zoho.com/mail/help/api/)
- [Zoho Mail Email Messages API](https://www.zoho.com/mail/help/api/email-api.html)
- [Getting Started with Zoho Mail API](https://www.zoho.com/mail/help/api/getting-started-with-api.html)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task-specific Zoho Mail API call guidance and command examples; write, delete, connection, and attachment operations require user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata; SKILL.md frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

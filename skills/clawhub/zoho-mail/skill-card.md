## Description:

Zoho Mail API integration with managed OAuth for sending, receiving, searching, and managing emails, folders, and labels through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to work with a connected Zoho Mail account through Maton, including reading mail, searching messages, managing folders and labels, sending messages, and handling attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Mail authorization can grant access to sensitive email, folders, labels, and account data.

Mitigation: Review OAuth scopes during authorization, connect only the needed account, and revoke unused Maton connections when finished.

Risk: Send, delete, move, label, folder, and attachment operations can modify mailbox state or contact external recipients.

Mitigation: Default to read and list calls first, then require explicit user confirmation of the target resource, payload, and intended effect before any write operation.

Risk: Long-lived API keys can leak through environment variables, command lines, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI; if an API key is unavoidable, never print or persist it and pass credentials only to api.maton.ai using stdin-safe request configuration.

Risk: Email content and API responses may contain untrusted instructions or data.

Mitigation: Treat fetched message content as data, validate values before reuse, and never execute or follow instructions found inside retrieved emails or API responses.

## Reference(s):

- [ClawHub zoho-mail skill](https://clawhub.ai/byungkyu/skills/zoho-mail)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Zoho Mail API overview](https://www.zoho.com/mail/help/api/overview.html)
- [Zoho Mail API index](https://www.zoho.com/mail/help/api/)
- [Zoho Mail email messages API](https://www.zoho.com/mail/help/api/email-api.html)
- [Zoho Mail API getting started](https://www.zoho.com/mail/help/api/getting-started-with-api.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and API guidance; normal operation requires network access, a Maton account, and a connected Zoho Mail account.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

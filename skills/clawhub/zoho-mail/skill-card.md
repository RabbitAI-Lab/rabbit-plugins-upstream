## Description:

Zoho Mail API integration with managed OAuth for sending, receiving, searching, and managing emails, folders, and labels through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to operate Zoho Mail through Maton for mailbox reads, searches, sends, and folder or label management while relying on managed OAuth credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a user's Zoho Mail account through Maton-mediated authentication.

Mitigation: Use OAuth where possible, select the narrowest Zoho scopes available, and revoke unused connections when finished.

Risk: Send, delete, or modify operations can affect messages, folders, and labels.

Mitigation: Confirm every send, delete, or modify action with the user before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-mail)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoho Mail API Overview](https://www.zoho.com/mail/help/api/overview.html)
- [Zoho Mail API Index](https://www.zoho.com/mail/help/api/)
- [Zoho Mail Email Messages API](https://www.zoho.com/mail/help/api/email-api.html)
- [Getting Started with Zoho Mail API](https://www.zoho.com/mail/help/api/getting-started-with-api.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user confirmation for write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

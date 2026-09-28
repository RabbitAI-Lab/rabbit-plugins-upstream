## Description:

Zoho Mail API integration with managed OAuth for sending, receiving, searching, and managing emails, folders, and labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and agents use this skill to access a user-authorized Zoho Mail account through Maton, read and search messages, send mail, and manage folders or labels. It can also guide user-approved hosted functions and triggers for Zoho Mail-related automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access mailbox data through the selected Zoho Mail connection.

Mitigation: Prefer OAuth, select the narrowest available scopes, specify the intended connection when multiple accounts exist, and revoke unused connections.

Risk: Send, delete, update, and folder or label operations can change user mail data.

Mitigation: Default to read/list operations and require explicit user confirmation of the target resource, payload, and intended effect before any write.

Risk: Triggers, hosted functions, and destinations can create persistent automation or data forwarding.

Mitigation: Create them only for a specific user-approved purpose, keep function network access denied unless separately approved, review destinations before use, and remove automation when it is no longer needed.

Risk: Raw HTTP fallback requires a long-lived Maton API key in the process environment.

Mitigation: Use the CLI with OAuth when possible; if raw HTTP is required, do not print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-mail)
- [Zoho Mail API Overview](https://www.zoho.com/mail/help/api/overview.html)
- [Zoho Mail API Index](https://www.zoho.com/mail/help/api/)
- [Email Messages API](https://www.zoho.com/mail/help/api/email-api.html)
- [Getting Started with Zoho Mail API](https://www.zoho.com/mail/help/api/getting-started-with-api.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated API-call guidance, function examples, trigger setup steps, and safety confirmations for user-approved Zoho Mail operations.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

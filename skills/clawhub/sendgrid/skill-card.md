## Description:

SendGrid API integration with managed OAuth for sending emails, managing contacts, templates, suppressions, statistics, sender identities, unsubscribe groups, and SendGrid API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with a connected SendGrid account through Maton, including email delivery, marketing contacts, templates, suppressions, sender identities, statistics, and API key management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email sends and other write operations can affect real recipients, account data, or sender reputation.

Mitigation: Default to read or list operations and require explicit user approval for every POST, PUT, PATCH, DELETE, email send, or new connection.

Risk: SendGrid API key management can create long-lived credentials that persist outside the session.

Mitigation: Only perform API key management when explicitly requested, never display created key values, and confirm scope and intended use before changes.

Risk: Using the raw MATON_API_KEY fallback can expose a long-lived Maton credential.

Mitigation: Prefer OAuth through the Maton CLI and use the raw API key fallback only when the CLI cannot be used.

## Reference(s):

- [ClawHub SendGrid Skill](https://clawhub.ai/byungkyu/skills/sendgrid)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [SendGrid API Documentation](https://www.twilio.com/docs/sendgrid/api-reference)
- [SendGrid Mail Send API](https://www.twilio.com/docs/sendgrid/api-reference/mail-send)
- [SendGrid Marketing Contacts API](https://www.twilio.com/docs/sendgrid/api-reference/contacts)
- [SendGrid Suppressions Overview](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-suppressions)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce SendGrid API requests through Maton; write operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

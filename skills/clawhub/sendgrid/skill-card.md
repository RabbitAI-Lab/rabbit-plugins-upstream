## Description:

SendGrid API integration through Maton-managed OAuth for sending email, managing contacts, templates, suppressions, sender identities, unsubscribe groups, statistics, and API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing or email teams use this skill to perform SendGrid account operations through Maton, including transactional email, marketing contacts and lists, templates, suppressions, sender identities, unsubscribe groups, statistics, and API key management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SendGrid operations are routed through Maton and can access account data or change account state.

Mitigation: Prefer OAuth and the Maton CLI, default to read and list calls, and approve every write, new connection, or account-changing action before execution.

Risk: Email sending delivers messages to real recipients and can affect deliverability, reputation, cost, and user trust.

Mitigation: Confirm recipients, subject, content, sender identity, and intended audience before any send operation.

Risk: API key management can create long-lived SendGrid credentials that persist beyond the session.

Mitigation: Use API key operations only when explicitly requested, apply least privilege, and never print, log, persist, or expose created key values.

Risk: Raw MATON_API_KEY fallback can expose a long-lived credential through environment variables, logs, shell history, or process listings.

Mitigation: Avoid the raw fallback unless the CLI cannot be used; never echo or persist the key, feed authorization headers through stdin, and send the key only to api.maton.ai.

## Reference(s):

- [ClawHub SendGrid Skill](https://clawhub.ai/byungkyu/skills/sendgrid)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [SendGrid API Documentation](https://www.twilio.com/docs/sendgrid/api-reference)
- [SendGrid Mail Send API](https://www.twilio.com/docs/sendgrid/api-reference/mail-send)
- [SendGrid Marketing Campaigns API](https://www.twilio.com/docs/sendgrid/api-reference/contacts)
- [SendGrid Suppressions Overview](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-suppressions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code, JSON]

**Output Format:** [Markdown with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations require network access, a Maton account, and an authorized SendGrid connection.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

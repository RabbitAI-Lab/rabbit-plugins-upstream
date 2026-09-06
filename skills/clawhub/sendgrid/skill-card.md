## Description:

SendGrid API integration with managed OAuth for sending email, managing contacts, templates, suppressions, sender identities, unsubscribe groups, API keys, and analyzing email performance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to connect a SendGrid account through Maton, send transactional or marketing email, manage email assets and recipient data, handle suppressions, and review delivery statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email sends and write operations can affect real recipients, account data, sender reputation, and persistent SendGrid resources.

Mitigation: Default to read and list calls, then require explicit user approval with the target resource, payload, and intended effect before sending email or running any POST, PUT, PATCH, or DELETE request.

Risk: SendGrid API key management can create long-lived credentials that persist beyond the session.

Mitigation: Only manage API keys when the user explicitly requests it, avoid exposing created key values, and review every proposed key creation, update, or deletion before execution.

Risk: Using API keys or raw HTTP fallback can expose durable credentials if they are printed, logged, written to files, or passed through broad environment scope.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, and avoid printing, persisting, or transmitting credential values outside the intended Maton API flow.

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

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected SendGrid account; write operations require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

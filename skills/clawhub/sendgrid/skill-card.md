## Description:

SendGrid API integration with managed OAuth for sending email, managing contacts, templates, suppressions, statistics, sender identities, unsubscribe groups, and SendGrid API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to access SendGrid through the Maton gateway for transactional or marketing email workflows, contact and template management, suppressions, statistics, sender identities, unsubscribe groups, and API key management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send real email and change SendGrid account data.

Mitigation: Default to read and list calls, verify account context and resource identifiers, and require explicit user approval before any POST, PUT, PATCH, or DELETE request.

Risk: SendGrid API key management can create long-lived credentials that persist beyond the session.

Mitigation: Use API key management only when explicitly requested, prefer OAuth where possible, and never expose created key values in output.

Risk: Raw HTTP fallback requires a long-lived Maton API key in the process environment.

Mitigation: Use raw HTTP only where the CLI cannot be installed, do not print or persist the key, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub SendGrid Skill](https://clawhub.ai/byungkyu/skills/sendgrid)
- [Maton Homepage](https://maton.ai)
- [SendGrid API Documentation](https://www.twilio.com/docs/sendgrid/api-reference)
- [Mail Send API](https://www.twilio.com/docs/sendgrid/api-reference/mail-send)
- [Marketing Campaigns API](https://www.twilio.com/docs/sendgrid/api-reference/contacts)
- [Suppressions Overview](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-suppressions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API workflow guidance for calls that require network access, Maton authentication, and a connected SendGrid account.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

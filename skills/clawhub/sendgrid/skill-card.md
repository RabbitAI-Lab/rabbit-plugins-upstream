## Description:

SendGrid API integration with managed OAuth for sending emails and managing contacts, templates, suppressions, statistics, sender identities, unsubscribe groups, and SendGrid API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a SendGrid account through Maton: sending approved transactional or marketing email, managing email lists and suppression data, and reviewing delivery or engagement statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send email to real recipients and modify SendGrid resources.

Mitigation: Confirm the audience, content, sender, target resource, payload, and intended effect before any send, modify, delete, API-key, or automation action.

Risk: API key workflows can create long-lived credentials that persist outside the Maton connection.

Mitigation: Use OAuth and least-privilege scopes when possible; only manage API keys when explicitly requested, never log key values, and rotate any credential exposed in shell history or logs.

Risk: Hosted functions and triggers can create unattended automation or standing data forwarding.

Mitigation: Use user-reviewed handlers, prefer deny-all network policy for functions, keep trigger destinations on approved platform endpoints unless the user confirms a third-party host, and remove unused automation.

## Reference(s):

- [SendGrid Skill Page](https://clawhub.ai/byungkyu/skills/sendgrid)
- [Maton Homepage](https://maton.ai)
- [SendGrid API Documentation](https://www.twilio.com/docs/sendgrid/api-reference)
- [Mail Send API](https://www.twilio.com/docs/sendgrid/api-reference/mail-send)
- [Marketing Campaigns API](https://www.twilio.com/docs/sendgrid/api-reference/contacts)
- [Suppressions Overview](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-suppressions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Google Mail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include authenticated API call guidance and should avoid exposing raw personal data or credential values.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

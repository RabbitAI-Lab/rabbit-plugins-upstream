## Description:

Gumroad API integration with managed OAuth for accessing products, sales, subscribers, licenses, and webhooks for a digital storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external operators use this skill to manage Gumroad storefront data through Maton-authenticated API calls, including product, sales, subscriber, license, and webhook workflows. It defaults to read and list operations and requires explicit approval for writes, new connections, hosted functions, triggers, or raw HTTP credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Gumroad storefront data, including products, sales, subscribers, licenses, webhooks, and customer-related records.

Mitigation: Install only when the publisher and Maton account are trusted, use the least-privileged Gumroad connection available, and extract only the fields needed for the task.

Risk: Writes, product changes, license changes, webhook changes, connection creation, hosted functions, triggers, and destination forwarding can persistently affect the user's storefront or data flows.

Mitigation: Require separate explicit approval for each write, new connection, hosted function, trigger, destination URL, or persistent automation before running it.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key in the process environment.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, never print, log, persist, or pass the key on the command line, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Gumroad Skill](https://clawhub.ai/byungkyu/skills/gumroad)
- [Maton Homepage](https://maton.ai)
- [Gumroad API Overview](https://gumroad.com/api)
- [Create API Application](https://help.gumroad.com/article/280-create-application-api)
- [License Keys Help](https://help.gumroad.com/article/76-license-keys)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown guidance with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authenticated Gumroad connection; responses may include storefront or customer data.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

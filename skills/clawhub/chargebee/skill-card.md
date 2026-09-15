## Description:

Chargebee provides a Maton-managed OAuth integration for accessing Chargebee APIs to manage subscriptions, customers, invoices, and billing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to administer Chargebee billing data through authenticated Maton CLI or HTTP calls, with read/list operations preferred and explicit confirmation required for writes. The skill also documents approved hosted function and trigger patterns for Chargebee automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chargebee write actions can mutate subscriptions, invoices, customers, and billing records.

Mitigation: Default to read/list calls, verify the exact connection, endpoint, account, resource ID, and financial consequence, then wait for explicit user approval before writes.

Risk: Raw HTTP mode uses a long-lived Maton API key that can leak through logs, shell history, child processes, or pasted output.

Mitigation: Use OAuth where possible; when an API key is unavoidable, keep it in the process environment only, never print or persist it, send it only to api.maton.ai, and rotate it after exposure.

Risk: Hosted functions and persistent triggers can create ongoing automation or data forwarding.

Mitigation: Use hosted functions or trigger destinations only after reviewing the code, scope, destination, network policy, and cleanup plan; prefer platform destinations and avoid third-party hosts unless specifically approved.

## Reference(s):

- [ClawHub Chargebee Skill](https://clawhub.ai/byungkyu/skills/chargebee)
- [Maton](https://maton.ai)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [Chargebee API Overview](https://apidocs.chargebee.com/docs/api)
- [Chargebee Customers API](https://apidocs.chargebee.com/docs/api/customers)
- [Chargebee Subscriptions API](https://apidocs.chargebee.com/docs/api/subscriptions)
- [Chargebee Invoices API](https://apidocs.chargebee.com/docs/api/invoices)
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

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with CLI commands, HTTP examples, code snippets, and reference tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Chargebee connection.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Square API integration with managed OAuth for reading and administering Square business resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to connect a Square account, inspect Square resources, and perform specific approved administrative actions through documented Square endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or change Square business and payment data through an authorized connection.

Mitigation: Install only for Square administration, use least-privileged OAuth scopes, confirm the exact connection and resource identifiers before writes, and revoke unused connections.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or pasted output when the CLI cannot be used.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is required, read the API key only from the process environment, never print or persist it, and rotate it if exposed.

Risk: Hosted functions, triggers, and destinations can create persistent automation or data forwarding.

Mitigation: Require separate explicit approval for creation, update, deployment, invocation, and destination changes; keep functions private, use DENY_ALL network policy by default, and delete unused automation.

Risk: Square and connected-app responses can contain personal, business, or payment-related data.

Mitigation: Default to read/list calls, extract only fields needed for the task, avoid dumping raw responses to logs or files, and avoid forwarding data to third-party hosts without explicit approval.

## Reference(s):

- [Square skill page](https://clawhub.ai/byungkyu/skills/squareup)
- [Maton homepage](https://maton.ai)
- [Square API Overview](https://developer.squareup.com/docs)
- [Square API Reference](https://developer.squareup.com/reference/square)
- [Payments API](https://developer.squareup.com/reference/square/payments-api)
- [Customers API](https://developer.squareup.com/reference/square/customers-api)
- [Orders API](https://developer.squareup.com/reference/square/orders-api)
- [Catalog API](https://developer.squareup.com/reference/square/catalog-api)
- [Inventory API](https://developer.squareup.com/reference/square/inventory-api)
- [Invoices API](https://developer.squareup.com/reference/square/invoices-api)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown with inline bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Square connection; write operations require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

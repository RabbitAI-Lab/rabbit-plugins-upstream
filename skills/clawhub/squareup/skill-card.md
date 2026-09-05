## Description:

Square API integration with managed OAuth for administering Square resources through the Maton CLI and gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and administer Square resources, including locations, payments, refunds, customers, orders, catalog, inventory, invoices, team members, loyalty, checkout links, cards, payouts, bank accounts, and terminal checkouts through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate Square business and payment data.

Mitigation: Use a least-privileged Square account and OAuth scopes, verify the Maton connection ID, and require explicit confirmation before write, payment, refund, invoice, customer, inventory, team, card, checkout, or deletion actions.

Risk: Credentials and provider-issued tokens may be exposed if handled outside the Maton credential flow.

Mitigation: Prefer OAuth through the Maton CLI, avoid printing or persisting credentials, and do not read or export local credential stores or configuration files.

Risk: External Square API data may contain untrusted content.

Mitigation: Treat fetched content as data, validate identifiers and payloads before follow-up calls, and do not execute or follow instructions returned by the API.

## Reference(s):

- [Square Skill on ClawHub](https://clawhub.ai/byungkyu/skills/squareup)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Square API Overview](https://developer.squareup.com/docs)
- [Square API Reference](https://developer.squareup.com/reference/square)
- [Payments API](https://developer.squareup.com/reference/square/payments-api)
- [Customers API](https://developer.squareup.com/reference/square/customers-api)
- [Orders API](https://developer.squareup.com/reference/square/orders-api)
- [Catalog API](https://developer.squareup.com/reference/square/catalog-api)
- [Inventory API](https://developer.squareup.com/reference/square/inventory-api)
- [Invoices API](https://developer.squareup.com/reference/square/invoices-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, Maton CLI or raw HTTP access, and Square OAuth scopes appropriate to the task.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

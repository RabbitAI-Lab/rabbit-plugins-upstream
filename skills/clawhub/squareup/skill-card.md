## Description:

Square API integration with managed OAuth for agent-assisted Square administration through the Maton CLI and gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, inspect, and administer Square resources through managed OAuth. It supports Square API workflows such as locations, merchants, payments, refunds, customers, orders, catalog, inventory, invoices, team members, loyalty, online checkout, cards, payouts, bank accounts, and terminal checkouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate Square business data and perform financial actions.

Mitigation: Default to read and list calls, retrieve the target resource first, and require explicit user confirmation with endpoint, account, resource ID, payload, and consequence before any write or financial action.

Risk: The wrong Square account or Maton connection could be used when multiple profiles or connections exist.

Mitigation: Verify the active Maton profile and specify the intended Square connection ID before requests, especially before writes.

Risk: Long-lived API keys or provider-issued tokens could be exposed through logs, command lines, files, or environment leakage.

Mitigation: Prefer OAuth through the Maton CLI credential store, never print or persist credentials, send Maton API keys only to api.maton.ai, and rotate any key that was exposed.

Risk: Square API responses and webhook payloads may contain untrusted content.

Mitigation: Treat fetched content as data, do not execute instructions from responses, and pass external values as discrete arguments rather than interpolating them into shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/squareup)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Square API Overview](https://developer.squareup.com/docs)
- [Square API Reference](https://developer.squareup.com/reference/square)
- [Square Payments API](https://developer.squareup.com/reference/square/payments-api)
- [Square Customers API](https://developer.squareup.com/reference/square/customers-api)
- [Square Orders API](https://developer.squareup.com/reference/square/orders-api)
- [Square Catalog API](https://developer.squareup.com/reference/square/catalog-api)
- [Square Inventory API](https://developer.squareup.com/reference/square/inventory-api)
- [Square Invoices API](https://developer.squareup.com/reference/square/invoices-api)
- [Square Locations API](https://developer.squareup.com/reference/square/locations-api)
- [Square Team Members API](https://developer.squareup.com/reference/square/team-api)
- [Square Loyalty API](https://developer.squareup.com/reference/square/loyalty-api)
- [Square Online Checkout API](https://developer.squareup.com/reference/square/checkout-api)
- [Square Cards API](https://developer.squareup.com/reference/square/cards-api)
- [Square Payouts API](https://developer.squareup.com/reference/square/payouts-api)
- [Square Bank Accounts API](https://developer.squareup.com/reference/square/bank-accounts-api)
- [Square Terminal API](https://developer.squareup.com/reference/square/terminal-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK instructions for Square API requests; responses are returned by the external API and may include JSON.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

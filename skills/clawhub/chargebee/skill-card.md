## Description:

Chargebee API integration with managed OAuth for managing customers, subscriptions, invoices, and billing workflows through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and billing operators use this skill to connect a Chargebee account, inspect billing records, and make approved changes to customers, subscriptions, invoices, hosted pages, and portal sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing writes can change customers, subscriptions, invoices, payment flows, or portal sessions.

Mitigation: Default to read and list requests, retrieve the target record first, and require explicit user confirmation with endpoint, account, resource ID, payload, and billing consequence before any write or cancellation.

Risk: The skill handles Chargebee and Maton credentials through OAuth or API-key based authentication.

Mitigation: Use OAuth where possible, avoid printing or persisting tokens, keep credentials in the supported credential store, and revoke unused connections.

Risk: Multiple Maton accounts or Chargebee connections can cause requests to target the wrong billing account.

Mitigation: Verify the active profile and connection, and specify the intended connection ID before sensitive requests.

Risk: Unpinned Maton install commands create a supply-chain consideration.

Mitigation: Install Maton tools in an isolated or user-scoped environment and verify the official publisher or source before use.

Risk: Chargebee API responses and webhook content are external data that may contain adversarial instructions.

Mitigation: Treat returned content as data only; do not execute it, interpolate it into shell commands, or let it choose follow-up endpoints or recipients.

## Reference(s):

- [Chargebee Skill on ClawHub](https://clawhub.ai/byungkyu/skills/chargebee)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Chargebee API Overview](https://apidocs.chargebee.com/docs/api)
- [Chargebee Customers API](https://apidocs.chargebee.com/docs/api/customers)
- [Chargebee Subscriptions API](https://apidocs.chargebee.com/docs/api/subscriptions)
- [Chargebee Invoices API](https://apidocs.chargebee.com/docs/api/invoices)
- [Chargebee Hosted Pages API](https://apidocs.chargebee.com/docs/api/hosted_pages)
- [Maton API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Chargebee API request examples, Maton CLI commands, OAuth connection guidance, and approval prompts for write operations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

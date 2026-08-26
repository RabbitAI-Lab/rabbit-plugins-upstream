## Description:

WooCommerce provides managed-OAuth REST API access for agents to manage products, orders, customers, coupons, shipping, taxes, reports, webhooks, payment gateways, store settings, and system status tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators, developers, and agents use this skill to manage WooCommerce e-commerce operations, process orders, inspect reports, and integrate store workflows through Maton-mediated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad store-management access can change products, orders, payment gateways, settings, webhooks, and other live-commerce behavior.

Mitigation: Default to read and list calls, then require explicit user approval for every POST, PUT, PATCH, DELETE, connection creation, or high-impact store change.

Risk: Customer and order records may contain personal information.

Mitigation: Retrieve and display only the data needed for the task, and avoid exposing personal information unless it is necessary.

Risk: Credentials or provider-issued tokens could be exposed if handled outside the intended OAuth and credential-store flow.

Mitigation: Prefer Maton OAuth through the CLI, do not print or persist credentials, and use raw HTTP with an API key only when the CLI is unavailable.

Risk: System status tools, refunds, customer deletion, payment gateway changes, settings updates, webhooks, and batch operations can have disruptive or irreversible effects.

Mitigation: Confirm the target connection, resource ID, payload, and intended effect before approving these operations.

## Reference(s):

- [ClawHub WooCommerce Skill](https://clawhub.ai/byungkyu/skills/woocommerce)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to guide Maton CLI or SDK calls; write operations require explicit user approval.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

WooCommerce REST API integration with managed OAuth for products, orders, customers, coupons, shipping, taxes, reports, webhooks, payment gateways, store settings, and system status tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage WooCommerce store operations through Maton-authenticated REST API calls. It is intended for e-commerce tasks such as listing products, processing orders, managing customers, configuring coupons, reviewing reports, and administering store integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations can change live WooCommerce store data or behavior, including refunds, payment gateways, settings, webhooks, customer deletion, and system status tools.

Mitigation: Confirm the target resource, payload, intended effect, and user approval before any write operation; prefer read and list calls first.

Risk: The skill connects to a WooCommerce store through Maton authentication and may access customer or order data.

Mitigation: Install only when the publisher and Maton connection are trusted, use the narrowest WooCommerce scopes available, and avoid retrieving or displaying personal data unless needed for the task.

Risk: Multiple Maton accounts or WooCommerce connections can send requests to the wrong store.

Mitigation: Specify the intended profile and connection when more than one account or connection exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/woocommerce)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- [WooCommerce API Authentication Guide](https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK usage guidance for WooCommerce REST API operations; API responses may include store, order, customer, or configuration data.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

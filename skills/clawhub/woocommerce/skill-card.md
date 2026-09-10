## Description:

WooCommerce REST API integration with managed OAuth for accessing products, orders, customers, coupons, shipping, taxes, reports, webhooks, payment gateways, store settings, and system status tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, store operators, and agents use this skill to manage WooCommerce store operations through Maton, including catalog, order, customer, coupon, tax, shipping, reporting, webhook, payment gateway, settings, and system status tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive WooCommerce store data, including customer and order personal information.

Mitigation: Install only when Maton access to the store is intended, prefer OAuth and read-only scopes where possible, and avoid retrieving or displaying personal information unless needed for the task.

Risk: Write operations, payment gateway changes, settings updates, webhooks, customer deletion, and system status tools can affect customers, transactions, or live store behavior.

Mitigation: Default to read and list calls, confirm the exact target, payload, and intended effect before any POST, PUT, PATCH, or DELETE request, and use extra confirmation for disruptive maintenance actions.

Risk: Long-lived Maton API keys can be exposed through environment variables, logs, command history, or pasted output.

Mitigation: Use OAuth when possible, avoid exposing MATON_API_KEY, never print or persist credentials, and rotate the key if it was disclosed.

Risk: Multiple Maton profiles or WooCommerce connections can cause requests to affect the wrong store.

Mitigation: Specify the intended Maton profile and WooCommerce connection when more than one exists, especially before any write operation.

## Reference(s):

- [ClawHub WooCommerce Skill](https://clawhub.ai/byungkyu/skills/woocommerce)
- [Maton](https://maton.ai)
- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- [WooCommerce API Authentication Guide](https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or SDK workflows; favors read and list operations before any confirmed change.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

WooCommerce REST API integration through Maton-managed OAuth for managing products, orders, customers, coupons, shipping, taxes, reports, webhooks, payment gateways, store settings, and system status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, store operators, and agent users use this skill to inspect and manage WooCommerce store resources through authenticated API calls. It supports e-commerce operations such as product maintenance, order processing, customer lookup, coupon management, reporting, webhooks, payment gateways, settings, and system status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations can change store data or behavior, including refunds, customer deletion, payment gateways, settings, webhooks, and system status tools.

Mitigation: Verify the target connection, resource ID, payload, and intended effect before allowing any write or maintenance operation.

Risk: Customer and order records may contain personal information.

Mitigation: Retrieve and display only the personal data needed for the task.

Risk: Long-lived API keys and provider-issued tokens can leak if printed, logged, persisted, or passed through shell history.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, and avoid exposing token values in files, logs, or command arguments.

## Reference(s):

- [WooCommerce ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/woocommerce)
- [Maton](https://maton.ai)
- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- [WooCommerce API Authentication Guide](https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication)
- [WooCommerce Developer Resources](https://developer.woocommerce.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for new connections and write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

WooCommerce REST API integration with managed OAuth for managing products, orders, customers, coupons, shipping, taxes, reports, webhooks, payment gateways, store settings, and system status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and e-commerce operators use this skill to manage WooCommerce stores, process orders, maintain catalog data, and build approved store automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect a live WooCommerce store, including orders, payment gateways, settings, webhooks, and system status tools.

Mitigation: Confirm the exact store connection and review every write, webhook, payment, settings, or system-status action before execution.

Risk: Customer, order, and payment-adjacent data may include personal or sensitive business information.

Mitigation: Prefer read-only scopes when possible and avoid retrieving, displaying, or forwarding customer/order/payment data unless required for the approved task.

Risk: Forwarding store data to third-party URLs can expose business or customer data outside the approved WooCommerce and Maton workflow.

Mitigation: Forward data only to destinations the user explicitly approves, and confirm the destination host and exact data fields first.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/woocommerce)
- [Maton Homepage](https://maton.ai)
- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- [WooCommerce API Authentication Guide](https://woocommerce.github.io/woocommerce-rest-api-docs/#authentication)
- [WooCommerce Developer Resources](https://developer.woocommerce.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Catalog](references/calendly/triggers.md)
- [GitHub Trigger Catalog](references/github/triggers.md)
- [Google Mail Trigger Catalog](references/google-mail/triggers.md)
- [HubSpot Trigger Catalog](references/hubspot/triggers.md)
- [Linear Trigger Catalog](references/linear/triggers.md)
- [Notion Trigger Catalog](references/notion/triggers.md)
- [Slack Trigger Catalog](references/slack/triggers.md)
- [Stripe Trigger Catalog](references/stripe/triggers.md)
- [Time Trigger Catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with bash, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs authenticated WooCommerce REST API workflows through Maton; write operations, new connections, hosted functions, and trigger actions require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

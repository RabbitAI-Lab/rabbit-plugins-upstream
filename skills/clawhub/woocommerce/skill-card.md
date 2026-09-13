## Description:

WooCommerce REST API integration with managed OAuth for accessing products, orders, customers, coupons, shipping, taxes, reports, webhooks, payment gateways, store settings, and system status tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External store operators and developers use this skill to inspect and manage WooCommerce store resources through authenticated Maton calls. It supports e-commerce operations such as order processing, product and customer management, reporting, webhook setup, and store configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WooCommerce writes, payment gateway changes, settings changes, webhooks, and system tools can affect store behavior, customers, transactions, or downstream automation.

Mitigation: Confirm the target resource, payload, intended effect, and persistence before running writes or automation, and default to read-only calls when possible.

Risk: Customer and order data can include personal information.

Mitigation: Retrieve or display personal data only when it is necessary for the user's task, and avoid forwarding WooCommerce-derived data to external destinations.

Risk: Hosted functions run with the deploying Maton account's available connections, creating residual account-scope risk.

Mitigation: Use a dedicated Maton account with only the required WooCommerce connection, prefer OAuth with the narrowest scopes available, deploy with denied outbound network access where possible, and get separate approval for each deploy or invocation.

## Reference(s):

- [ClawHub WooCommerce Skill](https://clawhub.ai/byungkyu/skills/woocommerce)
- [Maton](https://maton.ai)
- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API endpoint paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands and HTTP request examples that require user approval for writes, connection changes, hosted functions, and triggers.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

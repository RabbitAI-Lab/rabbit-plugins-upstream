## Description:

Helps agents manage WooCommerce products, orders, customers, store settings, and related commerce operations through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Store operators and developers use this skill to inspect and manage WooCommerce products, orders, customers, shipping, payments, and store automation with their approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad access to live store data and operations through the connected account.

Mitigation: Review authorization scopes, prefer read-only access where possible, and confirm each connection or write.

Risk: Refunds, payment gateway and setting changes, or system tools can affect sales and store behavior.

Mitigation: Confirm the exact target and intended effect with the user before executing a change.

Risk: Customer and order information, webhooks, or trigger destinations can expose personal data.

Mitigation: Limit retrieved or forwarded fields to those needed, review destinations, and obtain approval before enabling automation.

## Reference(s):

- [WooCommerce skill release](https://clawhub.ai/byungkyu/skills/woocommerce)
- [Maton](https://maton.ai)
- [Maton API documentation](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [WooCommerce REST API documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Text]

**Output Format:** [Markdown with command examples and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Store data may contain personal information; show only what the task requires.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

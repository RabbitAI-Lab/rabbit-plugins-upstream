## Description:

Shopify商品查询 helps agents filter Shopify storefront products by keyword or URL, price, weekly sales and revenue, listing date, Facebook ad activity, competition, supplier availability, deletion status, and shipping country.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, dropshipping researchers, and agents use this skill to find and compare Shopify products by commercial signals such as demand, price, advertising activity, competition, supplier availability, and shipping country. It also guides users through LinkFox authentication and billing recovery when API access or account balance blocks the query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopify search inputs, account phone and SMS login data, API keys, and billing actions may be sent to LinkFox services.

Mitigation: Install and use the skill only when that data sharing is acceptable for the user and organization; avoid entering sensitive inputs that are not needed for the query.

Risk: Billing recovery can create payment orders or consume credits based on returned product count.

Mitigation: Confirm plan, payment method, amount, and expected per-page credit cost before creating an order or running broad queries.

Risk: Custom LINKFOX_* endpoint overrides can redirect requests to a different service.

Mitigation: Use the default LinkFox endpoints unless the destination is controlled and explicitly approved.

Risk: API keys may be copied into shell startup files during onboarding.

Mitigation: Prefer a managed secret store or session-scoped environment variables where available, and rotate keys if they are exposed.

## Reference(s):

- [Shopify 商品查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopify-product-query)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API inputs and outputs, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The query helper may save full JSON responses in the current workspace and summarize large responses in stdout.]

## Skill Version(s):

1.0.9 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

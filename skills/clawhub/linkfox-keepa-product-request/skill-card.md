## Description:

通过 LinkFox/Keepa API 按 ASIN 查询 Amazon 商品价格、标题、主图、上架日期、规格、FBA 费用、销量和历史销售趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, analysts, and agent users use this skill to retrieve structured ASIN-level product data, compare up to five products, and summarize pricing, sales, category, dimension, and fee information across supported Amazon marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary states that the skill handles ASIN queries and persists saved API responses with insufficient scoping and consent controls.

Mitigation: Tell users before running a lookup that full responses will be saved locally; avoid submitting sensitive product lists, and review or clear the local linkfox response and cache files when needed.

Risk: The security summary states that the skill includes account login, API-token generation, and payment-order workflows.

Mitigation: Require explicit user approval before phone/SMS onboarding, API-token generation, plan selection, or payment-order creation.

Risk: The security guidance warns that lookups can consume credits and that feedback or user text should not be sent without consent.

Mitigation: Confirm credit-consuming lookups with the user before execution and submit feedback only when the user has consented to the content being sent.

## Reference(s):

- [Keepa Amazon Product Detail API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-request)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, local JSON data files, and shell commands for API or onboarding workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The product lookup script saves the full API response under a local linkfox session data directory, prints small responses inline, summarizes larger responses, and uses a 24-hour local cache unless disabled.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

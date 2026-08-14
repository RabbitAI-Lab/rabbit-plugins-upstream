## Description:

Searches and filters Amazon product data from SellerSprite by marketplace, keyword, price, sales, BSR, margin, rating, fulfillment, seller, brand, and listing attributes for product research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to research product opportunities, compare sales and ranking signals, and screen products across supported Amazon marketplaces.

### Deployment Geography for Use:

Global; product data queries are limited to the supported Amazon marketplaces documented by the skill.

## Known Risks and Mitigations:

Risk: Product-search queries and account setup data are handled by LinkFox/SellerSprite services.

Mitigation: Install only if you trust LinkFox/SellerSprite with those queries and account setup data.

Risk: API keys may be exposed through shared logs, shell history, or copied environment configuration.

Mitigation: Obtain API keys through the official site and keep keys out of shared logs and public configuration.

Risk: Gateway URL environment variables can redirect requests away from the intended service.

Mitigation: Verify gateway-related environment variables point to official LinkFox domains before use.

Risk: Account, payment, and feedback-reporting flows can create user-impacting actions.

Mitigation: Require explicit user confirmation before any payment or feedback-reporting action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-product-search)
- [SellerSprite Product Search API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON API responses, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved as JSON data files; large responses are summarized with top-level fields, counts, and samples. Repeated identical queries may use a 24-hour cache.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

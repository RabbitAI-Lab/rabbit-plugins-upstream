## Description:

Search Walmart and read product detail, reviews, category listings, buy-box offers, seller storefronts, and seller catalogs as structured JSON through Scavio's Walmart product-data API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Walmart marketplaces, inspect product details and reviews, compare prices, and retrieve buy-box or seller data for retail research and ecommerce workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SCAVIO_API_KEY exposure could allow unauthorized use of the Scavio account.

Mitigation: Store the key in environment or secret storage and do not commit it to source control.

Risk: Repeated Walmart lookups can spend Scavio API credits, with Mexico search and category requests costing more than default US or Canada requests.

Mitigation: Check the target domain and expected credit cost before running repeated search or category requests.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/walmart-product-data)
- [Scavio Walmart API Documentation](https://scavio.dev/docs/walmart-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart Product Documentation](https://scavio.dev/docs/walmart-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart Reviews Documentation](https://scavio.dev/docs/walmart-reviews?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart Category Documentation](https://scavio.dev/docs/walmart-category?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart Offers Documentation](https://scavio.dev/docs/walmart-offers?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart Seller Documentation](https://scavio.dev/docs/walmart-seller?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart Seller Products Documentation](https://scavio.dev/docs/walmart-seller-products?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON request and response details, shell setup commands, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Walmart search and category requests cost more credits when targeting walmart.com.mx.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

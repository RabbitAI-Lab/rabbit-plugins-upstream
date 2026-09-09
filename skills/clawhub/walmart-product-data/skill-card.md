## Description:

Search Walmart and read product detail, reviews, category listings, buy-box offers, seller storefronts and a seller's catalog as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Walmart marketplaces and retrieve structured product, review, category, offer, and seller data through Scavio's Walmart API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Walmart search terms and product, category, or seller identifiers to Scavio as a third-party API provider.

Mitigation: Use it only for queries appropriate for the user's Scavio account and avoid sending private or sensitive search terms.

Risk: API calls require SCAVIO_API_KEY and may consume Scavio credits.

Mitigation: Keep the API key out of source control and check credits_used and credits_remaining in responses before continuing high-volume workflows.

Risk: Returned Walmart prices, availability, ratings, and seller data can change after retrieval.

Mitigation: Report only values returned by the API and include product URLs so users can verify current listing details before purchase or analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/walmart-product-data)
- [Scavio Walmart API documentation](https://scavio.dev/docs/walmart-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart product documentation](https://scavio.dev/docs/walmart-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart reviews documentation](https://scavio.dev/docs/walmart-reviews?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart category documentation](https://scavio.dev/docs/walmart-category?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart offers documentation](https://scavio.dev/docs/walmart-offers?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart seller documentation](https://scavio.dev/docs/walmart-seller?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio Walmart seller products documentation](https://scavio.dev/docs/walmart-seller-products?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=walmart-product-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON API responses and inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns Walmart product data through Scavio's response envelope, including data, response_time, credits_used, credits_remaining, and optional warnings.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

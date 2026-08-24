## Description:

Search Walmart and read product detail, reviews, category listings, buy-box offers, seller storefronts and a seller's catalog as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Scavio's Walmart API for product search, product detail, reviews, category listings, buy-box seller data, seller storefronts, and seller catalogs. It is suited for retail research, ecommerce monitoring, product comparison, and marketplace seller lookup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Walmart search terms, product IDs, seller IDs, and related lookup parameters are sent to Scavio.

Mitigation: Use only approved non-sensitive lookup data, and avoid confidential watchlists, sensitive competitive research, personal data, or regulated information unless that transfer is approved.

Risk: Search and category requests can cost more credits when targeting walmart.com.mx.

Mitigation: Check the response credits_used field and state the domain-based cost rule before making or recommending search and category requests.

Risk: The Walmart API may return warnings when retired parameters are ignored, which can make an apparently successful request misleading.

Mitigation: Surface any warnings returned by the API and retry with supported parameters when needed.

Risk: Generated retail guidance can be wrong if product names, prices, ratings, availability, or seller details are inferred instead of read from the API response.

Mitigation: Report only values returned by the API and include product URLs so users can verify details before taking action.

## Reference(s):

- [Scavio Walmart API documentation](https://scavio.dev/docs/walmart-api)
- [Scavio Walmart product documentation](https://scavio.dev/docs/walmart-product)
- [Scavio Walmart reviews documentation](https://scavio.dev/docs/walmart-reviews)
- [Scavio Walmart category documentation](https://scavio.dev/docs/walmart-category)
- [Scavio Walmart offers documentation](https://scavio.dev/docs/walmart-offers)
- [Scavio Walmart seller documentation](https://scavio.dev/docs/walmart-seller)
- [Scavio Walmart seller products documentation](https://scavio.dev/docs/walmart-seller-products)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with API request examples and structured JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and sends selected Walmart lookup parameters to Scavio.]

## Skill Version(s):

3.0.3 (source: server release metadata; artifact frontmatter is 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

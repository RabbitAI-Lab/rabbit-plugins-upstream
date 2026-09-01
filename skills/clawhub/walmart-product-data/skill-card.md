## Description:

Search Walmart and read product detail, reviews, category listings, buy-box offers, seller storefronts and a seller's catalog as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Walmart product search results, item details, customer reviews, category listings, buy-box offer data, and seller information through Scavio's structured JSON API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Walmart queries are sent to Scavio and may reveal product research intent to a third-party service.

Mitigation: Use the skill only when sending the query to Scavio is acceptable for the workflow and data policy.

Risk: API calls consume Scavio credits, with search and category calls costing more for walmart.com.mx.

Mitigation: Review credits_used and credits_remaining in responses and state the domain-based credit rule before cost-sensitive use.

Risk: SCAVIO_API_KEY is required for API access.

Mitigation: Keep SCAVIO_API_KEY in the environment or a secret store and do not place live keys in source files or shared transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/walmart-product-data)
- [Scavio Walmart API documentation](https://scavio.dev/docs/walmart-api)
- [Scavio Walmart product documentation](https://scavio.dev/docs/walmart-product)
- [Scavio Walmart reviews documentation](https://scavio.dev/docs/walmart-reviews)
- [Scavio Walmart category documentation](https://scavio.dev/docs/walmart-category)
- [Scavio Walmart offers documentation](https://scavio.dev/docs/walmart-offers)
- [Scavio Walmart seller documentation](https://scavio.dev/docs/walmart-seller)
- [Scavio Walmart seller products documentation](https://scavio.dev/docs/walmart-seller-products)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and inline bash or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls consume Scavio credits and return credits_used and credits_remaining in the response envelope.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

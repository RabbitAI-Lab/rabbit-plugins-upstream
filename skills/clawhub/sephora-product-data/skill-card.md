## Description:

Search Sephora’s U.S. catalog and retrieve structured product details, including prices, ratings, variations, ingredients, availability, and review sentiment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Shopping assistants use this skill to search Sephora products and present current prices, ratings, available shades or sizes, ingredients, and review summaries.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Searches, product requests, optional ZIP codes, and the API credential are sent to Scavio.

Mitigation: Keep the API key in an environment variable or secret store, and provide a ZIP code only when same-day eligibility is needed.

Risk: Each endpoint consumes API credits, so repeated lookups can use the account balance.

Mitigation: Monitor credit usage and check the balance before running large or repeated searches.

## Reference(s):

- [Sephora API overview](https://scavio.dev/sephora-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=sephora-product-data)
- [Sephora search endpoint](https://scavio.dev/docs/sephora-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=sephora-product-data)
- [Sephora category endpoint](https://scavio.dev/docs/sephora-category?utm_source=agent-skills&utm_medium=skill&utm_campaign=sephora-product-data)
- [Sephora product endpoint](https://scavio.dev/docs/sephora-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=sephora-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=sephora-product-data)

## Skill Output:

**Output Type(s):** [JSON data]

**Output Format:** [Structured JSON product search results, category listings, and product details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listings can contain up to 60 products per page; product details include available variations and review sentiment summaries.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

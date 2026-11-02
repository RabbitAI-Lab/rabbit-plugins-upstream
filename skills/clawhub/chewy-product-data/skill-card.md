## Description:

Chewy product data as structured JSON - search chewy.com or browse a category, 36 products per page, with the one-time price, Autoship price and discount, first-Autoship price and savings cap, strike-through and per-unit price, rating and rating count; and read one product with list, offer and MAP price, star distribution, review count, GTIN, specifications, ingredients and feeding details, promotions and every size and flavor variant. 2 endpoints, 10 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find Chewy pet products, compare one-time and Autoship prices, and retrieve product details such as ratings, ingredients, and variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup requests and the API key are sent to Scavio.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store.

Risk: Repeated or bulk lookups can consume credits.

Mitigation: Plan the number of calls and review credit costs before running bulk queries.

Risk: Optional SDK and MCP packages have not been independently reviewed.

Mitigation: Assess the packages separately before installing or enabling them.

## Reference(s):

- [Chewy search API documentation](https://scavio.dev/docs/chewy-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=chewy-product-data)
- [Chewy product API documentation](https://scavio.dev/docs/chewy-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=chewy-product-data)
- [Chewy API overview](https://scavio.dev/chewy-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=chewy-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=chewy-product-data)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON product and category data, with concise guidance as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each API call costs 10 credits; prices and product details reflect the returned data.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

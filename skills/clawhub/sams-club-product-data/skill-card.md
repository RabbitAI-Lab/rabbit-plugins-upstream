## Description:

Sam's Club product data as structured JSON - search, item detail with the club shelf price, Instant Savings, stock and aisle at the club you choose, a club locator by ZIP, every Instant Savings item, category and clearance listings, and paged member reviews. 6 endpoints, 1 credit each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find Sam's Club products, compare prices and offers, check club-specific inventory and aisle details, locate nearby clubs, and retrieve member reviews.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Search terms, ZIP codes, and product identifiers are sent to Scavio; its data-retention practices were not verified.

Mitigation: Send only the information needed for the lookup and consult Scavio's current data-retention terms before using sensitive queries.

Risk: Each endpoint call consumes API credits, and the API key should be treated as a secret.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store, and monitor credit usage.

Risk: Optional SDK and MCP packages execute external code whose internals were not reviewed.

Mitigation: Review the package and its permissions before installing or running it; use direct API calls when package review is not available.

## Reference(s):

- [Sam's Club API overview](https://scavio.dev/samsclub-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=sams-club-product-data)
- [Sam's Club product API documentation](https://scavio.dev/docs/samsclub-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=sams-club-product-data)
- [Sam's Club search API documentation](https://scavio.dev/docs/samsclub-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=sams-club-product-data)
- [Sam's Club clubs API documentation](https://scavio.dev/docs/samsclub-clubs?utm_source=agent-skills&utm_medium=skill&utm_campaign=sams-club-product-data)
- [Sam's Club savings API documentation](https://scavio.dev/docs/samsclub-savings?utm_source=agent-skills&utm_medium=skill&utm_campaign=sams-club-product-data)
- [Sam's Club category API documentation](https://scavio.dev/docs/samsclub-category?utm_source=agent-skills&utm_medium=skill&utm_campaign=sams-club-product-data)
- [Sam's Club reviews API documentation](https://scavio.dev/docs/samsclub-reviews?utm_source=agent-skills&utm_medium=skill&utm_campaign=sams-club-product-data)
- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/sams-club-product-data)

## Skill Output:

**Output Type(s):** [JSON, Product data, Retail availability and reviews]

**Output Format:** [Structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint-specific product, club, price, savings, inventory, and review fields; list results are paginated.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

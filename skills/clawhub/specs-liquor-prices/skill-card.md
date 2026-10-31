## Description:

Spec's Wines, Spirits & Finer Foods (Texas) data as structured JSON - product search, product detail with every store's price and stock in one call, and a store locator by region. 3 endpoints, 5 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to search Spec's products, compare current online and store prices or stock, and locate stores by Texas region.

### Deployment Geography for Use:

Texas, United States

## Known Risks and Mitigations:

Risk: Search queries and the selected store or region are sent to Scavio.

Mitigation: Avoid including sensitive personal details and send only the search and location information needed for the lookup.

Risk: Each endpoint call consumes five credits, so repeated lookups can use the account balance quickly.

Mitigation: Track the credit balance and limit calls to the lookups needed.

Risk: The optional MCP package contents were not independently audited.

Mitigation: Review the package and enable only the MCP platforms needed before setup.

## Reference(s):

- [Spec's product API documentation](https://scavio.dev/docs/specs-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=specs-liquor-prices)
- [Spec's search API documentation](https://scavio.dev/docs/specs-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=specs-liquor-prices)
- [Spec's store locator API documentation](https://scavio.dev/docs/specs-stores?utm_source=agent-skills&utm_medium=skill&utm_campaign=specs-liquor-prices)
- [Spec's API overview](https://scavio.dev/specs-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=specs-liquor-prices)

## Skill Output:

**Output Type(s):** [JSON, API data]

**Output Format:** [Structured JSON containing product, price, stock, and store details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices are integers in cents; each endpoint call uses five credits.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

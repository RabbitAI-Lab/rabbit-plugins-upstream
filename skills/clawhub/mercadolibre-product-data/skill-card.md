## Description:

Helps agents retrieve Mercado Libre product searches, listing details, reviews, buyer questions, and category best sellers through Scavio's structured data API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and commerce analysts use this skill to compare listings and prices, inspect products and customer feedback, research sellers, and identify category best sellers in supported Latin American marketplaces.

### Deployment Geography for Use:

Global (data coverage: Mexico, Brazil, Argentina, and Colombia; best sellers exclude Brazil)

## Known Risks and Mitigations:

Risk: Search terms, product URLs or IDs, seller identifiers, and the Scavio API key are sent to Scavio.

Mitigation: Use the connector only when sharing these details with Scavio is acceptable; keep the API key in a secret store or environment variable.

Risk: Pagination and repeated searches can consume paid API credits.

Mitigation: Set a request budget and check remaining credits before loops or pagination.

Risk: Optional SDK or MCP installation runs third-party packages.

Mitigation: Install the optional Scavio packages only if you trust their publisher and need those integrations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/mercadolibre-product-data)
- [Mercado Libre search API documentation](https://scavio.dev/docs/mercadolibre-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=mercadolibre-product-data)
- [Product API documentation](https://scavio.dev/docs/mercadolibre-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=mercadolibre-product-data)
- [Reviews API documentation](https://scavio.dev/docs/mercadolibre-reviews?utm_source=agent-skills&utm_medium=skill&utm_campaign=mercadolibre-product-data)
- [Questions API documentation](https://scavio.dev/docs/mercadolibre-questions?utm_source=agent-skills&utm_medium=skill&utm_campaign=mercadolibre-product-data)
- [Best sellers API documentation](https://scavio.dev/docs/mercadolibre-best-sellers?utm_source=agent-skills&utm_medium=skill&utm_campaign=mercadolibre-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=mercadolibre-product-data)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with structured JSON results and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices are in local currency; results and reviews can be paginated, and API requests consume credits.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

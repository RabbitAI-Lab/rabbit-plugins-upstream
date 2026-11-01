## Description:

HEB grocery data as structured JSON - product search, full item detail with pricing and nutrition, and store locator, with per-store prices, stock and aisle location via store_id. 3 endpoints, 2 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and agents can search HEB products, retrieve product details, compare store-specific prices and availability, and find nearby stores. Developers can use the returned product, nutrition, and store data to answer grocery questions or enrich catalogs.

### Deployment Geography for Use:

United States; HEB stores are primarily in Texas.

## Known Risks and Mitigations:

Risk: Grocery searches, city or ZIP queries, and selected store identifiers are sent to Scavio.

Mitigation: Send only the search and location details needed for the lookup; use direct API calls or an HEB-only MCP configuration to limit enabled tools.

Risk: API requests consume account credits and require a secret API key.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, out of source code, and monitor credit use.

## Reference(s):

- [HEB search API documentation](https://scavio.dev/docs/heb-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB product API documentation](https://scavio.dev/docs/heb-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB store locator API documentation](https://scavio.dev/docs/heb-stores?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB API overview](https://scavio.dev/heb-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [Scavio account setup](https://dashboard.scavio.dev/sign-up?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON records with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices are returned in cents; prices, stock, and aisle details can vary by store. Each endpoint request uses 2 credits.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

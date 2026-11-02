## Description:

Menards product data as structured JSON - search menards.com at the store you choose with each result's price, sale price, mail-in rebate, final price after rebate and that store's stock count; read one product by item id or URL with the full price ladder, specifications, images and documents, plus a store's stock quantity and aisle location; and find Menards stores near a ZIP or city. 3 endpoints; search 2 credits, product 1 (2 with a store), stores 1.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find Menards products, compare current prices and rebates, check stock and aisle details at a selected store, and locate nearby stores.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Search terms, selected products, and supplied ZIP code or city and state are sent to Scavio, and API calls consume credits.

Mitigation: Use only the search and location details needed for the request, and check credit costs before making calls.

Risk: The optional SDK and MCP packages have not been independently verified, and Scavio's data-retention practices were not verified in this review.

Mitigation: Review optional packages separately before use and enable only the MCP platforms needed.

Risk: The Scavio API key could be exposed if stored in source code or shared configuration.

Mitigation: Keep the key in an environment variable or secret store.

## Reference(s):

- [Menards search API documentation](https://scavio.dev/docs/menards-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=menards-product-data)
- [Menards product API documentation](https://scavio.dev/docs/menards-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=menards-product-data)
- [Menards stores API documentation](https://scavio.dev/docs/menards-stores?utm_source=agent-skills&utm_medium=skill&utm_campaign=menards-product-data)
- [Menards API overview](https://scavio.dev/menards-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=menards-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=menards-product-data)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON product, pricing, rebate, store inventory, and store location data, with user-facing summaries as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are store-specific where requested; endpoint calls consume credits.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

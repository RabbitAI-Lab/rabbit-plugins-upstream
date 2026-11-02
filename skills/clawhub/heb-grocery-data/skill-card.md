## Description:

HEB grocery data as structured JSON - product search, full item detail with pricing and nutrition, and store locator, with per-store prices, stock and aisle location via store_id. Also HEB Mexico (heb.com.mx) with peso prices, units in stock and promotions. 3 endpoints, 2 credits each.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search HEB products, retrieve product details such as prices and nutrition, check store-specific availability, and locate nearby US stores. It also supports product and pricing lookups on HEB Mexico.

### Deployment Geography for Use:

Texas, United States, and northeast Mexico for product data; the store locator covers US stores only.

## Known Risks and Mitigations:

Risk: Grocery searches and any ZIP code or city supplied for store lookup are shared with Scavio.

Mitigation: Provide only the location detail needed to find a store; use direct API calls or HEB-only MCP tools if those better fit the task.

Risk: Requests require an API key and each endpoint call costs two credits.

Mitigation: Keep SCAVIO_API_KEY private in an environment variable or secret store, and account for the per-request credit charge.

## Reference(s):

- [HEB API overview](https://scavio.dev/heb-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB search documentation](https://scavio.dev/docs/heb-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB product documentation](https://scavio.dev/docs/heb-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)
- [HEB stores documentation](https://scavio.dev/docs/heb-stores?utm_source=agent-skills&utm_medium=skill&utm_campaign=heb-grocery-data)

## Skill Output:

**Output Type(s):** [API Calls, Structured data, Guidance]

**Output Format:** [Structured JSON results with concise natural-language answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices, stock, and aisle data may be store-specific; Mexico product data uses the default HEB Mexico store.]

## Skill Version(s):

1.2.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

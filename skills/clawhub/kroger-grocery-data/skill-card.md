## Description:

Search Kroger-family banners for grocery products and retrieve item details with pricing and nutrition as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search Kroger-family banners and retrieve grocery product details, including prices, availability, nutrition, and ingredients, by query, product URL, or UPC.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs are sent to Scavio, and requests consume API credits.

Mitigation: Send only the query or product identifiers needed, review per-request costs, and monitor credit usage.

Risk: An exposed SCAVIO_API_KEY could enable unauthorized API use.

Mitigation: Keep the key in an environment variable or secret store and out of source control.

Risk: The optional MCP example enables default platforms in addition to Kroger.

Mitigation: Limit enabled MCP platforms to those required for the task.

## Reference(s):

- [Kroger search documentation](https://scavio.dev/docs/kroger-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=kroger-grocery-data)
- [Kroger product documentation](https://scavio.dev/docs/kroger-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=kroger-grocery-data)
- [Kroger API overview](https://scavio.dev/kroger-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=kroger-grocery-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=kroger-grocery-data)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/kroger-grocery-data)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured JSON product search results and product details, with Markdown setup and usage guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include retrieval timestamps and credit metadata; online prices and availability may differ from in-store conditions.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

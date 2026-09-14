## Description:

Search TikTok Shop products with exact prices, read product details, reviews, the category tree, category and seller catalogs, and resolve any TikTok Shop link to an id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce teams use this skill to query TikTok Shop product, seller, category, price, and review data through Scavio's API for catalog research, competitive analysis, and review mining.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls require a Scavio API key and send requested TikTok Shop lookup data to Scavio.

Mitigation: Use an appropriate Scavio account, keep SCAVIO_API_KEY in environment or secret storage, and avoid submitting sensitive lookup data unless that data sharing is acceptable.

Risk: Scavio requests consume credits, including some product-detail calls that return expected 404 responses.

Mitigation: Prefer listing endpoints for price and catalog workflows, handle 404 product-detail responses as normal outcomes, and monitor credit balance before broad collection runs.

Risk: TikTok Shop coverage varies by endpoint and region, and product detail does not return exact prices.

Mitigation: Use search, category products, or shop products as the price source, respect documented regional coverage, and avoid estimating missing values.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/tiktok-shop-api)
- [Scavio TikTok Shop API Documentation](https://scavio.dev/docs/tiktok-shop-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-shop-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, JSON]

**Output Format:** [Markdown guidance with shell and code examples for JSON API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; responses are structured JSON from Scavio API endpoints.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

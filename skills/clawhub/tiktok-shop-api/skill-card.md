## Description:

Search TikTok Shop products with exact prices, read product details and reviews, browse category and seller catalogs, and resolve TikTok Shop links to product or shop IDs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agent builders use this skill to query TikTok Shop product, pricing, review, category, seller, and link-resolution data through Scavio's API.

### Deployment Geography for Use:

Global, with endpoint-level TikTok Shop region coverage limited as documented by the publisher.

## Known Risks and Mitigations:

Risk: Search terms, product IDs, shop IDs, and TikTok Shop URLs are sent to Scavio.

Mitigation: Use the skill only for data the user is permitted to share with Scavio, and avoid sending confidential identifiers or sensitive URLs.

Risk: Each endpoint call consumes Scavio API credits.

Mitigation: Batch or paginate deliberately, prefer larger supported review page sizes when appropriate, and confirm cost-sensitive workflows before making repeated calls.

Risk: Returned review, seller, and product data may carry privacy or compliance obligations.

Mitigation: Handle returned data according to the user's privacy, retention, and compliance requirements before storing, sharing, or reusing it.

Risk: Some product details may not resolve, and product prices are only authoritative from listing endpoints.

Mitigation: Treat product-detail 404s as expected, avoid retry loops, and use search, shop product, or category product listings for exact prices.

## Reference(s):

- [Scavio TikTok Shop API documentation](https://scavio.dev/docs/tiktok-shop-search)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/tiktok-shop-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoint responses are structured JSON and each endpoint call consumes one API credit.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

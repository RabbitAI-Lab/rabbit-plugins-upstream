## Description:

Search TikTok Shop products with exact prices, read product details, reviews, the category tree, category and seller catalogs, and resolve any TikTok Shop link to an id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and e-commerce operators use this skill to search TikTok Shop product listings, inspect product and seller details, mine reviews, browse categories, and resolve TikTok Shop links through Scavio's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and do not commit it to source code.

Risk: TikTok Shop search terms, product IDs, shop IDs, and URLs are sent to Scavio's API.

Mitigation: Use the skill only when those lookup inputs are appropriate to share with Scavio.

Risk: Pagination or loops across many products can consume Scavio credits.

Mitigation: Limit result depth, monitor remaining credits, and avoid unbounded retries or pagination.

Risk: Product detail lookups may return normal 404 responses and product detail does not provide exact prices.

Mitigation: Treat detail 404s as expected misses, avoid retry loops, and use listing endpoints for exact prices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/tiktok-shop-api)
- [Scavio TikTok Shop API documentation](https://scavio.dev/docs/tiktok-shop-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-shop-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=tiktok-shop-api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API Calls]

**Output Format:** [Markdown with bash, Python, JSON, and endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are structured JSON; calls require SCAVIO_API_KEY and consume Scavio credits.]

## Skill Version(s):

1.0.2 (source: release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

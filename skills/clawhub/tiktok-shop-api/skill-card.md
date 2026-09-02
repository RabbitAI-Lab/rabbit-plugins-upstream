## Description:

Search TikTok Shop products with exact prices, read product details, reviews, the category tree, category and seller catalogs, and resolve any TikTok Shop link to an id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and e-commerce researchers use this skill to query TikTok Shop product, price, review, category, and shop catalog data through Scavio for market research, competitor tracking, and review mining.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Scavio API key for TikTok Shop lookups.

Mitigation: Install it only where the agent may use SCAVIO_API_KEY, and keep the key in the environment or a secret store rather than source text.

Risk: Bulk searches, pagination, review mining, and some 404 product-detail responses consume API credits.

Mitigation: Warn users before large loops, monitor credits_remaining, use larger review page sizes where appropriate, and avoid retrying expected product-detail 404s.

Risk: Product detail lookups are incomplete for many search result ids and do not return exact prices.

Mitigation: Use listing endpoints for exact prices, branch on HTTP status for product-detail 404s, and present missing fields as unavailable rather than estimating them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/tiktok-shop-api)
- [Scavio TikTok Shop API documentation](https://scavio.dev/docs/tiktok-shop-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON, API calls]

**Output Format:** [Markdown guidance with JSON examples, bash curl commands, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses include credit usage and remaining balance.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

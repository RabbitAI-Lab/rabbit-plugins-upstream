## Description:

Search TikTok Shop products with exact prices, read product details, reviews, the category tree, category and seller catalogs, and resolve any TikTok Shop link to an id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce researchers use this skill to query TikTok Shop product, seller, category, review, price, and link-resolution data through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok Shop lookup inputs to Scavio using a Scavio API key.

Mitigation: Use the skill only when the user is comfortable sharing those lookup inputs with Scavio and provide the API key through the required SCAVIO_API_KEY environment variable.

Risk: API calls consume credits, including some product-detail lookups that return 404 because upstream product detail is unavailable.

Mitigation: Ask before large pagination, bulk detail collection, or bulk review collection, and treat documented product-detail 404 responses as normal non-retry outcomes.

Risk: Some endpoints have regional or data-coverage limits, so product detail, pricing, reviews, or category listings may be incomplete for a requested workflow.

Mitigation: Use listing endpoints for exact prices, avoid estimating missing prices, and clearly report unavailable or unsupported data instead of filling gaps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-tiktok-shop)
- [Scavio TikTok Shop API documentation](https://scavio.dev/docs/tiktok-shop-search)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration, text]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces API usage guidance for agents; live results are returned by Scavio as structured JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

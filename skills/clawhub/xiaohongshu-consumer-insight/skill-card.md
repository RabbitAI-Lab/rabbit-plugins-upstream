## Description:

Analyzes a Xiaohongshu post and its share-page comments to summarize its audience, claims, concerns, purchase intent, products, prices, and questions, with source quotes checked against the available content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External product and marketing teams can use the skill to review Xiaohongshu posts for product selection, competitor feedback, selling points, customer concerns, and purchase signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Post links and supplied share text are sent to LinkDigest for processing.

Mitigation: Review links before submitting and avoid sending private or sensitive material.

Risk: Reading a post and optional insight or question features can consume service credits.

Mitigation: Check the credit cost before running; use the --max-credits option when a spending cap is needed.

## Reference(s):

- [LinkDigest Xiaohongshu consumer insight](https://linkdigest.dev/zh/xiaohongshu-shichang-diaoyan?ref=skill-xiaohongshu-consumer-insight)
- [LinkDigest API key setup](https://linkdigest.dev/signin?ref=skill-xiaohongshu-consumer-insight&next=/app/keys)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [LinkDigest MCP endpoint](https://linkdigest.dev/mcp)
- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/xiaohongshu-consumer-insight)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown or JSON consumer-insight results]

**Output Parameters:** [1D (one post per analysis)]

**Other Properties Related to Output:** [Insight items include source quotes and a verified flag. Private, deleted, login-gated posts, and comments beyond those shown on the share page may be unavailable.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

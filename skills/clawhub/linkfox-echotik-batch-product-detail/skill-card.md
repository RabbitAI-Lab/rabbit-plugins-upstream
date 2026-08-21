## Description:

Fetches detailed EchoTik/TikTok Shop product analytics in batches, including multi-period sales, GMV, livestream, video, influencer, pricing, rating, review, commission, and status metrics for known product IDs or TikTok Shop URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and commerce analysts use this skill to compare known TikTok Shop products side by side using product-detail, sales, GMV, livestream, video, influencer, price, rating, review, commission, and availability data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product IDs and TikTok Shop URLs are sent to LinkFox/EchoTik for lookup.

Mitigation: Use the skill only when the user is comfortable sharing those product identifiers or URLs with LinkFox/EchoTik.

Risk: The skill writes full responses, caches, and possible payment QR artifacts locally.

Mitigation: Run it in an appropriate workspace, limit access to saved files, and clean up local response, cache, or QR files when they contain business-sensitive data.

Risk: Authentication, SMS login, API-key generation, recharge, and payment-order flows are sensitive.

Mitigation: Prefer self-service API-key setup, avoid sharing SMS codes through the agent unless necessary, and confirm any paid plan or order before proceeding.

Risk: Sales, GMV, attribution, and product-performance metrics are analytics estimates rather than exact platform figures.

Mitigation: Present the data as estimated analytics and avoid treating it as authoritative financial reporting.

## Reference(s):

- [EchoTik-TikTok商品批量详情 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-batch-product-detail)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and comparison tables, JSON request/response data, saved JSON files, and shell commands or configuration snippets for authentication and billing flows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are persisted under a workspace linkfox directory; small responses may also be printed inline, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

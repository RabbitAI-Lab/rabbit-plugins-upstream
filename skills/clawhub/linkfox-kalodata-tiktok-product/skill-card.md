## Description:

Queries Kalodata-powered TikTok Shop product leaderboards and product details by region, currency, language, date range, and productId.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, product researchers, and developers use this skill to discover TikTok Shop best-selling products and retrieve product-level pricing, sales, revenue, commission, category, shop, video, livestream, and creator metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network calls to LinkFox/Kalodata services and each lookup may consume paid credits.

Mitigation: Confirm the user's intent before repeated lookups, reuse the 24-hour cache for identical parameters, and clearly disclose additional credit consumption before continuing.

Risk: The onboarding flow can handle phone numbers, SMS codes, generated API keys, and payment orders.

Mitigation: Prefer self-service key setup, avoid collecting verification codes unless the user explicitly chooses scripted registration or login, and treat printed API keys as secrets.

Risk: The scripts save full API responses locally, which may include product research data and account-related context.

Mitigation: Store outputs only in the intended workspace, review saved files before sharing, and remove response files when they are no longer needed.

Risk: Automatic feedback reporting may send skill-use feedback to a LinkFox endpoint.

Mitigation: Use feedback reporting only when it matches the documented conditions and avoid including unnecessary sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-product)
- [Kalodata-TikTok商品搜索与详情 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables with JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved locally; small responses may also print complete JSON, while large responses print summaries.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

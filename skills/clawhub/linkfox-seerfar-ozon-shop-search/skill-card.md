## Description:

Seerfar Ozon 店铺商品搜索：按 Ozon 店铺（卖家）ID 拉取该店铺的商品列表，返回每个商品的近30天销量、价格、评分、重量、配送方式（FBO/FBS）、卖家类型（本土/跨境）、退货取消率，以及店铺近30天总销量。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce analysts use this skill to retrieve and compare one Ozon shop's product catalog, 30-day sales metrics, pricing, ratings, fulfillment model, seller type, and shop-level sales totals. It supports competitor shop analysis, best-seller discovery, and seller catalog breakdowns when the user has a Seerfar/Ozon seller ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API credentials and can guide phone/SMS onboarding.

Mitigation: Prefer a pre-created, limited-scope API key and only provide phone or SMS details when intentionally setting up access.

Risk: The skill includes paid-credit purchase and billing flows.

Mitigation: Confirm costs and user intent before running purchase or order commands.

Risk: The skill stores full API responses and generated files locally under linkfox directories.

Mitigation: Review saved files after use and delete local response data that should not persist.

Risk: Endpoint environment variables can redirect LinkFox requests.

Mitigation: Keep default LinkFox endpoints unless an alternate endpoint is explicitly trusted.

Risk: The skill can submit feedback automatically based on user reactions or observed issues.

Mitigation: Avoid including sensitive information in feedback content and review feedback behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-shop-search)
- [Seerfar Ozon shop search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance]

**Output Format:** [Markdown summaries and tables, shell commands, and saved JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under linkfox session data directories, summarizes large responses by default, and uses a 24-hour local cache for repeated calls.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

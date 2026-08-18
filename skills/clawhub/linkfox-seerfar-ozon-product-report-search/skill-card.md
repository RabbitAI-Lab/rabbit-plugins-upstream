## Description:

Searches Seerfar's Ozon product database and returns product-level report rows filtered by sales, revenue, price, conversion, rating, brand, seller, fulfillment, listing age, and related metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and analysts use this skill to screen Ozon products, mine best sellers, compare competitor products, and inspect product-level performance reports from Seerfar data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkFox receives Ozon query data, API credentials, and optional phone-based login data during onboarding.

Mitigation: Use the skill only with trusted LinkFox endpoints, protect LINKFOX_AGENT_API_KEY, and do not set LINKFOX_* URL override variables unless the destination is trusted.

Risk: The skill can consume credits and includes billing flows for account recharge or plan purchase.

Mitigation: Tell users before repeated paid calls and require an explicit user choice before continuing with additional credit-consuming requests or payment actions.

Risk: Full search responses are saved locally and may contain commercially sensitive product-analysis data.

Mitigation: Review generated linkfox session files before sharing, committing, or retaining them, and remove sensitive local outputs when no longer needed.

## Reference(s):

- [Seerfar Ozon 商品报表搜索 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-product-report-search)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and summaries with persisted JSON response files; onboarding helpers emit stdout JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a linkfox session data directory; large responses print a summary unless --inline is used.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

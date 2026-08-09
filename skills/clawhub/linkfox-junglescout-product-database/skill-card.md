## Description:

Jungle Scout-商品库 helps agents filter Amazon products across 10 marketplaces by category, price, sales, revenue, reviews, rating, BSR rank, LQS, seller type, and related criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to discover and compare Amazon products by market, category, sales, price, competition, listing quality, and fulfillment filters. Agents use it to build LinkFox Jungle Scout product database queries, present product results, and guide credential or billing recovery when required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API credentials and can help create or retrieve API keys through phone and SMS login flows.

Mitigation: Use a dedicated LinkFox account or scoped credential when possible, and provide phone numbers or SMS codes only when you intend to link that account.

Risk: The onboarding flow can list paid plans, create orders, and render payment QR codes for LinkFox billing.

Mitigation: Confirm the selected plan and payment method with the user before ordering, and do not submit payment choices unless the user intends to fund the account.

Risk: Product query results are written locally under linkfox session data directories and repeated query responses may be cached for 24 hours.

Mitigation: Avoid sensitive product searches unless local storage is acceptable, review where response files are saved, and remove local result or cache files when retention is not desired.

Risk: The skill includes automatic feedback reporting when behavior, results, or user sentiment indicate feedback should be sent.

Mitigation: Do not include sensitive user or product-research details in feedback content, and review feedback payloads before sending when the agent workflow allows.

## Reference(s):

- [Jungle Scout 产品数据库查询 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-product-database)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON API parameters, tabular product summaries, shell commands, and saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The product query script saves complete responses under a linkfox session data directory, uses a 24-hour local cache for repeated parameter sets, and summarizes responses larger than 8 KB unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

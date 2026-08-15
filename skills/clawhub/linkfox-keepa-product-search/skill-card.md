## Description:

Helps Amazon sellers and e-commerce researchers search and filter Amazon products with Keepa-backed criteria such as category, price, monthly sales, BSR, ratings, reviews, dimensions, weight, fulfillment, and historical sales rank.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and product researchers use this skill to build multi-criteria Keepa product searches and review the resulting product metrics. It is suited to product discovery, BSR and sales filtering, category screening, competitor research, and historical sales analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags broad activation, account and SMS onboarding, API-token generation, payment flows, automatic feedback reporting, and persistent local storage.

Mitigation: Install only when the user intends to use LinkFox as a paid, account-backed Keepa provider; prefer self-service API-key setup and review generated LinkFox files after use.

Risk: Searches can consume paid LinkFox credits and historical data can increase cost.

Mitigation: Confirm before any credit-consuming search or purchase step, avoid automatic retries or query expansion, and explain additional cost before continuing.

Risk: The skill stores full search responses locally, which may include product research data and query context.

Mitigation: Tell users where result files are saved and advise them to review or delete generated LinkFox files when finished.

## Reference(s):

- [Keepa Product Search Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-search)
- [Keepa-亚马逊-商品搜索 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Files, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown summaries and tables, JSON API responses saved to local files, and inline shell commands for setup or onboarding.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are summarized unless inline output is requested; full API responses are saved under a LinkFox session data directory.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

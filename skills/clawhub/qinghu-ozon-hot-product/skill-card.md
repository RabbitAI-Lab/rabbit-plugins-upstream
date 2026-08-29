## Description:

青虎AI Ozon 爆款跟卖与选品：拉取 Ozon 热卖产品榜与中国专区产品列表，批量看商品详情、产品趋势快照与信息追踪，锁定当前爆款与飙升款，分析价格带和销量结构，判断是做同款跟卖还是差异化改良。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and Ozon sellers use this skill to inspect hot-product rankings, China-zone product performance, item details, trend snapshots, and traffic keywords before deciding whether to follow, adapt, watch, or abandon candidate products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call a third-party Qinghu data service that may consume credits and requires an API token.

Mitigation: Require user approval before data-service calls, report Qinghu credit consumption from the response envelope, and keep credentials in user-provided secrets or environment variables.

Risk: Product-research exports or cached files may contain commercially sensitive marketplace analysis.

Mitigation: Treat generated exports and cached datasets as sensitive business data and share only the needed file links and brief previews.

Risk: Following Ozon products without legal review can create brand, patent, or marketplace-compliance exposure.

Mitigation: Present follow/adapt/watch/abandon recommendations as decision support and tell users to verify brand authorization, patent status, and platform compliance before listing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-hot-product)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional exported tabular files and JSON/API call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Qinghu API credentials, user approval before data-service calls, and concise previews when large result sets are exported.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

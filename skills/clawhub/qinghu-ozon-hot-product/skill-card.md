## Description:

青虎AI Ozon 爆款跟卖与选品：拉取 Ozon 热卖产品榜与中国专区产品列表，批量看商品详情、产品趋势快照与信息追踪，锁定当前爆款与飙升款，分析价格带和销量结构，判断是做同款跟卖还是差异化改良。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and ecommerce analysts use this skill to research Ozon hot products, compare general and China-zone rankings, inspect item details and trend snapshots, and decide whether to follow-sell, improve, watch, or reject candidate products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a Qinghu API token and instructs the agent to pass it in request headers.

Mitigation: Use a scoped Qinghu token where possible, provide it through the supported environment variables or direct user approval, and rotate or revoke it if it may have been exposed.

Risk: Large query results may be exported or cached as local spreadsheet files.

Mitigation: Avoid sensitive source data unless export locations and cleanup procedures are understood, and remove local cache or spreadsheet files after use when they are no longer needed.

Risk: Product-selection recommendations can be misleading if API calls fail, return partial data, or compare different periods or sites.

Mitigation: Follow the skill's success checks, label metrics with site and period, and review candidate products before acting on follow-selling, compliance, brand, or patent decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-hot-product)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown recommendations with concise previews and optional exported spreadsheet files for larger result sets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Qinghu API responses to produce candidate product lists, strategy labels, improvement suggestions, and data-delivery links when exports are created.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

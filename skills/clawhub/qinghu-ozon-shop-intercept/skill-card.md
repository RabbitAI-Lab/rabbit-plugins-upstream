## Description:

青虎AI Ozon 竞店截流帮助用户分析对标店铺的在售商品、店铺趋势、热销结构和潜力新品，用于复刻选品逻辑并制定竞店截流方案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and ecommerce analysts use this skill to inspect Ozon competitor shops, identify shop-level product and price patterns, monitor rising new products, and produce concise replication or interception recommendations. The workflow relies on Qinghu data APIs and requires the user to provide or authorize an appropriate Qinghu token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token and may call paid Qinghu tools.

Mitigation: Use only a token trusted for this purpose, review paid-call prompts before authorizing calls, and track charges from the returned pointCost values.

Risk: Competitor-shop recommendations can create brand, patent, or marketplace-policy exposure if copied without review.

Mitigation: Independently check brand authorization, patent status, and Ozon marketplace-policy compliance before acting on product replication or interception recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-shop-intercept)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow API check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-RPC request examples, concise analysis, and optional exported tabular files for larger datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shop profiles, product-matrix tables, potential-new-product lists, replication recommendations, Qinghu point-cost summaries, and file links when data is exported.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

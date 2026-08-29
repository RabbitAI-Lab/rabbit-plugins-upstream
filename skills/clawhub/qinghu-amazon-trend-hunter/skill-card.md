## Description:

青虎AI 亚马逊爆款趋势挖掘：在 Amazon 海量商品里按销量、销售额、BSR 增长、评分、评论数、利润率、卖家结构等多维条件筛选，挖出当前爆款与潜力热卖单品，并用历史趋势验证是真爆还是昙花一现。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, product researchers, and ecommerce operators use this skill to find current best-selling and rising-potential products across Amazon marketplaces. It helps screen by category or keyword, compare sales and competition signals, validate trends, and summarize opportunities and risks before product selection decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a Qinghu API key and may spend Qinghu credits when approved tool calls are made.

Mitigation: Confirm the marketplace, category or keyword, planned tool list, and expected credit use before authorizing Qinghu API requests.

Risk: Amazon sales, revenue, BSR, and profitability figures are third-party estimates rather than seller-backend records.

Mitigation: Treat findings as research signals and cross-check important product decisions with independent data sources and business review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-trend-hunter)
- [ClawHub publisher profile: autoagc](https://clawhub.ai/user/autoagc)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown summaries with optional tabular file exports and inline command or JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include opportunity rankings, ASIN-level product metrics, trend judgments, risk notes, and credit-consumption reporting when paid Qinghu API calls are made.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

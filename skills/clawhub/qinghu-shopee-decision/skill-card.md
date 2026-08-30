## Description:

青虎AI Shopee 选品决策：面向重大项目立项，一次串起站点大盘、类目榜单、店铺榜单、商品榜单与热搜词榜四条线，输出「大盘+竞店+爆款+搜词」的全景选品报告与多维度结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, ecommerce operators, and market analysts use this skill to decide whether to launch a category or product direction. It coordinates Qinghu market, category, shop, item, and search-term data into a conclusion-first selection report with supporting exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to make paid Qinghu data calls.

Mitigation: Require user approval before calls, use the returned pointCost for actual cost reporting, and avoid estimates that are not grounded in prior observed calls.

Risk: The skill requires a Qinghu API token for data access.

Mitigation: Use a dedicated low-privilege Qinghu token where possible and avoid exposing the token in reports, logs, or shared files.

Risk: Generated spreadsheet or report attachments may contain sensitive commercial analysis.

Mitigation: Review exported files before sharing and delete them after use in shared or sensitive environments.

Risk: Third-party market data may differ from Shopee seller-backend figures or local operational requirements.

Mitigation: Verify important decisions against authoritative seller, compliance, logistics, tax, and certification sources before committing investment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-decision)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu login](https://www.iqinghu.com/workbench/login?urlCode=agentch)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Structured Markdown report with exported spreadsheet attachments when result sets are large]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conclusion-first Shopee market analysis with concise previews and links to exported detail files.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

青虎AI Shopee 选品决策：面向重大项目立项，一次串起站点大盘、类目榜单、店铺榜单、商品榜单与热搜词榜四条线，输出「大盘+竞店+爆款+搜词」的全景选品报告与多维度结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers, ecommerce operators, and market analysts use this skill to decide whether a product category is worth a larger launch investigation. It coordinates Qinghu Shopee market APIs to compare site trends, categories, competitor stores, product rankings, search demand, price bands, and known launch risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can call paid Qinghu market-analysis tools and consume user credits.

Mitigation: Confirm the tools to be called, the authorization token, expected point costs, and user approval before running paid workflows.

Risk: Large result sets may be exported or cached as local files.

Mitigation: Confirm where exported spreadsheets or cached data files will be stored and avoid exposing sensitive business analysis paths or files.

Risk: Market data may differ from Shopee seller-backend figures or omit local compliance, tax, logistics, and certification details.

Mitigation: Treat the report as decision support and verify launch decisions against seller-backend data, compliance requirements, and operational constraints.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shopee-decision)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow permissions check](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, API Calls, Guidance]

**Output Format:** [Markdown report with optional exported spreadsheet files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are conclusion-first and may include local spreadsheet exports for result sets with 10 or more records.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

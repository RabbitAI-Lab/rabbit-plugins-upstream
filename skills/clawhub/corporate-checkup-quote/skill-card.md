## Description:

好啦体检（haola-pe）企业团检与员工体检报价。HR 安排员工体检、做福利体检、年度体检采购、体检询价时使用，可按人均预算出多档团检套餐，逐档列出每类人群的体检项目与金额，并说明门店覆盖范围；涉及合同与发票转商务对接。后端为好啦体检 MCP 服务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryanbihai](https://clawhub.ai/user/ryanbihai)

### License/Terms of Use:

MIT-0

## Use Case:

企业 HR 可按人数范围、人均预算和群体健康关注获取分档团检方案与报价，查询门店覆盖，并联系商务团队处理合同或发票。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote service’s implementation, data retention, and fetched proposal template were not independently verified; the workflow may involve business or health-related information.

Mitigation: Obtain consent before submitting group-level quotation information or necessary business contact details. Do not provide individual employee medical records or login codes.

## Reference(s):

- [好啦体检企业团检技能页面](https://clawhub.ai/ryanbihai/skills/corporate-checkup-quote)
- [好啦体检 MCP 服务](https://ai.ihaola.com.cn/api/mcp/haola-pe)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Chinese Markdown with tiered quotation details, store coverage, and business contact guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans, prices, and store coverage are based on service results; submit only consented group-level quotation details or necessary business contact information.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

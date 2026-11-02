## Description:

好啦体检（haola-pe）企业团检与员工体检报价。HR 安排员工体检、做福利体检、年度体检采购、体检询价时使用，可按人均预算出多档团检套餐，逐档列出每类人群的体检项目与金额，并说明门店覆盖范围；涉及合同与发票转商务对接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ryanbihai](https://clawhub.ai/user/ryanbihai)

### License/Terms of Use:

MIT-0

## Use Case:

HR and benefits teams use the skill to request employee health-check package quotes, compare tiers and covered locations, and contact the provider about corporate arrangements. It uses group-level workforce information; individual employee health records are outside its scope.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Employee health details could be included in information sent for a corporate inquiry.

Mitigation: Use aggregate workforce information only, and review the fields and recipient before approving a submission.

Risk: A changed service destination may not be trusted, and the remote service guidance has not been verified.

Mitigation: Keep the documented default endpoint unless another destination is intentionally trusted; review returned quote and coverage details before relying on them.

## Reference(s):

- [Project homepage](https://github.com/ryanbihai/haola-checkup-mcp)
- [ClawHub skill page](https://clawhub.ai/ryanbihai/skills/corporate-checkup-quote)
- [Haola PE service endpoint](https://ai.ihaola.com.cn/api/mcp/haola-pe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary of quote tiers, itemized package details, and location coverage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Specific prices and locations must come from service responses.]

## Skill Version(s):

1.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

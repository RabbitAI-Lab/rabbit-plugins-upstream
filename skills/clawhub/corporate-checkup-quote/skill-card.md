## Description:

帮助企业 HR 查询团体员工体检方案、分档报价与门店覆盖，并联系商务人员处理合同和发票事宜。

This skill is ready for commercial/non-commercial use.

## Publisher:

[haola](https://clawhub.ai/user/haola)

### License/Terms of Use:

MIT-0

## Use Case:

企业 HR 用它按人均预算查询员工团检方案和报价、核对门店覆盖，并发起合同、发票等商务咨询。它面向企业团检，不处理个人体检预约或个人报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quote and business inquiry submissions may include workforce health information.

Mitigation: Share only aggregate workforce details, omit individual employee records, and review the displayed fields before approving a submission.

Risk: The remote service's internal behavior, data retention, and hosted proposal instructions were not verified.

Mitigation: Review returned proposals and submission details before approval, and send only the information needed for the requested business task.

## Reference(s):

- [Declared project homepage (Clawdis metadata)](https://github.com/Beijing-Haola-Tech/haola-checkup-mcp)
- [haola-pe MCP service endpoint](https://ai.ihaola.com.cn/api/mcp/haola-pe)
- [ClawHub release page](https://clawhub.ai/haola/skills/corporate-checkup-quote)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Chinese text or Markdown summaries of returned quotations, checkup items, locations, and business contact guidance; setup instructions may include MCP configuration and Node.js commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Specific prices, items, locations, and availability must come from service responses; no unsupported estimates.]

## Skill Version(s):

1.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

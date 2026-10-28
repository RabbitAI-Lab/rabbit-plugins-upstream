## Description:

用 Cue 沿核心企业客户、供应商和招投标关系挖掘产业链上下游拓客名单，并为每家企业提供切入点和可能的金融需求。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

对公客户经理可从一家具体的核心企业出发，发现其客户、供应商和招投标关系中的潜在拓客对象。技能整理企业名单、关系线索、拜访切入点和可能的金融需求，供客户经理进一步核实和展业。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags automatic updates of executable code.

Mitigation: Review and pin the runner version, then disable automatic updates before use.

Risk: The security review reports conflicting assurances about API-key access.

Mitigation: Use a dedicated Cue key and understand how the agent handles it before sharing or configuring it.

Risk: Company queries are sent to Cue, research consumes credits, and the workflow discourages cancelling jobs midway.

Mitigation: Share only company information you are authorized to send, monitor credit use, and preserve the ability to stop jobs.

## Reference(s):

- [Cue 平台](https://cuecue.cn/)
- [企查查](https://www.qcc.com)
- [天眼查](https://www.tianyancha.com)
- [东方财富行业数据](https://data.eastmoney.com)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Structured Markdown prospecting report with relationship findings, company lists, outreach angles, inferred financial needs, priorities, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires one specific company as the starting point; the skill asks for a company name instead of running on an industry or raw material.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

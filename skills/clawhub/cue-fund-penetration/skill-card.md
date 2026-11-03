## Description:

用 Cue 穿透你的基金组合持仓——你以为分散了，其实买了一篮子同样的东西。逐层拆解股票/行业/风格暴露，检测重复配置与集中度风险，逐只排雷。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向个人基金投资者、基金投顾和研究人员，用于穿透公募基金公开持仓，检查组合中的个股重叠、行业集中度与风格暴露，并辅助组合诊断。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key may be exposed if shared in chat during setup.

Mitigation: Configure the key locally, protect its configuration file, and rotate any key already shared.

Risk: Portfolio queries are sent to Cue for analysis.

Mitigation: Submit only fund and portfolio details you are comfortable sharing with the external service.

## Reference(s):

- [Cue service](https://cuecue.cn/)
- [Cue runner repository cited in the skill documentation](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown report with fund holdings, overlap, industry concentration, style exposure, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis is based on publicly disclosed fund holdings, generally the top ten holdings in quarterly or annual reports, so data may lag.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

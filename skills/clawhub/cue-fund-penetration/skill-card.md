## Description:

用 Cue 穿透你的基金组合持仓——你以为分散了，其实买了一篮子同样的东西。逐层拆解股票/行业/风格暴露，检测重复配置与集中度风险，逐只排雷。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External investors and portfolio advisers use it to compare publicly disclosed top-ten holdings across Chinese public mutual funds, identify stock and sector overlap, and review concentration and style exposure.

### Deployment Geography for Use:

Global (focused on A-share mutual fund holdings)

## Known Risks and Mitigations:

Risk: The instructions ask users to send an API key in chat.

Mitigation: Configure the key locally in protected configuration or an environment variable; rotate any key already shared.

Risk: The workflow automatically updates an external runner before execution, and its behavior has not been verified.

Mitigation: Pin and inspect the runner before execution, then review updates explicitly.

Risk: Portfolio queries are sent to Cue and reports include share links.

Mitigation: Consider the sensitivity of portfolio details before submitting queries or distributing reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-fund-penetration)
- [Cue service](https://cuecue.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown portfolio report with tables and a Cue share link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Based on publicly disclosed top-ten holdings; reports may lag current holdings by one or more months.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

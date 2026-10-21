## Description:

根据用户提供的品牌或产品、目标受众、候选小红书达人和预算，比较蒲公英报价、粉丝画像与内容表现，并整理合作适配依据和待确认事项；不预测实际成交或投放回报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

品牌营销人员可依据用户给定的候选达人、目标受众和预算，比较可获取的商业数据并整理合作适配判断与补充资料需求。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commercial data queries consume paid credits, and costs vary by endpoint.

Mitigation: Confirm the query scope and credit budget first, then request only the endpoints needed for the evaluation.

Risk: The external CLI package runs locally with the SocialDataX API key available.

Mitigation: Obtain the key through the official SocialDataX site, prefer a reviewed fixed package version, and limit access to unrelated secrets.

## Reference(s):

- [SocialDataX API Key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-creator-collaboration-evaluation)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown comparison table with evidence-based recommendations and follow-up items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses returned data and its stated date ranges; distinguishes missing data and estimates from confirmed facts; does not predict actual ROI.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

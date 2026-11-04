## Description:

用户提供品牌或产品、目标受众、候选小红书达人和预算时，使用蒲公英报价、粉丝画像和内容表现比较合作适配度，交付候选对照表与待确认事项。SocialDataX 支持命令查询；不预测实际成交或投放回报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

品牌方和营销团队可用它比较用户指定的小红书达人候选，依据蒲公英报价、粉丝画像和内容表现整理合作适配度、预算依据及待确认事项。评估意见与接口数据分开呈现，不预测成交或投放回报。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Successful creator-data queries consume paid credits, so unnecessary endpoint calls can add cost.

Mitigation: Confirm the candidates, selected queries, and expected credit budget before use; query only the data needed for the evaluation.

Risk: An exposed API key could be misused, and the downloaded CLI package implementation was outside this artifact review.

Mitigation: Keep the key in supported secret storage and out of chat and version control; use a reviewed, fixed CLI version with limited permissions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-creator-collaboration-evaluation)
- [SocialDataX AI service and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown candidate comparison table with evidence and follow-up items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares only user-provided candidates; distinguishes returned data from recommendations and notes data scope and gaps.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

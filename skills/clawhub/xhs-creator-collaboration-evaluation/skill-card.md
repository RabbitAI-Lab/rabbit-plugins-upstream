## Description:

用户提供品牌或产品、目标受众、候选小红书达人和预算时，使用蒲公英报价、粉丝画像和内容表现比较合作适配度，交付候选对照表与待确认事项。SocialDataX 支持命令查询；不预测实际成交或投放回报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

品牌与营销团队可用此技能比较用户指定的小红书达人候选，结合报价、粉丝画像和内容表现评估预算与受众适配度，并整理依据及待确认事项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Successful commercial data queries consume credits.

Mitigation: Confirm the selected endpoints and expected total credit cost before querying.

Risk: The command examples use the latest CLI release, which may change.

Mitigation: For repeatable use, review and pin a vetted CLI version.

Risk: An API key could be exposed if copied into generated files.

Mitigation: Keep SOCIALDATAX_API_KEY in the environment and out of generated files.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown candidate comparison table with supporting notes and follow-up items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed data ranges and missing information; does not predict actual deals or campaign returns.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

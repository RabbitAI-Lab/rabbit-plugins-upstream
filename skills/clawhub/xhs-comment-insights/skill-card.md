## Description:

分析用户提供的小红书笔记评论，提炼用户反馈、痛点、需求、购买顾虑与可执行建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、产品调研人员、品牌调研人员和创作者可用它分析指定小红书笔记中已获取的评论与回复，整理主题、痛点、购买顾虑、未满足需求、FAQ 和行动建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided links, IDs, or share text are sent to SocialDataX for comment analysis.

Mitigation: Only provide links, IDs, or share text that you are comfortable sharing with SocialDataX.

Risk: API key exposure or unbounded requests can create credential and credit-use risks.

Mitigation: Store the API key securely, set page or item limits to control credit use, and prefer a reviewed fixed CLI version.

## Reference(s):

- [SocialDataX API key and service page](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown summary and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers fetched comments and replies only; may include themes, pain points, purchase concerns, unmet needs, FAQs, representative comments, and actionable suggestions.]

## Skill Version(s):

0.1.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

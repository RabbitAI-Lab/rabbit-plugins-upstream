## Description:

当用户需要分析小红书评论、用户反馈、痛点、需求、购买顾虑、FAQ、口碑或讨论时，本技能基于用户提供的笔记链接或 note_id 下的评论结果提供洞察。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容运营、产品与品牌研究人员及创作者，汇总指定小红书笔记的评论与回复，提炼主题、痛点、未满足需求、购买顾虑、FAQ 和可行动建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted note IDs, links, or share text are sent to SocialDataX.

Mitigation: Submit only the lookup information needed for the request; exclude unrelated sensitive information.

Risk: Package updates or execution of the npm program may introduce operational risk.

Mitigation: Review and pin a package version where possible; the read-only account-action scope does not sandbox the program.

Risk: Large comment or reply collections can incur API-credit costs.

Mitigation: Set page or item limits appropriate to the analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights)
- [SocialDataX skill and API information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown summaries and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are based only on returned comments and replies for the supplied note; distinguish quoted comment evidence from analysis.]

## Skill Version(s):

0.1.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

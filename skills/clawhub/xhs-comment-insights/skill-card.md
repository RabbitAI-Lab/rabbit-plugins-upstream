## Description:

当用户需要做小红书评论分析、小红书评论洞察、小红书用户反馈分析、小红书需求挖掘、痛点总结、购买顾虑整理、FAQ 提炼、口碑分析、评论回复观察或内容讨论复盘时使用。基于用户提供的小红书笔记链接或 note_id 下的评论结果，面向内容运营、产品调研、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、产品调研、品牌调研人员和创作者可基于指定小红书笔记的评论与回复，整理评论主题、用户痛点、购买顾虑、FAQ 和可执行建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned CLI package, so a compromised package update could access credentials or local resources during execution.

Mitigation: Review and verify the package release before running it, and keep API credentials in the intended private environment or credential store.

Risk: Submitted note details and comment text are sent to SocialDataX, and the skill evidence does not include a privacy disclosure for that transfer.

Mitigation: Tell users what note and comment data will be sent to SocialDataX and obtain their consent before making the request.

## Reference(s):

- [SocialDataX API Key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Comment themes, pain points, needs, FAQs, and recommendations based on the returned comments and replies; state the coverage represented by the fetched pages.]

## Skill Version(s):

0.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

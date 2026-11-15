## Description:

用于小红书评论分析、小红书评论回复、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Xiaohongshu / XHS / RedNote comments，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要了解小红书内容受众反馈的用户，用于读取评论与回复，并归纳讨论主题、情绪倾向、常见问题和痛点。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly runs an unpinned latest CLI, which can change at runtime and create supply-chain exposure.

Mitigation: Review the CLI release before use and pin a reviewed version where supported.

Risk: Submitted URLs or share text are sent to SocialDataX for comment retrieval.

Mitigation: Submit only content links or share text you are comfortable sending to the service.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-comments)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured comment data with concise thematic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paginated comments and replies; summarize observed themes before inferring sentiment or demand.]

## Skill Version(s):

0.1.22 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

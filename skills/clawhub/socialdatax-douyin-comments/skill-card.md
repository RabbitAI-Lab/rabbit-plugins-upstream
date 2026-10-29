## Description:

用于抖音评论分析、抖音评论回复、抖音评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Douyin comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Teams analyzing Douyin posts use this skill to retrieve first-level comments and replies, then summarize audience feedback, sentiment themes, objections, pain points, FAQs, and discussion topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI examples use @latest, so the installed package can change over time.

Mitigation: Pin a reviewed package version when reproducible behavior is needed.

Risk: Fetching comments and replies can incur API charges, especially when pagination continues until exhausted.

Mitigation: Set page or item limits to control usage; use --all only when complete pagination is intended.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-comments)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [JSON comment data with concise text or Markdown analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports paginated comments and replies; retrieval can be limited by page or item count.]

## Skill Version(s):

0.1.21 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

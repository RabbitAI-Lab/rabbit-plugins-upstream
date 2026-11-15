## Description:

用于抖音评论分析、抖音评论回复、抖音评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Douyin comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and analyze Douyin comments and replies, summarize audience feedback, and identify recurring discussion themes and pain points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repeated execution of the mutable `socialdatax-skills@latest` package could expose users to a compromised future release, especially when an API key is available.

Mitigation: Review the package release before use, and avoid supplying an API key to an unreviewed release; use a reviewed, pinned version when one is available.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Analysis, Markdown, Shell commands, Configuration instructions]

**Output Format:** [JSON comment data with concise Markdown summaries and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be paginated; summaries should state whether one or multiple pages were retrieved.]

## Skill Version(s):

0.1.23 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

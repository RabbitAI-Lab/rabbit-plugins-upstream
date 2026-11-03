## Description:

用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

外部用户和开发者可用它获取指定微博帖子的一级评论或评论回复，并按观察到的主题整理反馈、情绪、异议、痛点和常见问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key could be exposed through local configuration or logs.

Mitigation: Store it in the executing client's secret facility and keep it out of chat, logs, and generated skill files.

Risk: Unbounded comment or reply pagination can consume API credits, and the external CLI may change between runs.

Mitigation: Set page or item limits and prefer a reviewed, fixed CLI version over @latest.

Risk: The external npm implementation and publisher identity are unverified in the supplied security evidence.

Mitigation: Review the package and confirm the publisher before relying on it.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-comments)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Markdown analysis and summaries; JSON for direct CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can summarize one or multiple pages; paginated results include page and item counts and a continuation token.]

## Skill Version(s):

0.1.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

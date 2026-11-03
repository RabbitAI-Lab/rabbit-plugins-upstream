## Description:

用于快手评论分析、快手评论回复、快手评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Kuaishou / Kwai comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts, marketers, and creators use this skill to retrieve Kuaishou comments and replies, then summarize audience feedback, sentiment themes, objections, pain points, FAQs, and discussion topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external CLI was not included in this review and its local process permissions are not restricted by the skill's read-only description.

Mitigation: Prefer a reviewed, pinned CLI release or an already trusted MCP connection.

Risk: The API key is a stored credential used for data requests.

Mitigation: Store it through the client's secret mechanism and keep local credential files out of version control.

Risk: Unbounded pagination can increase API usage.

Mitigation: Set page or item limits when fetching comments and replies.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-comments)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Structured comment data with concise theme and sentiment analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Comment and reply results may be paginated; summaries should distinguish single-page from multi-page results.]

## Skill Version(s):

0.1.22 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

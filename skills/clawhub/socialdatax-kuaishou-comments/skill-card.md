## Description:

用于快手评论分析、快手评论回复、快手评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Kuaishou / Kwai comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营者、创作者与分析人员可用此技能读取快手/Kwai 视频评论及回复，并整理受众反馈、情绪主题、异议、痛点、常见问题和讨论摘要。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downloaded CLI implementation is outside the supplied security review, so package trust remains a consideration.

Mitigation: Review and pin a package version before use.

Risk: Fetching many pages or an entire thread can increase API credit usage.

Mitigation: Set page or item limits and use a dedicated SocialDataX API key.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [JSON comment and reply data with concise thematic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports paginated results; an empty comment set may be a valid result.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

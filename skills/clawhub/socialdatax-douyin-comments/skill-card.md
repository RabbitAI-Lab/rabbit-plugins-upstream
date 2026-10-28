## Description:

用于抖音评论分析、抖音评论回复、抖音评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Douyin comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

帮助运营、创作者和分析人员获取指定抖音内容的评论与回复，并总结观众反馈主题、常见问题、异议和痛点。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency trust for the external SocialDataX CLI and service.

Mitigation: Trust SocialDataX only with the requested content identifiers and disclosed usage attribution; prefer a reviewed, pinned CLI version.

Risk: Broad or unbounded comment retrieval can use more API credits than intended.

Mitigation: Set page or item limits to match the requested analysis and use unbounded retrieval only when intended.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-comments)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured comment and reply data with concise Markdown or text insights]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only retrieval; results may span multiple pages, with pagination and item limits controlled by the user.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

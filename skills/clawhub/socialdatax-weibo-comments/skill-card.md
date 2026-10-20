## Description:

用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts and community teams use this skill to review Weibo post comments and replies, summarize audience feedback and sentiment themes, identify objections and pain points, and extract FAQs or discussion summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of the SocialDataX API key

Mitigation: Keep SOCIALDATAX_API_KEY private and avoid sharing it in prompts, logs, or generated reports.

Risk: Unintended API usage or charges

Mitigation: Analyze only intended Weibo threads and set page or item limits to control usage.

Risk: The external package's runtime behavior was not audited in the supplied security assessment

Mitigation: Prefer a reviewed package version and review the dependency before installation.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-comments)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured JSON results with concise natural-language analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only retrieval; result coverage depends on selected page and item limits and available API data.]

## Skill Version(s):

0.1.20 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

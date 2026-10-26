## Description:

用于小红书评论分析、小红书评论回复、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Xiaohongshu / XHS / RedNote comments，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use the skill to retrieve Xiaohongshu comments and reply threads, then summarize audience feedback, recurring themes, sentiment, pain points, FAQs, and discussion topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an npm client package and requires a SocialDataX API key.

Mitigation: Review and pin the client version before use, and provide the API key only after trusting the package.

Risk: Unbounded comment pagination can consume API credits.

Mitigation: Set page or item limits and monitor API-credit use; avoid unbounded retrieval unless it is intended.

## Reference(s):

- [SocialDataX API access and documentation](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-comments)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance, Shell commands]

**Output Format:** [Structured JSON comment data with concise text or Markdown analysis and optional CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include paginated comments, reply threads, and pagination metadata; comment analysis should distinguish observed themes from inferred sentiment or demand.]

## Skill Version(s):

0.1.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

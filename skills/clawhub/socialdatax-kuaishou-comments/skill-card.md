## Description:

用于快手评论分析、快手评论回复、快手评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Kuaishou / Kwai comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Kuaishou first-level comments or replies, then group observed themes and summarize audience feedback, objections, pain points, FAQs, and discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Data requests use the SocialDataX API key and may expose private information if unrelated share text is included.

Mitigation: Keep SOCIALDATAX_API_KEY in the runtime environment, and provide only the public content ID or necessary URL after removing unrelated private information from share text.

Risk: Retrieving many comment pages can consume account credits.

Mitigation: Set --pages or --max-items to an appropriate limit; use --all only when the full result set is needed.

Risk: Using an unpinned CLI release can change runtime behavior as the package updates.

Mitigation: Consider pinning a reviewed CLI version instead of using @latest.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis, Markdown]

**Output Format:** [JSON comment data and a concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Theme-grouped insights with the number of pages reported.]

## Skill Version(s):

0.1.21 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

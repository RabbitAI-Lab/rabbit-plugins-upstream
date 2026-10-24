## Description:

用于快手数据助手、快手内容研究、作品研究、作品详情、评论分析、评论回复分析、达人数据和达人作品。覆盖 Kuaishou / Kwai short-video research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Kuaishou content and creators, inspect video details, analyze comments and replies, and retrieve creator profiles and posts through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and supplied links or share text are processed by SocialDataX; broad requests may incur API charges.

Mitigation: Exclude unrelated private information, protect the API key, review and pin the CLI version where possible, and consider costs before requesting all results.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured Kuaishou data with concise Markdown summaries and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; returned data may be partial when an API request fails.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

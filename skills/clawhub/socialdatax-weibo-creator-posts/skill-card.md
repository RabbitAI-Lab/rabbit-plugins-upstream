## Description:

用于微博创作者数据、微博创作者内容列表、近期发布、内容调研和创作者内容分析。覆盖 Weibo creator posts，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can retrieve Weibo creator posts for recent publishing reviews, content research, style analysis, creator benchmarking, and account tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an unpinned npm package that may change, including during login when an API key is entered.

Mitigation: Review and trust the package source before running its commands, especially before entering credentials.

Risk: Security scan coverage is partial, so its suspicious verdict does not establish malicious intent and the available scan evidence is incomplete.

Mitigation: Use the scan as a prompt for review and assess whether the package source is trusted before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON creator-post data with natural-language summaries when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only creator content; available fields depend on the returned records.]

## Skill Version(s):

0.1.23 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

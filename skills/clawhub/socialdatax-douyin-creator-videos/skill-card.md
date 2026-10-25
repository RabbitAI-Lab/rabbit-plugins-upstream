## Description:

用于抖音达人数据、抖音达人作品、作品列表、图文列表、短剧/合集列表、近期发布、内容调研和创作者内容分析。覆盖 Douyin creator works and series，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Douyin creator videos, image/text posts, and short-drama series for recent publishing reviews, content analysis, creator benchmarking, and account tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API usage may incur charges, and submitted creator queries are handled by SocialDataX.

Mitigation: Use a dedicated API key and review the service's charges and handling of submitted queries.

Risk: Installing a moving package version or collecting all available pages can increase runtime and API usage uncertainty.

Mitigation: Prefer a reviewed, fixed package version and set page or item limits when collecting results.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-videos)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [JSON creator content or series data, with summaries when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available fields depend on the selected endpoint; collection can be bounded by page or item limits.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

用于查询抖音创作者的作品与短剧/合集列表，支持近期发布跟踪、内容调研和创作者内容分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

创作者研究人员、营销团队和内容分析人员可用此技能查询抖音创作者发布的视频、图文作品及短剧合集，用于近期内容回顾、创作者比较和内容风格分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator lookups use an external service and may consume account credits; API access also depends on protecting the SocialDataX API key.

Mitigation: Protect the API key, use a reviewed and pinned CLI version, and set --pages or --max-items to bound larger requests.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-videos)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Text]

**Output Format:** [Structured JSON data with concise text summaries]

**Output Parameters:** [Variable-length creator work or series results]

**Other Properties Related to Output:** [Read-only lookup results may span multiple pages; users can limit requests by page count or item count.]

## Skill Version(s):

0.1.21 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

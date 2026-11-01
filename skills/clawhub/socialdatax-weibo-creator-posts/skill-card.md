## Description:

用于微博创作者数据、微博创作者内容列表、近期发布、内容调研和创作者内容分析。覆盖 Weibo creator posts，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and creators use this skill to retrieve Weibo creator posts for recent publishing reviews, content research, benchmarking, and style analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected creator identifiers and query parameters are sent to SocialDataX with the user's API key.

Mitigation: Review the request parameters and use the SocialDataX service only for creator data you intend to retrieve.

Risk: An installed CLI package runs with the local process permissions available to the agent.

Mitigation: Prefer a reviewed, pinned CLI version and set page or item limits to control usage and charges.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Text]

**Output Format:** [JSON creator-post data with concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Post text, media links, publication times, interaction counts, and author details are included when available.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

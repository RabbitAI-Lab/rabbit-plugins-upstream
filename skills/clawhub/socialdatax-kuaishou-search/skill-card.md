## Description:

用于快手数据分析、快手作品研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Kuaishou / Kwai work research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers can search Kuaishou works by keyword to explore content, monitor competitors, and study trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX, and searches may use account credits.

Mitigation: Avoid confidential queries and set page or item limits to control credit use.

Risk: The skill depends on a third-party CLI or MCP tool and an API key.

Mitigation: Use a reviewed, pinned CLI version where possible, and protect SOCIALDATAX_API_KEY.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON search results with concise text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include content IDs, share URLs, author details, interaction counts, and pagination metadata.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

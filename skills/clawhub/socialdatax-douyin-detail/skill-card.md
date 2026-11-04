## Description:

用于抖音数据分析、抖音作品详情、图文详情、作品数据、互动指标、内容调研和内容分析。覆盖 Douyin work details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, analysts, and developers use this skill to retrieve structured details about Douyin videos and image/text posts for content research and analysis, including available descriptions, authors, publish times, and interaction metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the CLI package uses the agent's permissions.

Mitigation: Prefer a reviewed, pinned package version or a trusted existing MCP connection.

Risk: Data requests may incur API charges, and optional media downloads write to a local destination.

Mitigation: Keep the API key local and out of version control, and choose download destinations explicitly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-detail)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON data with a concise factual summary in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available fields vary by response; image/text posts may include images and music rather than video.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

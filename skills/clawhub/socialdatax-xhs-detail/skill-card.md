## Description:

用于小红书数据分析、小红书笔记详情、笔记数据、互动指标、内容调研和内容分析。覆盖 Xiaohongshu / XHS / RedNote note details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve structured details and engagement metrics for a Xiaohongshu/XHS/RedNote post and summarize its content and media. It can optionally save returned media to a user-selected local path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI package may change or carry ordinary package risks.

Mitigation: Prefer a reviewed, pinned CLI version or already configured MCP tools.

Risk: API credentials and service credits may be exposed or consumed during data calls.

Mitigation: Protect the API key and monitor service credit usage.

Risk: Returned note links preserve query tokens, and media downloads create local files.

Mitigation: Share note links deliberately and choose the media download folder explicitly.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-detail)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Text]

**Output Format:** [Structured JSON note details with concise factual summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post metadata, engagement counts, image and video references, and media summaries when available; optional media downloads save files to a user-selected local path.]

## Skill Version(s):

0.1.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

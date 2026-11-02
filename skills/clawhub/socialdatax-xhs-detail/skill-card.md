## Description:

用于小红书数据分析、小红书笔记详情、笔记数据、互动指标、内容调研和内容分析。覆盖 Xiaohongshu / XHS / RedNote note details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can retrieve details and engagement metrics for Xiaohongshu, XHS, or RedNote posts by note ID or URL. They can use the returned structured data for content research and analysis, and optionally save media to a chosen local folder.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests may incur SocialDataX credit charges.

Mitigation: Use a dedicated SocialDataX API key and monitor API-credit usage.

Risk: The CLI version referenced with @latest can change independently of this skill release.

Mitigation: Review and pin a fixed CLI version before routine use.

Risk: Full note links can retain query parameters when shared.

Mitigation: Share returned full note links only with intended recipients.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-detail)

## Skill Output:

**Output Type(s):** [JSON, Text, Files]

**Output Format:** [Structured JSON note details with concise text summaries; optional downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a complete note ID or a note URL/share text; optional media downloads use a user-selected output path.]

## Skill Version(s):

0.1.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

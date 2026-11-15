## Description:

当用户需要做社媒内容日历研究、7 天或 30 天选题规划、发布时间观察、内容主题分组、平台节奏对比或运营素材整理时使用。覆盖小红书、抖音和快手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

社交媒体运营人员可用此 skill 研究小红书、抖音和快手的热点与搜索样本，并据此整理 7 天或 30 天内容日历、主题分组和发布时间观察。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a mutable SocialDataX package that could access credentials.

Mitigation: Review the package before installation; enter API keys only through the documented hidden local login flow and keep them out of chat, logs, and skill files.

Risk: Search terms may be sent to SocialDataX without a privacy disclosure.

Mitigation: Tell users when a query will be sent to SocialDataX and avoid sending sensitive terms unless sharing them is appropriate.

Risk: The security scan had partial coverage because it could not resolve several local references.

Mitigation: Review the package and referenced files before installation, and treat the scan's suspicious verdict as unresolved.

## Reference(s):

- [SocialDataX skill and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-content-calendar-research)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Markdown summary based on structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trend rankings, popularity signals, sample titles, authors, links or content IDs, and publication times when available.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

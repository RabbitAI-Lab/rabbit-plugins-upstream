## Description:

当用户需要做社媒内容日历研究、7 天或 30 天选题规划、发布时间观察、内容主题分组、平台节奏对比或运营素材整理时使用。覆盖小红书、抖音和快手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

社媒运营人员和内容策划者可用此技能研究小红书、抖音和快手的热榜与关键词样本，观察发布时间和主题趋势，并为 7 天或 30 天内容计划整理选题与平台节奏。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords are sent to SocialDataX and may reveal information the user did not intend to share.

Mitigation: Avoid confidential details in search terms unless the user intends to share them with the service.

Risk: The external CLI implementation was unavailable for inspection, and installing or updating a package carries supply-chain risk.

Mitigation: Keep the API key in a supported secret store and consider pinning a reviewed CLI version.

Risk: API calls may consume service credits.

Mitigation: Start with a small sample and expand the search only as needed.

## Reference(s):

- [SocialDataX AI skill and API key page](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-content-calendar-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown summaries of rankings, trend signals, content samples, and follow-up angles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can preserve source titles, authors or accounts, links or content IDs, visible engagement signals, and publication times when available.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

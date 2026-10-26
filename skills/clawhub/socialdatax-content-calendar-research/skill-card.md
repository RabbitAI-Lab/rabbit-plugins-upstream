## Description:

当用户需要做社媒内容日历研究、7 天或 30 天选题规划、发布时间观察、内容主题分组、平台节奏对比或运营素材整理时使用。覆盖小红书、抖音和快手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media researchers and content operators can use this skill to review trends and search results across Xiaohongshu, Douyin, and Kuaishou, organize topics, compare platform rhythms, and plan 7-day or 30-day content calendars.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and filters are sent to SocialDataX and may contain sensitive context.

Mitigation: Avoid sending confidential information; use general or sanitized search terms.

Risk: Larger or repeated searches can consume API credits.

Mitigation: Start with a small sample and set page or result limits before expanding a search.

Risk: The downloaded CLI and its dependencies may change, and the CLI runs with the local process's permissions.

Mitigation: Prefer a reviewed, fixed package version over @latest and provide only the required API key.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-content-calendar-research)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown summaries with ranked trends, content examples, links, and planning angles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result volume can be limited or paginated.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

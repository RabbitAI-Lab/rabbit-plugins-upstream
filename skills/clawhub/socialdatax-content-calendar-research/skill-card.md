## Description:

当用户需要做社媒内容日历研究、7 天或 30 天选题规划、发布时间观察、内容主题分组、平台节奏对比或运营素材整理时使用。覆盖小红书、抖音和快手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External social media researchers and content operators can use this skill to review hot lists and keyword search results from Xiaohongshu, Douyin, and Kuaishou, then organize topics and posting observations into a content calendar.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX, and calls may consume paid credits.

Mitigation: Avoid confidential search terms and review expected credit use before running searches.

Risk: The skill requires a SocialDataX API key, and returned Xiaohongshu URLs may contain token parameters.

Mitigation: Protect the API key and review full result URLs before sharing them.

Risk: The documented CLI uses an unpinned package version; read-only skill instructions do not sandbox downloaded package code.

Mitigation: Prefer a reviewed fixed package version and limit the local access available to the runtime.

## Reference(s):

- [SocialDataX Agent Skill and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-content-calendar-research)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Markdown summaries of social search results, with JSON-backed rankings, titles, authors, links or content IDs, and follow-up angles.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include current hot-list signals and paginated keyword search samples for supported platforms.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

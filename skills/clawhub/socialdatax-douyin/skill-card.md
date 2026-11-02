## Description:

用于抖音数据助手、抖音热榜、抖音数据分析、作品搜索、作品详情、作品分享链接、评论分析、评论回复分析、达人数据、达人作品和达人短剧/合集。覆盖 Douyin hot search and work research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to research Douyin trends, posts, comments, creators, and creator series through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, identifiers, and supplied share text are sent to SocialDataX.

Mitigation: Avoid including sensitive information in queries or supplied text.

Risk: Large page or item requests can use more account credits.

Mitigation: Set page and item limits to match the research task.

Risk: Using the floating @latest package tag can change the CLI version between runs.

Mitigation: Prefer a reviewed, fixed CLI version for repeatable use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, JSON, Text]

**Output Format:** [Structured JSON data and human-readable research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested Douyin data and any pagination or item limits.]

## Skill Version(s):

0.1.22 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

检索抖音公开视频、图文、热榜、博主作品与评论数据，并以结构化 JSON 返回，支持内容与用户反馈分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

面向内容运营者、分析师与开发者，用于搜索抖音公开内容、追踪热榜和博主作品，并汇总评论反馈以支持选题、竞品和舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and links are sent to the disclosed third-party service, and saved results or logs may contain inputs and public user data.

Mitigation: Use the service only if its terms and pricing are acceptable, keep GUAIKEI_API_TOKEN private, choose suitable retrieval limits, and protect or delete saved logs.

## Reference(s):

- [GuaiKei Service Website](https://www.guaikei.com)
- [Usage Options](references/options.md)
- [Changelog](references/changelog.md)
- [ClawHub Release Page](https://clawhub.ai/why20261/skills/douyin-comments-guaikei)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON containing query metadata and Douyin search, creator, trending, or comment results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are saved locally as documented; empty-result responses use a structured status and error code.]

## Skill Version(s):

1.4.0 (source: SKILL.md frontmatter, package.json, changelog, released 2026-10-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

查询快手公开的视频、博主作品和评论数据，支持竞品监测、选题调研与内容分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

快手内容创作者、品牌营销人员和分析师可查询公开的视频、账号作品及评论，用于竞品对比、内容选题和舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, profile and video links, and query parameters are sent to a third-party API.

Mitigation: Use only targets and queries you are comfortable sharing with guaikei.com, and confirm data-sharing authorization before use.

Risk: The API token and locally saved results may reveal sensitive research targets or comments.

Mitigation: Protect GUAIKEI_API_TOKEN, restrict access to logs/, and remove saved results when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-insight)
- [使用参数说明](references/options.md)
- [版本更新记录](references/changelog.md)
- [API 令牌与使用帮助](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured JSON with optional plain-language summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes success, empty or error status; results are saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

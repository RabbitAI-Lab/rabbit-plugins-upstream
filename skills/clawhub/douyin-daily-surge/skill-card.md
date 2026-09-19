## Description:

抖音每日点赞飙升榜查询工具，可获取公开抖音作品的单日点赞榜、关键词搜索结果、实时热榜、博主公开作品和视频评论数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, and developers use this skill to collect structured public Douyin data for trend discovery, competitor monitoring, content research, comment analysis, and marketing reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved result logs may retain Douyin results, search terms, creator IDs, comments, nicknames, and IP-region labels.

Mitigation: Run the skill only in workspaces approved for this data, restrict access to generated logs, and clean logs when they are no longer needed.

Risk: GUAIKEI_API_TOKEN is a third-party API credential required for live data access.

Mitigation: Store the token as a protected environment variable or secret, avoid exposing terminal configuration, and rotate the token if it is disclosed.

## Reference(s):

- [Server-resolved GitHub source repository](https://github.com/why20261/douyin-daily-surge)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-daily-surge)
- [抖音达人数据获取官网](https://www.guaikei.com)
- [Complete command options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [Structured JSON responses from Node.js CLI commands, with optional saved JSON log files and concise Markdown guidance from the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN. CLI commands write JSON to stdout and status logs to stderr; search, post, and comment commands may save result files under logs/.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact runtime reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

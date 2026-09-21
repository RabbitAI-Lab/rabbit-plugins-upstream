## Description:

查询快手公开视频、达人作品和评论数据，用于关键词搜索、博主作品抓取、评论分析以及市场调研和内容运营判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External content creators, marketers, market researchers, and data analysts use this skill to collect public Kuaishou video, creator, and comment data for trend research, competitor monitoring, topic selection, and campaign planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile or video URLs, requested limits, and the GUAIKEI API token are sent to the guaikei.com service.

Mitigation: Install and run the skill only when that data sharing is acceptable, and scope the token according to the user's authorization and retention requirements.

Risk: Saved logs can retain public comments, creator metadata, and research outputs.

Mitigation: Protect or delete generated logs according to privacy, platform-compliance, and internal data-retention policies.

## Reference(s):

- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [GuaiKei API Service](https://www.guaikei.com)
- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/kuaishou-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI scripts return structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save JSON research logs under logs/.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, package.json, release evidence, changelog released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

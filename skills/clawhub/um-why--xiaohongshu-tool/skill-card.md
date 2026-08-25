## Description:

小红书公开数据检索工具，用于按关键词搜索笔记、读取笔记详情和评论、查看博主公开作品与互动数据，支持爆款选题、竞品监控、KOL 筛选和评论舆情分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

Content creators, brand marketers, market analysts, and agent operators use this skill to retrieve structured Xiaohongshu public data for topic research, competitor monitoring, KOL screening, comment analysis, and trend tracking. It requires a GUAIKEI_API_TOKEN and sends Xiaohongshu keywords or URLs to the guaikei.com API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, profile URLs, and API tokens are sent to guaikei.com to retrieve data.

Mitigation: Install and run only when third-party API use is acceptable for the research target, and scope queries to public data that may be shared with that service.

Risk: Returned public notes, profiles, and comments may be retained locally in result logs.

Mitigation: Clear the temp log directory after runs that involve sensitive research targets or personal data from public comments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/um-why/skills/xiaohongshu-tool)
- [Publisher Profile](https://clawhub.ai/user/um-why)
- [Project Homepage](https://github.com/um-why/xiaohongshu-openclaw-skill)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Node.js shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results may be archived locally under the temp log directory; output can include public note, profile, and comment data returned by the third-party API.]

## Skill Version(s):

1.1.2 (source: frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

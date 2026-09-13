## Description:

小红书公开数据检索工具，用于按关键词或链接获取公开笔记、笔记详情、评论、博主作品和互动数据，支持选题调研、竞品监控、KOL筛选和评论舆情分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

External operators, marketers, content teams, and agent users use this skill to collect structured public Xiaohongshu data for topic research, competitor monitoring, creator screening, trend tracking, and comment analysis. The skill requires a GUAIKEI_API_TOKEN and sends query keywords or Xiaohongshu links to guaikei.com to return JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or links and the configured GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only with research targets and tokens that are appropriate to share with that API service, and avoid submitting sensitive or confidential query terms.

Risk: Successful runs save full results and URLs to a local temporary log directory.

Mitigation: Run on trusted machines, avoid shared workstations for sensitive research, and delete temporary logs after analysis is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/xiaohongshu-tool)
- [Publisher profile](https://clawhub.ai/user/um-why)
- [Project homepage](https://github.com/um-why/xiaohongshu-openclaw-skill)
- [Guaikei API token service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Troubleshooting reference](references/troubleshooting.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-producing command-line workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command outputs include structured JSON from the Xiaohongshu data API and are also saved to local temporary logs by the skill.]

## Skill Version(s):

1.1.4 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

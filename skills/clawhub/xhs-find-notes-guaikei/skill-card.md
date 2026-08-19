## Description:

搜索小红书公开笔记、查看笔记详情与评论、获取笔记评论数据、抓取博主公开作品列表，并返回结构化数据用于爆款挖掘、竞品分析、KOL筛选与趋势洞察。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, analysts, and agent operators use this skill to retrieve public Xiaohongshu notes, note details, comments, and creator post lists for content research, competitor monitoring, KOL screening, and trend analysis. It does not support login, publishing, liking, commenting, following, or private content access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Xiaohongshu URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com to retrieve public Xiaohongshu data.

Mitigation: Use the skill only when this data transfer is authorized, scope tokens appropriately, and avoid submitting confidential research terms or URLs unless the user accepts the transfer.

Risk: Retrieved public comments, URLs, and business research results are written to a local logs directory.

Mitigation: Review, protect, or delete generated log files when the results should not remain on disk.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/xhs-find-notes-guaikei)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; command execution returns structured JSON and writes JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword, URL, filter, sorting, time range, and limit parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter, package.json, constants, and changelog report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

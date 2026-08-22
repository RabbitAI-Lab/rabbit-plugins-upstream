## Description:

获取小红书公开内容数据的工具：按关键词搜索笔记、查看单篇笔记详情、拉取笔记评论、抓取博主公开作品，返回结构化 JSON 用于爆款挖掘、竞品分析、KOL 筛选与评论舆情。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content creators, brand marketers, market analysts, and operations teams use this skill to retrieve public Xiaohongshu content, note details, comments, and creator posts for content research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, links, and public-content targets to the Guaikei API provider.

Mitigation: Use only authorized public-content targets and avoid confidential campaign terms or sensitive URLs unless sharing them with the provider is approved.

Risk: Task results may persist in local logs and become available through workspace files or backups.

Mitigation: Review or delete generated log files when retrieved results should not remain in the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-trending-keywords)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands that return structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes task results to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

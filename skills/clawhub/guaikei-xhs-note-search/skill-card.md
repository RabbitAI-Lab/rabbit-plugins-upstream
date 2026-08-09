## Description:

小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and analysts use this skill to retrieve public Xiaohongshu notes, note details, comments, and creator posts for content research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note/profile URLs, requested limits, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use only with approved queries and an authorized API token; confirm that third-party API use is acceptable for the data and organization before running commands.

Risk: Saved logs may retain sensitive business research or public personal-content data.

Mitigation: Restrict access to local logs and delete the logs directory when retained results are no longer needed.

Risk: The skill is limited to public Xiaohongshu data and does not support private, hidden, login-required, or account-mutating actions.

Mitigation: Decline requests for private or authenticated data and use the skill only for public lookup and analysis workflows.

## Reference(s):

- [Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-note-search)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON result expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release evidence, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

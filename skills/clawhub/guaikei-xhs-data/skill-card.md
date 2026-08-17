## Description:

搜索小红书公开笔记、查看笔记详情、获取笔记评论、抓取博主公开作品，返回结构化数据用于爆款挖掘、竞品分析、KOL筛选与评论洞察。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketing teams, analysts, and business operators use this skill to collect structured public Xiaohongshu data for content research, competitor monitoring, KOL screening, trend analysis, and comment insight workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, links, embedded URL parameters, and public content identifiers are sent to the third-party guaikei.com API.

Mitigation: Use the skill only when sharing those inputs with guaikei.com is acceptable, and avoid submitting URLs whose query parameters should not be shared.

Risk: GUAIKEI_API_TOKEN is required and functions as a sensitive API credential.

Mitigation: Store the token in the environment, do not paste it into prompts or logs, and rotate it if exposure is suspected.

Risk: Fetched result data may be saved in the skill's local logs directory.

Mitigation: Periodically clear saved logs when retained Xiaohongshu result data should not remain on disk.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-data)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON results from command-line tools, with shell command guidance and optional downstream markdown summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands can save result logs locally.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

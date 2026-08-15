## Description:

小红书运营数据工具｜当用户需要搜索小红书公开笔记、查看某篇笔记详情与评论、获取单篇笔记评论、或抓取某个博主的公开作品列表时使用，可实现爆款挖掘/竞品分析/KOL筛选/趋势洞察，用数据驱动小红书流量增长，告别盲目创作

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brand marketers, and analysts use this skill to search Xiaohongshu public notes, retrieve note details and comments, and monitor creator posts for topic research, competitor analysis, KOL screening, and trend insight.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu URLs, and related request details are sent to the third-party GuAikei API service.

Mitigation: Use the skill only when that data sharing is acceptable, avoid private or sensitive URLs, and confirm that the data source is authorized for the intended use.

Risk: Successful results can be saved locally, including retained search results, profile URLs, comments, or request metadata.

Mitigation: Review and periodically delete the skill's logs directory when retained Xiaohongshu data or request metadata should not remain on disk.

Risk: The skill requires a GUAIKEI_API_TOKEN to access the data service.

Mitigation: Keep the token in environment configuration, avoid sharing it in prompts or committed files, and rotate it if exposure is suspected.

## Reference(s):

- [Parameter and invocation guide](references/options.md)
- [Skill changelog](references/changelog.md)
- [GuAikei API service](https://www.guaikei.com)
- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-word-cloud)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with shell command examples; command output is structured JSON and successful runs may save local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword or URL inputs plus type, sort, time, and limit options depending on the command.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

按关键词搜索小红书公开笔记，支持按点赞、评论、收藏排序与时间筛选，并获取笔记详情、评论和博主公开作品数据供后续分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, analysts, and agent operators use this skill to collect public Xiaohongshu note, comment, and profile-post data for content research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu note URLs, profile URLs, requested limits, and the GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Use only with approved public-data collection tasks, confirm organizational approval for data sharing, and manage GUAIKEI_API_TOKEN through secrets handling rather than prompts or logs.

Risk: Successful results are saved locally under logs and may contain collected public content, comments, author metadata, or marketing research outputs.

Mitigation: Review log retention and access controls, avoid collecting sensitive or unnecessary data, and delete outputs when they are no longer needed.

Risk: The skill is limited to public Xiaohongshu data and is not intended for private, login-required, publishing, liking, commenting, following, or unclear monitoring tasks.

Mitigation: Validate the requested task and URL type before execution, refuse private or account-action requests, and ask for clarification when the user's target is ambiguous.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-note-insights)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; invoked CLI commands return structured JSON and save local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful task results are saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

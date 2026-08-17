## Description:

获取小红书博主公开作品及单篇笔记的点赞、评论和收藏数据，帮助评估内容互动质量、筛选 KOL 和支持小红书营销调研。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, brand marketing teams, data analysts, and MCN operators use this skill to collect public Xiaohongshu note, comment, search, and creator-post data for topic research, competitor monitoring, KOL screening, and engagement analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, URLs, and URL query parameters are sent to guaikei.com with the configured GUAIKEI_API_TOKEN.

Mitigation: Use only approved public-data queries, avoid sensitive competitor or campaign URLs unless authorized, and confirm organizational approval for the external API service.

Risk: Collected public comments, research keywords, and competitor URLs may be written to local logs.

Mitigation: Review, retain, or delete generated log files according to the organization's data-handling policy.

Risk: The skill does not support private, hidden, login-gated, publishing, liking, following, or commenting workflows.

Mitigation: Limit use to public Xiaohongshu data collection and do not use the skill for account interaction or restricted data access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-creator-notes-collector)
- [Guaikei API service](https://www.guaikei.com)
- [Parameter and invocation guide](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; executed commands return structured JSON and may save local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword, note URL, creator profile URL, limit, sort, type, and time options.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

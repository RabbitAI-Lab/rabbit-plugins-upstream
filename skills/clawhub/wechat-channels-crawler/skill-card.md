## Description:

视频号作品查询工具。根据用户输入的关键词搜索视频号热门作品，支持按最新、最多点赞、最多收藏和综合排序，结果以结构化表格展示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, MCN and brand operators, marketing teams, and individual users use this skill to search WeChat Channels works by keyword, compare engagement metrics, and optionally subscribe to daily keyword updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords are sent to RedFox using REDFOX_API_KEY.

Mitigation: Install and use the skill only when sending those keywords to RedFox is acceptable, and keep the API key out of prompts, logs, and committed files.

Risk: Daily subscriptions create persistent scheduled keyword queries.

Mitigation: Create subscriptions only after explicit user confirmation and remove unneeded jobs with qoder_cron.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-channels-crawler)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFoxHub](https://redfox.hk?source=clawhub)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown tables for agent responses and JSON for raw search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include work title, author, engagement counts, publish time, topics, duration, and video URL when returned by the RedFox API.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

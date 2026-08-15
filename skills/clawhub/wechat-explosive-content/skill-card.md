## Description:

公众号搜索工具，支持按关键词搜索爆款文章，展示推荐热门文章，助力内容创作者把握趋势与获取灵感；当用户需要搜索公众号文章、查找爆款内容、获取创作灵感时使用.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, WeChat operators, brand teams, and self-media learners use this skill to search recent high-read WeChat Official Account articles, compare topics, and identify content trends. Agents can call the bundled script with keywords and dates, then present JSON results as Markdown tables or optional local HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends WeChat article search terms and date ranges to the external RedFox API using REDFOX_API_KEY.

Mitigation: Use the skill only when the user is comfortable sharing those query terms with RedFox, and keep the API key in environment configuration rather than prompts, logs, source files, or generated reports.

Risk: The subscription workflow can create recurring calendar reminders for keyword searches.

Mitigation: Confirm the user's desired subscription, schedule, and cancellation or management path before creating recurring reminders.

Risk: Optional HTML output creates local report files from external article data.

Mitigation: Generate HTML reports only when the user wants local files and is comfortable storing externally sourced article metadata on the device.

## Reference(s):

- [Skill source on ClawHub](https://clawhub.ai/redfox-data/skills/wechat-explosive-content)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFox WeChat hot article API endpoint](https://redfox.hk/story/api/gzh/search/hotArticle)
- [WeChat trend data format reference](references/gzh_trend_data_format.md)
- [English README](README.en.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [JSON from stdout, Markdown tables in the agent response, and optional local HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY and sends keyword/date queries to RedFox; default query scope is recent WeChat articles with 5,000+ reads from the past 30 days.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

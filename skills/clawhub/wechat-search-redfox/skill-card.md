## Description:

Searches WeChat Official Account hot articles through Redfox, ranks results by relevance, popularity, and recency, and helps content creators find topic ideas and trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, WeChat account operators, brand teams, and self-media learners use this skill to search recent 5,000+ read WeChat articles, compare hot topics, and plan content. Agents use it to run a Redfox-backed query, interpret structured results, and present concise Markdown tables and subscription prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends WeChat search keywords and date ranges to Redfox using REDFOX_API_KEY.

Mitigation: Use it only when that data sharing is acceptable, obtain the key from Redfox, keep it in environment configuration, and avoid exposing it in code, prompts, logs, or output files.

Risk: The subscription flow can create recurring calendar reminders for future pushes.

Mitigation: Confirm the desired schedule before creating a subscription and understand how to cancel recurring reminders before relying on them.

Risk: Article metrics are not real-time and are limited to the indexed recent 30-day, 5,000+ read data scope described by the artifact.

Mitigation: Tell users the update cadence and data scope when presenting results, and avoid describing the returned metrics as live engagement data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/wechat-search-redfox)
- [Publisher profile](https://clawhub.ai/user/yuanyi-github)
- [Data format reference](references/gzh_trend_data_format.md)
- [Redfox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [Redfox hot article API endpoint](https://redfox.hk/story/api/gzh/search/hotArticle)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, files]

**Output Format:** [Markdown tables and prompts for users, JSON from the query script, and optional HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; can query single or comma-separated keywords and date ranges up to the recent 30-day data window described by the artifact.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

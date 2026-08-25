## Description:

每日新闻获取技能，通过 API 获取每日新闻摘要和详情，支持按日期查询、热点新闻排行和新闻详情阅读。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Chinese daily news summaries, ranked hot news, category-filtered news, and article details through an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines a news-fetching purpose with unrelated database, file-writing, and command-execution claims.

Mitigation: Review before installation and use it only for the documented news retrieval workflow unless the publisher narrows and documents the extra scope.

Risk: The skill relies on shell-based API calls.

Mitigation: Run in an agent environment where shell execution is reviewed or sandboxed, and inspect API commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-news)
- [Daily news API endpoint](https://api.cjiot.cc/api/v1/daily?date={当前日期})

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON-style responses with API-derived news summaries and details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include article titles, categories, heat rankings, publication times, summaries, detail text, and troubleshooting guidance.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

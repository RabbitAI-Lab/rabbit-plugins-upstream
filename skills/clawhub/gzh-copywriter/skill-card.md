## Description:

公众号文案创作工具，基于红狐数据公众号爆款雷达按关键词检索热门文章、分析流量规律，并生成可发布的公众号文章。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, content operators, MCN teams, and brand planners use this skill to research recent WeChat Official Account viral article patterns and draft publish-ready WeChat copy with titles, tags, a core viewpoint, and source pattern analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword queries and API credentials are sent to redfox.hk when the bundled data-fetching script runs.

Mitigation: Use a revocable RedFox API key with the least necessary scope, avoid confidential keywords, and rotate or revoke the key after testing.

Risk: The skill asks users for personal writing samples without clear privacy, retention, or deletion guidance.

Mitigation: Do not provide diaries, private notes, customer data, proprietary drafts, or other sensitive samples unless handling and deletion expectations are explicit.

Risk: The bundled script appends an undisclosed promotional contact line to its output.

Mitigation: Review generated output before sharing or publishing and remove unexpected promotional or contact content.

## Reference(s):

- [公众号趋势数据格式说明](references/gzh_trend_data_format.md)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=github)
- [RedFox WeChat viral article search endpoint](https://redfox.hk/story/api/gzh/search/hotArticleNew)
- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/gzh-copywriter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown article draft with analysis sections and occasional inline shell commands for data retrieval]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; keyword queries are limited to five keywords and the default data window expands from 7 to 30 days when results are insufficient.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

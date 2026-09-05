## Description:

全网持续收录每日公众号原创热门文章内容，向用户推送公众号原创热门文章；当用户需要获取全领域的公众号原创热门文章、或订阅每日原创热门文章推送时使用

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, WeChat operators, content planners, and operations leads use this skill to fetch original WeChat article rankings by category or date, review article tables, generate HTML reports, and consider category subscription prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a Redfox API key and evidence reports certificate checks disabled during API requests.

Mitigation: Review before installing, only use the skill if Redfox is trusted with the API key and query parameters, and prefer deployment after TLS verification is fixed.

Risk: Generated HTML is active browser content that renders remote article data and loads third-party JavaScript.

Mitigation: Treat generated HTML files as active content, review them before sharing or opening in sensitive environments, and avoid exposing secrets in generated output.

Risk: The skill can prompt for article-category subscription behavior.

Mitigation: Confirm any subscription action explicitly and verify there is a clear way to stop it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/gzh-original-article-king)
- [Category mapping](references/category_mapping.md)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFoxHub](https://redfox.hk?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown article ranking tables with optional generated HTML report files and PDF export support]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY and uses Redfox article data; generated HTML renders remote article content and loads third-party JavaScript.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

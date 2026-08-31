## Description:

全网持续收录每日超过1000+公众号10w+文章内容，向用户推送公众号达到10w+阅读的热门文章；当用户需要获取全领域的公众号热门文章、或订阅每日10w+文章推送、特定领域爆款文章时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External content operators, editors, marketers, and researchers use this skill to find WeChat Official Account articles with 10w+ reads, compare category rankings, analyze viral patterns, and generate shareable HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure or overbroad secret access could occur if an agent follows documentation that suggests reading shell startup files for API keys.

Mitigation: Use a dedicated RedFox API key through the platform or REDFOX_API_KEY environment variable only, and do not allow the skill or agent to inspect shell startup files for secrets.

Risk: Subscription or report-generation actions may create ongoing pushes or local files the user did not intend.

Mitigation: Confirm subscription choices and report generation with the user before running those actions.

Risk: Generated HTML reports may include content and links from external WeChat/RedFox data sources.

Mitigation: Treat generated reports as external-source content, review them before sharing, and avoid exposing secrets in prompts, logs, or output files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/gzh-10w-hot)
- [API interface specification](references/api-spec.md)
- [Category mapping table](references/category-mapping.md)
- [RedFoxHub API keys](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFoxHub](https://redfox.hk?source=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, HTML files, Guidance]

**Output Format:** [Markdown rankings and analysis, shell command invocations, JSON-backed data, and generated HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; uses RedFox article data with scheduled freshness and lookback limits; generated HTML may contain external article content and links.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

全网持续收录每日超过1000+公众号10w+文章内容，向用户推送公众号达到10w+阅读的热门文章；当用户需要获取全领域的公众号热门文章、或订阅每日10w+文章推送、特定领域爆款文章时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External content operators, editors, growth teams, and marketers use this skill to retrieve WeChat 10w+ article rankings, analyze viral patterns, generate shareable reports, and optionally subscribe to niche updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Redfox API key and the security evidence flags credential-handling disclosure concerns.

Mitigation: Provide a scoped key through an environment variable or OpenClaw secret/config, avoid shell profile credential searches, and rotate or revoke the key if exposure is suspected.

Risk: The skill returns uncurated WeChat article links and content from a third-party data source.

Mitigation: Review article links, summaries, and generated analysis before relying on them for publishing, reporting, or business decisions.

Risk: The recurring subscription flow is unclear in the security evidence.

Mitigation: Enable daily subscriptions only when the platform clearly shows how to manage and cancel them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-10w-hot)
- [API接口规范](references/api-spec.md)
- [分类映射表](references/category-mapping.md)
- [RedFoxHub API keys](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown rankings and analysis, shell command guidance, JSON working data, and optional HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; results depend on Redfox API availability, data freshness, and platform support for subscriptions.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

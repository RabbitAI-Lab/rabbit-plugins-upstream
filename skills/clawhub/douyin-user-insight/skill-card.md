## Description:

通过关键词搜索、热榜、公开作品及评论查询，帮助分析抖音用户需求、内容趋势和产品机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、市场研究和产品团队使用抖音公开数据研究热门话题、创作者作品及评论反馈，以支持选题、竞品分析和产品机会评估。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research terms and Douyin links are sent to the GUAIKEI third-party API.

Mitigation: Avoid sensitive queries or links unless external data transfer is authorized.

Risk: The GUAIKEI_API_TOKEN may be exposed if shared or logged.

Mitigation: Keep the token private and provide it through the environment rather than sharing it in prompts or outputs.

Risk: Saved result JSON files can persist in the local logs directory.

Mitigation: Review retention needs and periodically remove logs that should not persist.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-user-insight)
- [GUAIKEI API and access](https://www.guaikei.com)
- [Command options](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON results with optional text analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, creator and comment results may also be saved as local JSON files.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

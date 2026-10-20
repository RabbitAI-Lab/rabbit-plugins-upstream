## Description:

帮助用户检索招标和中标公告，并简要汇总项目名称、金额及链接。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

采购和销售团队可按关键词、企业、地区和时间查找招投标公告，查看项目详情并汇总市场与企业信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broader-than-advertised behavior, including account creation and device fingerprinting.

Mitigation: Review the skill before installing; configure your own ZLBX_API_KEY and approve auto-registration only if you accept device fingerprinting and third-party account creation.

Risk: The skill may store API credentials locally and access account balances or tender contact data.

Mitigation: Protect the API key and local configuration; authorize account and contact-data queries only when needed.

Risk: Data queries can consume quota or lead to recharge flows.

Mitigation: Check quota and expected query costs before expanded searches or recharge, and approve only intended calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/tender-search-biaozhaozhao)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Automatic registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise Markdown lists or tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes stated search filters and available project amounts; missing fields remain blank.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

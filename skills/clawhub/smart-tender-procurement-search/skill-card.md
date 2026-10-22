## Description:

帮助用户按关键词、地区、金额和时间检索招标采购公告，查看项目详情并跟踪潜在商机。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

采购团队、供应商及市场分析人员可检索招标和中标公告、查看项目及企业信息，并分析采购趋势与潜在商机。查询需使用知了标讯 API 凭证。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses an API key from the environment or local configuration.

Mitigation: Use a dedicated key, restrict access to its storage, and do not include it in shared outputs.

Risk: Optional automatic registration transmits a MAC-derived device hash and saves the returned API key locally.

Mitigation: Review the consent prompt and registration terms before approving automatic registration.

Risk: Contact results and account usage data may contain sensitive business information.

Mitigation: Share results only with authorized recipients and avoid exporting contact data in bulk.

Risk: First-use account/version checks and acknowledgement callbacks may contact the provider.

Mitigation: Review these provider interactions before installing or using the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search)
- [Skill installation documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Registry data interpretation](references/api-registry.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with links to source announcements]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on API access and available account credits; contact details may be masked.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

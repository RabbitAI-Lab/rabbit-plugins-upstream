## Description:

帮助采购与投标团队检索招中标公告、调查供应商和企业，并分析采购市场与历史中标价格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

采购、招投标和业务开发人员用它查询项目公告、核验供应商履历、寻找潜在客户与投标伙伴，并查看市场统计。使用知了标讯服务需要 API 密钥。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The third-party tender-data service receives search terms, API credentials, and skill package identity.

Mitigation: Review the provider's data handling before use; configure your own API key and avoid sending sensitive queries unnecessarily.

Risk: Automatic registration sends a hashed device identifier and saves a credential locally.

Mitigation: Prefer manual API-key setup; require explicit consent before registration and review the credential stored in ~/.zlbx/config.json.

Risk: Account/version checks and display acknowledgments contact the provider beyond the requested data search.

Mitigation: Review these network interactions before installation and acknowledge upgrade notices only after showing them to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/enterprise-tender-search-bilianwang)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market API reference](artifact/references/api-market.md)
- [Business registry API reference](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters, result counts, company records, and market statistics depend on the selected API and available account balance.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

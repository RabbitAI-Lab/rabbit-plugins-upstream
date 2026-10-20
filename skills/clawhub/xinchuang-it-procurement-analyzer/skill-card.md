## Description:

分析中国信创及 IT 信息化招投标公告、企业与市场数据，帮助筛选项目、比较供应商和了解采购趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

采购团队、投标供应商和市场分析人员可查询中国 IT 与国产化项目，比较中标价格和供应商，并识别潜在商机。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Procurement queries and account metadata are sent to an external service using an API key.

Mitigation: Review the service's data practices before use and avoid sending sensitive information in queries.

Risk: Auto-registration may send a hashed MAC address and store an API key locally.

Mitigation: Request consent before collecting device data; allow manual registration and protect the stored credential.

Risk: Embedded instructions may initiate account or update-related calls without clear user visibility.

Mitigation: Review these calls before deployment and only confirm an update notice after displaying it to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/xinchuang-it-procurement-analyzer)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include linked procurement notices, filters, dates, amounts, and supplier comparisons.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

帮助用户发现临期续约与拟建招标商机，分析采购客户、潜在供应商和竞争对手的中标动态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

销售、投标及市场分析人员可查询中国招投标公告和临期项目，追踪竞争对手中标记录，发现潜在采购客户与供应商。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement searches and related business parameters are sent to Zhiliaobiaoxun's external API.

Mitigation: Review the data being shared before using the service; avoid including unnecessary sensitive business information.

Risk: Automatic registration collects device features and stores an API key in a local plaintext configuration file.

Mitigation: Prefer configuring your own ZLBX_API_KEY; review and consent to device-feature collection before auto-registration, and protect local credential storage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/tender-opportunity-intelligence-officer)
- [标讯搜索 API 参考](artifact/references/api-search.md)
- [企业分析 API 参考](artifact/references/api-company.md)
- [市场分析 API 参考](artifact/references/api-market.md)
- [自动注册及凭证配置说明](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with linked result summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports applied filters and available source links; requires a Zhiliaobiaoxun API key.]

## Skill Version(s):

1.0.9 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

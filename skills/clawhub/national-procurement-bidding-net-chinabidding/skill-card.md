## Description:

面向中国招投标与采购信息的检索、企业分析和市场趋势研判助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

采购、销售和市场分析人员可检索中国招标、中标与合同公告，分析企业、竞争对手及采购趋势，辅助供应商寻源和商机评估。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Automatic registration sends device platform, CPU architecture and a MAC-address hash to the provider.

Mitigation: Prefer a manually configured API key; obtain explicit consent before automatic registration.

Risk: Automatic registration stores the returned API key in a local configuration file.

Mitigation: Review the local key storage and protect the configuration file from unauthorized access.

Risk: Procurement queries and some account or update checks are sent to the provider's endpoints.

Mitigation: Avoid submitting confidential search terms or personal data unless this disclosure is acceptable.

Risk: Operational instructions embedded in Markdown comments can be easy to miss during review.

Mitigation: Review the entire skill, including comments, before installing or approving requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/national-procurement-bidding-net-chinabidding)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Automatic registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the vendor's available data and the user's API access.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

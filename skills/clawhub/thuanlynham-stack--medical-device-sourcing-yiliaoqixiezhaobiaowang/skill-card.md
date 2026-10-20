## Description:

帮助查询中国医疗器械及耗材招投标信息、品牌与型号的历史中标价格，并汇总采购方和供应商数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

采购团队和医疗器械供应商可检索招标与中标项目、比较品牌型号的历史中标单价，并了解采购单位、供应商及市场趋势。查询需使用平台 API Key，部分查询消耗账户积分。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Automatic trial registration derives a stable device fingerprint from a hashed MAC address and sends it to the platform.

Mitigation: Review the account-creation and privacy implications before consenting; configure ZLBX_API_KEY through normal secret management to skip automatic registration.

Risk: Account setup stores an API key in a home-directory configuration file.

Mitigation: Prefer a managed API key and limit access to any local file containing credentials.

Risk: Some request-control instructions are hidden in Markdown comments.

Mitigation: Review the full skill and request behavior before installation; ask the publisher to make those instructions explicit.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Skill setup documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](references/api-search.md)
- [Market analysis API reference](references/api-market.md)
- [Company analysis API reference](references/api-company.md)
- [Account and registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with links to procurement notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include historical unit prices, project amounts, buyer and supplier details, and trend summaries; availability and contact visibility depend on the account.]

## Skill Version(s):

1.0.10 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

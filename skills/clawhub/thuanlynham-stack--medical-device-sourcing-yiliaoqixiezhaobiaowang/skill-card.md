## Description:

帮助采购人员查询医疗器械与耗材的招标中标信息、品牌型号价格趋势及采购单位数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

医疗采购人员可用它检索医疗器械与耗材的招投标记录，并分析品牌、型号、历史中标价格和采购单位。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional automatic signup sends a MAC-derived device identifier that may allow persistent device recognition.

Mitigation: Prefer configuring your own ZLBX_API_KEY; agree to automatic signup only after considering the device identifier collection.

Risk: Company and product search terms are sent to Zhiliaobiaoxun, and the reviewed materials do not establish its retention or deletion practices.

Mitigation: Avoid including unnecessary sensitive details in searches and review the provider's data handling terms before use.

Risk: Some successful searches consume account credits.

Mitigation: Query only the information needed and check the account balance or daily consumption when managing usage.

## Reference(s):

- [ClawHub release](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [标讯搜索参考](artifact/references/api-search.md)
- [企业分析参考](artifact/references/api-company.md)
- [市场分析参考](artifact/references/api-market.md)
- [企业登记查询参考](artifact/references/api-registry.md)
- [账户查询参考](artifact/references/api-account.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some queries require a ZLBX_API_KEY and consume account credits.]

## Skill Version(s):

1.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

通过招投标数据查询医疗器械与耗材的品牌、型号、历史中标单价及采购单位信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

采购人员、供应商及分析人员可查询中国医疗器械与耗材招投标记录，比较品牌和型号的中标价格，并识别采购单位与潜在供应商。

### Deployment Geography for Use:

China (nationwide)

## Known Risks and Mitigations:

Risk: Vendor API usage and locally stored API keys may expose procurement queries or credentials.

Mitigation: Review the vendor's data handling; protect the API key and use a manually provisioned ZLBX_API_KEY where preferred.

Risk: Trial registration collects device characteristics, including a hashed MAC address, and creates an account.

Mitigation: Obtain the user's informed consent before registration, or use a manually provisioned API key to avoid this path.

Risk: Contact lookup and broad company expansion can expose sensitive business information.

Mitigation: Limit queries to the user's specific need, respect masked contacts, and avoid bulk contact exports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thuanlynham-stack/skills/medical-device-sourcing-yiliaoqixiezhaobiaowang)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Market analysis API reference](artifact/references/api-market.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Account registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with procurement comparisons, prices and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the vendor API and available account credits.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

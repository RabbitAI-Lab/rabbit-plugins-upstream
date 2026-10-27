## Description:

根据库存、销量和提前期生成可复核的逐 SKU 补货清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

中文小店经营者、小说作者和自媒体创作者可用它整理最多 100 个 SKU 的库存表，获得用于采购准备的补货建议、公式依据和缺失字段清单。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incomplete or inaccurate inventory fields, units, or assumptions can make a reorder suggestion unsuitable for purchasing.

Mitigation: Provide the required inventory fields and review quantities, units, and assumptions before purchasing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/xxjrq/skills/shop-stock-reorder-plan-cn)
- [ERPNext README (scope reference)](https://github.com/frappe/erpnext/blob/develop/README.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown table with formula notes, lead-time risk flags, assumptions, and missing fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 100 SKU rows; reorder suggestions are calculated from supplied fields and assumptions for human review.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

将最多20个脱敏订单的SKU、数量、单位、已确认套装组成、赠品条件和包装规则整理为逐单拣货装箱勾选表与拆套组件汇总，适合仓配人员进行当次发货前人工核对；缺单位、套装组成或赠品适用条件时明确列为待确认，绝不猜测附件、赠品或包裹数量。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT No Attribution

## Use Case:

仓配人员可用它将脱敏订单整理成逐单拣货与装箱清单，汇总已确认套装的组件，并标出需要人工补充或核对的信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order data may expose customer information.

Mitigation: Use anonymized order details and omit personal information.

Risk: Missing or inconsistent units, kit contents, or gift conditions can lead to incorrect pick quantities or gift decisions.

Mitigation: Resolve every flagged item manually and confirm gift thresholds before packing.

Risk: The documented installer and repository revision are unpinned.

Mitigation: Review and pin the installer and repository revision before running it.

## Reference(s):

- [ERPNext Packing Slip (business-purpose reference)](https://github.com/frappe/erpnext/blob/develop/erpnext/stock/doctype/packing_slip/packing_slip.json)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown checklist with per-order picks, confirmed kit-component totals, unresolved items, and packaging rules]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [For up to 20 sanitized orders and 100 item or component rows; unresolved units, kit contents, or gift conditions are flagged for manual review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

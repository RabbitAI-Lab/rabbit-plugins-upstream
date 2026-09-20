## Description:

仓储费结算单与库龄明细表逐项核对（仓储费逐行复算、库龄天数−免租期=计费天数、超期附加费复算、合计行勾稽、重复与空缺检测），每条结论都带原文行号。本免费版执行 6 项免费检查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Warehouse, logistics, finance, and reconciliation teams use this skill before payment review to check storage-fee settlement statements and inventory-aging detail for table-internal arithmetic issues, missing fields, duplicate rows, and fee totals. It produces line-cited findings and withholds conclusions when the supplied table is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accounting output could be mistaken for payment authorization or contractual judgment.

Mitigation: Use findings as review aids only; final payment, adjustment, and dispute decisions should be made by qualified finance staff against the applicable contract and source records.

Risk: Documentation inconsistencies around telemetry, --no-stats, and free-versus-full scope may confuse users about behavior.

Mitigation: Confirm the installed release behavior and review the executed and withheld checks before relying on the output.

Risk: The free version deliberately omits several deeper reconciliation checks.

Mitigation: Review the reported scope and withheld checks; perform separate review for out-of-scope items such as contract rate policy, tax, invoices, payment terms, WMS or ERP records, and cross-period comparisons.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/warehouse-storage-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, analysis, shell commands, guidance]

**Output Format:** [Human-readable console text or structured JSON with findings, summary, scope, and disclaimers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient inputs return missing fields rather than conclusions.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

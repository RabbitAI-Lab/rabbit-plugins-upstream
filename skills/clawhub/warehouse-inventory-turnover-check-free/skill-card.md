## Description:

仓库周转与呆滞库存表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, warehouse, and operations staff use this skill during month-end close, reconciliation, or inventory counts to check warehouse turnover and slow-moving inventory tables for arithmetic mismatches, missing fields, duplicate item-warehouse rows, and negative quantities or amounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Warehouse inventory tables may contain sensitive operational or financial data.

Mitigation: Provide only the specific table file that needs checking and avoid adding unrelated business records.

Risk: The free release intentionally omits several checks that may matter for a complete inventory review.

Mitigation: Review the listed checks that were not run before relying on the result for accounting, audit, or policy decisions.

Risk: Chinese-language output and domain-specific terminology may be misunderstood by reviewers who do not work in that language or inventory context.

Mitigation: Have a qualified reviewer confirm the cited rows, formulas, and conclusions before using the output in formal workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/warehouse-inventory-turnover-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON from the local Node.js runner, with Markdown guidance when explaining usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing fields instead of unsupported conclusions.]

## Skill Version(s):

1.0.49 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

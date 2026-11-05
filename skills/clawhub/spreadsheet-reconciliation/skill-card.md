## Description:

Inspect, clean, compare and summarize spreadsheets or tabular lists using lookups, duplicate analysis, reconciliations and pivots. Use when the task is to work through a messy table; use a dedicated validation workflow for the broader acceptance decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Spreadsheet users and analysts use this skill to inspect, clean, compare, and summarize messy workbooks or tabular lists while preserving source data and accounting for duplicate, missing, and ambiguous records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Duplicate exclusions or reconciliation totals can be misleading if workbook rows, keys, or dispositions are misunderstood.

Mitigation: Work from a copy of important workbooks and review duplicate exclusions, match counts, and reconciled totals against the original inputs.

Risk: Formula compatibility claims have not been independently tested for every spreadsheet engine or workbook.

Mitigation: Check formulas and recalculation in the target spreadsheet engine on representative cases, and disclose when results rely on cached values or arithmetic checks.

## Reference(s):

- [Literal-key lookup pattern](references/literal-lookup.md)
- [Worked reconciliation example](references/example.md)
- [Practice: reconcile two lists](references/practice.md)
- [ClawHub release page](https://clawhub.ai/redrookai/skills/spreadsheet-reconciliation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Cleaned or comparison tables, readable summaries, and spreadsheet formulas or operation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source values and reports relevant match, missing, duplicate, and exclusion dispositions.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

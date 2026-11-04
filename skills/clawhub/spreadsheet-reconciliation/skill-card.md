## Description:

Inspect, clean, compare and summarize spreadsheets or tabular lists using lookups, duplicate analysis, reconciliations and pivots. Use when the task is to work through a messy table; use dataset validation for the broader acceptance decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Spreadsheet users and analysts use this skill to inspect, clean, compare, and summarize workbooks or tabular lists, with attention to keys, duplicates, missing values, and reconciliation totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Formula behavior can vary by spreadsheet engine and locale, and compatibility may not have been checked in the user's workbook.

Mitigation: Check the formulas in the target workbook and spreadsheet engine before relying on their results.

Risk: Cleaning or excluding records can change reconciliation totals or obscure why a record was removed.

Mitigation: Preserve original inputs and document each change or exclusion before relying on the summarized results.

## Reference(s):

- [Spreadsheet Reconciliation on ClawHub](https://clawhub.ai/redrookai/skills/spreadsheet-reconciliation)
- [Literal-key lookup pattern](artifact/references/literal-lookup.md)
- [Worked reconciliation example](artifact/references/example.md)
- [Reconciliation practice](artifact/references/practice.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Spreadsheet formulas]

**Output Format:** [Markdown tables and summaries with spreadsheet formula examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source values and documents changes, exclusions, missingness, and ambiguity.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

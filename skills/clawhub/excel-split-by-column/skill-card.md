## Description:

Splits a large Excel workbook into grouped worksheets or separate XLSX files by a selected or auto-detected column, preserving headers and producing split statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dont4getme-2](https://clawhub.ai/user/dont4getme-2)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and agents use this skill to divide employee rosters, orders, registration forms, or inventory sheets by department, city, category, status, or similar columns for distribution or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated workbooks may reproduce sensitive rows from the source spreadsheet.

Mitigation: Process only files appropriate for local handling and review the output location and recipients before sharing generated files.

Risk: Selecting the wrong split column or output mode can produce misleading group files or sheets.

Mitigation: Confirm the intended column and output mode before running the helper and review the printed split statistics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dont4getme-2/skills/excel-split-by-column)
- [ClawHub publisher profile](https://clawhub.ai/user/dont4getme-2)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and generated XLSX workbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates either one workbook with multiple worksheets or multiple XLSX files; prints split counts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents improve existing Excel workbooks by diagnosing formatting, increasing readable font sizes, standardizing borders, adjusting widths and heights, setting zoom, and saving an optimized copy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jes614753-sketch](https://clawhub.ai/user/jes614753-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users can use this skill through an agent when an existing Excel workbook is hard to read or visually inconsistent. The agent applies an inspect-first workflow to improve fonts, borders, column widths, row heights, zoom settings, and output naming while preserving formulas and merged cells.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad visual formatting changes to Excel workbooks.

Mitigation: Keep the original workbook, save an optimized copy, and confirm the formatting plan before applying changes.

Risk: Installing openpyxl from a package mirror introduces dependency trust and availability considerations.

Mitigation: Install only from the named mirror when acceptable for the environment and review dependency installation before execution.

Risk: Formula results may require recalculation after workbook edits.

Mitigation: Preserve formulas during editing and approve any optional LibreOffice recalculation step separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jes614753-sketch/skills/excel-format-optimizer)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, files]

**Output Format:** [Markdown guidance with Python and shell code blocks; optimized .xlsx workbook copies when executed by an agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install openpyxl from a named package mirror, modifies workbook presentation, and may require separate user approval for optional LibreOffice formula recalculation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

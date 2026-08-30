## Description:

Splits a large Excel workbook into grouped worksheets in one file or separate .xlsx files by a specified or auto-detected column, preserving headers and producing split statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dont4getme-2](https://clawhub.ai/user/dont4getme-2)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operations users use this skill to split uploaded Excel tables such as rosters, orders, registrations, or inventory lists by department, city, category, status, or similar columns. It helps prepare grouped workbooks or per-group files for review, reporting, or distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes spreadsheet contents locally and writes new Excel outputs, which can expose sensitive workbook data if the wrong file or output location is used.

Mitigation: Confirm the intended source workbook, split column, mode, and output location before running the command, especially for sensitive spreadsheets.

Risk: A generic request to split data can select an unintended column when auto-detection is used.

Mitigation: Ask the user to specify the split column when the workbook has multiple plausible grouping columns or when the result will be distributed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dont4getme-2/skills/excel-split-by-column)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance, Text]

**Output Format:** [Markdown guidance with bash commands, generated .xlsx files, and split statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create either one workbook with grouped sheets or multiple .xlsx workbooks in an output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

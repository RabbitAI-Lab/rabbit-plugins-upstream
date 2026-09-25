## Description:

Excel公式工具 helps agents generate Excel formulas from natural-language descriptions, explain functions such as VLOOKUP, and diagnose spreadsheet errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, analysts, and developers use this skill to turn spreadsheet requirements into Excel formulas and troubleshooting guidance for common workbook calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact requests broad read, write, and command execution tools while the stated purpose is spreadsheet formula help.

Mitigation: Review before installing and scope use to Excel formula generation and spreadsheet diagnostics unless the publisher narrows the description and permissions.

Risk: The artifact advertises unrelated file-processing and automation capabilities that may cause agents to apply it outside Excel formula assistance.

Mitigation: Treat non-spreadsheet behavior as out of scope and validate generated formulas, commands, and file changes before using them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/excel-formula)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON containing formulas, explanations, diagnostics, and optional command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed before use on live spreadsheets or files.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists 2.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

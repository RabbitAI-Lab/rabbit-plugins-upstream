## Description:

Excel全能工具箱 helps agents inspect, read, write, convert, merge, split, clean, validate, analyze, chart, pivot, compare, insert images into, and protect Excel and CSV workbooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Employees, analysts, operations teams, and developers use this skill to automate local Excel and CSV workbook inspection, cleanup, transformation, reporting, charting, pivoting, comparison, template generation, and password protection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workbook write, protection, encryption, and decryption operations can modify or overwrite important spreadsheet files.

Mitigation: Require explicit output paths for important workbooks, keep an independent backup, and review generated files before replacing originals.

Risk: Business, HR, payroll, and financial spreadsheets may contain sensitive data handled by local automation scripts.

Mitigation: Run the skill only in trusted local environments and provide only files the agent is authorized to process.

Risk: The server security verdict is suspicious because overwrite behavior may differ from the documented backup expectation.

Mitigation: Review write and protection workflows before deployment and avoid relying solely on automatic backup behavior.

## Reference(s):

- [API Reference - mu-excel-toolbox](references/api-reference.md)
- [Scenario Examples - mu-excel-toolbox](references/examples.md)
- [ClawHub Skill Page](https://clawhub.ai/muippt/skills/mu-excel-toolbox)
- [Project Landing Page](https://muippt.github.io/mu-excel-toolbox/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown, JSON, CSV, terminal tables, shell commands, and Excel or CSV file outputs depending on the selected script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operates on local workbook paths and can create, modify, encrypt, decrypt, or convert spreadsheet files.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata; SKILL.md frontmatter says 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

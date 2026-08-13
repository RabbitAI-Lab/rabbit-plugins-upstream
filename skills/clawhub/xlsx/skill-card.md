## Description:

Use this skill when a spreadsheet file is the primary input or output, including opening, reading, editing, fixing, creating, cleaning, formatting, charting, or converting .xlsx, .xlsm, .csv, and .tsv files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisz112](https://clawhub.ai/user/lisz112)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, analysts, and developers use this skill to create, edit, analyze, clean, and convert spreadsheet files while preserving workbook formatting and enforcing formula-quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python and LibreOffice and can modify workbook files during recalculation.

Mitigation: Use the skill on trusted files, keep backups of important workbooks, and review generated commands before execution.

Risk: The bundled artifact includes broader Office-document tooling beyond spreadsheet workflows.

Mitigation: Review or remove non-spreadsheet scripts if the deployment only requires XLSX support.

Risk: LibreOffice setup may write a persistent macro as part of formula recalculation support.

Mitigation: Approve installation only in environments where persistent LibreOffice changes are acceptable and can be audited.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisz112/skills/xlsx)
- [Publisher profile](https://clawhub.ai/user/lisz112)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets and shell commands for producing spreadsheet files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can guide local Python, pandas, openpyxl, and LibreOffice workflows that read, write, recalculate, and validate spreadsheet files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

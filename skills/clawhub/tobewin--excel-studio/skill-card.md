## Description:

Professional Excel spreadsheet generator for creating data tables, reports, charts, financial models, and other structured data in Excel-compatible formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to generate formatted spreadsheets, reports, formulas, charts, and multi-sheet workbooks from structured requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable pip dependencies may be installed in the execution environment.

Mitigation: Install only where mutable pip dependencies are acceptable and review dependency versions before use.

Risk: Spreadsheet data from untrusted sources can be interpreted as formulas when values begin with formula characters.

Mitigation: Treat untrusted formula-like values as text unless formula execution is intended.

Risk: The skill claims XLSX, XLS, and CSV support, while security guidance says to expect XLSX output from the provided workflow.

Mitigation: Validate the generated output format before relying on XLS or CSV deliverables.

## Reference(s):

- [Excel Templates](artifact/references/templates.md)
- [ClawHub Excel Studio release page](https://clawhub.ai/tobewin/skills/excel-studio)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python and shell command blocks that generate local spreadsheet files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local spreadsheet-generation guidance and scripts; provided workflow should be expected to produce XLSX output.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

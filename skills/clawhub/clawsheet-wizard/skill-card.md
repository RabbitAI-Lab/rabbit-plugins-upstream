## Description:

Create, inspect and edit Excel/XLSX files with reliable formulas, data quality checks and template diff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and spreadsheet automation agents use this skill to create, inspect, and edit Excel/XLSX workbooks while checking formulas, data quality, and template drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Python scripts inspect user-selected spreadsheet files and may produce reports that are incomplete or require interpretation.

Mitigation: Run the scripts only on spreadsheets you intend to analyze and review generated reports before acting on them.

Risk: The documentation describes auto-fix behavior more strongly than the current formula checker implements.

Mitigation: Keep workbook backups and manually review formula issues before relying on any repaired or regenerated workbook.

## Reference(s):

- [ClawSheet Wizard on ClawHub](https://clawhub.ai/northcap-group/skills/clawsheet-wizard)
- [northcap-group publisher profile](https://clawhub.ai/user/northcap-group)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Code]

**Output Format:** [Markdown guidance with inline shell commands and local Python script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be printed to stdout or written to Markdown files; scripts require python3 plus pandas or openpyxl for workbook analysis.]

## Skill Version(s):

1.0.10 (source: evidence.release.version; artifact frontmatter and _meta.json report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

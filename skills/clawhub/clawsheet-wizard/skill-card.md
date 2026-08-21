## Description:

Create, inspect and edit Excel/XLSX files with reliable formulas, data quality checks and template diff. Spreadsheet automation for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and spreadsheet-heavy teams use this skill to inspect Excel workbooks, check formulas, produce data quality reports, compare workbook templates, and guide reliable spreadsheet edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads spreadsheet files named by the user, which may contain sensitive workbook data.

Mitigation: Use it only with workbooks the agent is allowed to inspect, and avoid providing files outside the intended task scope.

Risk: Spreadsheet edits or generated reports can affect decisions if formulas, types, or workbook structure are misunderstood.

Mitigation: Keep backups before editing workbooks and review formula checks, data quality reports, and template diffs before relying on the results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/clawsheet-wizard)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; helper scripts may require pandas or openpyxl for workbook inspection.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

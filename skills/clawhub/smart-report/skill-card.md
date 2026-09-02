## Description:

Data-to-report skill. Turns data files (CSV/Excel/JSON) into single-file interactive HTML reports with ECharts visualizations, narrative analysis and full numeric traceability (fact ledger).

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to turn intentionally provided CSV, Excel, or JSON data into single-file interactive HTML reports with charts, narrative analysis, and traceable numeric claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-generated pandas/Python transform snippets may run locally, and the sandbox should not be treated as a strong security boundary.

Mitigation: Use a disposable virtual environment or container, run the skill only on data files you intentionally provide, and review transform_code when possible.

Risk: Generated reports can contain misleading conclusions if transforms, aggregation choices, or source data are wrong.

Mitigation: Check the fact ledger, plot_stats, and data_preview values before relying on narrative claims or publishing the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/smart-report)
- [Publisher profile](https://clawhub.ai/user/neuhanli)
- [REFERENCE.md](references/REFERENCE.md)
- [REPORT.md](references/REPORT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON configuration, shell commands, and generated single-file HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline ECharts assets are bundled; supported inputs are CSV, TSV, TXT, XLSX, XLS, and JSON.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

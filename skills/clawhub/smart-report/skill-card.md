## Description:

Turns CSV, TSV, TXT, Excel, and JSON data into single-file interactive HTML reports with ECharts visualizations, free-form narrative, traceable fact and claims ledgers, and optional standalone chart generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and reporting agents use this skill to convert local tabular data into evidence-traceable reports, charts, and delivery-ready analysis documents. It is intended for report writing, recurring business reviews, data analysis briefs, retrospectives, and chart packages from supplied data files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated local Python transforms may run during report creation.

Mitigation: Review transform logic before execution, use trusted input data, and run the skill in a constrained environment.

Risk: Optional static export can evaluate chart JavaScript through local Node tooling.

Mitigation: Prefer HTML-only output when possible, avoid externally supplied chart HTML, and remove sensitive environment variables before DOCX/PPTX export.

## Reference(s):

- [Smart Report on ClawHub](https://clawhub.ai/neuhanli/skills/smart-report)
- [REPORT.md](artifact/references/REPORT.md)
- [REFERENCE.md](artifact/references/REFERENCE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON specifications, shell commands, and generated report artifacts such as HTML reports and optional DOCX or PPTX exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report outputs are designed around fact and claims ledgers; optional DOCX/PPTX export depends on additional local tooling.]

## Skill Version(s):

1.4.1 (source: server release metadata and user changelog; artifact frontmatter says 1.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

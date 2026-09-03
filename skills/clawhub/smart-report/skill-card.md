## Description:

Smart Report turns CSV, TSV, TXT, Excel, and JSON data files into single-file interactive HTML reports with ECharts visualizations, narrative analysis, numeric traceability, and optional standalone chart HTML generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and business users use this skill to generate narrative reports, weekly or monthly reports, reviews, presentation material, and chart outputs from local tabular data files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run generated pandas transform code on local data through an in-process exec-based sandbox.

Mitigation: Use trusted data, review unusual transform_code before execution, and avoid sensitive business files unless this execution model is acceptable.

Risk: Server-resolved source provenance is unavailable for this release.

Mitigation: Do not infer GitHub provenance; verify source lineage through the ClawHub publisher profile before enterprise deployment.

## Reference(s):

- [Smart Report CLI and Capability Reference](artifact/references/REFERENCE.md)
- [Report Assembly and Fact Ledger Specification](artifact/references/REPORT.md)
- [ClawHub Smart Report Skill Page](https://clawhub.ai/neuhanli/skills/smart-report)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON configuration and shell commands; generated artifacts are self-contained HTML reports or standalone HTML charts with ledger and spec JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs offline with bundled ECharts assets; supports CSV, TSV, TXT, XLSX, XLS, and one-level JSON inputs; report numbers are expected to trace to ledger.json.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

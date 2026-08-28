## Description:

Smart Charts helps agents analyze CSV, Excel, TSV, TXT, and JSON data files and generate interactive offline ECharts HTML visualizations with optional LLM-assisted pandas transformations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to inspect tabular data, choose suitable chart types, run bounded pandas transformations when needed, and deliver chart files with concise written interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LLM-generated pandas/Python transformation code may run locally under a sandbox that the scan describes as overstated.

Mitigation: Use the skill in a disposable or constrained environment, review generated transform code when practical, and avoid running it on files that require stronger isolation.

Risk: Generated previews, JSON outputs, and HTML chart files may contain raw values from user-provided datasets.

Mitigation: Do not provide credentials, private records, or regulated data unless that exposure is acceptable; review generated files before sharing them.

## Reference(s):

- [Smart Charts reference](artifact/references/REFERENCE.md)
- [ClawHub skill release page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands, pandas transform snippets, JSON CLI results, and generated HTML chart files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML charts inline bundled ECharts assets for offline viewing; CLI results include data previews, row counts, assumptions, and plot statistics.]

## Skill Version(s):

7.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

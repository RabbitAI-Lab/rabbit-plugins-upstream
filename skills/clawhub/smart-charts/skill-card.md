## Description:

Smart Charts turns CSV, TSV, TXT, Excel, or JSON tabular data into standalone offline ECharts HTML visualizations with traceable preview and plot statistics for captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and external users use this skill when an agent has a tabular data file and needs to generate an interactive chart with source-backed caption facts instead of a narrative report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated transform code runs in-process and may not be fully contained by the skill's own sandbox claims.

Mitigation: Install only from a trusted publisher, review generated transforms, run with network disabled and limited filesystem access, and write outputs to a disposable user-visible folder.

Risk: Untrusted prompts or data could induce unsafe or misleading transform code or chart assumptions.

Mitigation: Avoid transform execution on untrusted prompts or data, and verify chart facts against the emitted data_preview, data_rows, source_rows, plotted_rows, unique_entities, and plot_stats before reuse.

## Reference(s):

- [Smart Charts reference](references/REFERENCE.md)
- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Code]

**Output Format:** [Standalone HTML charts with JSON CLI output and concise annotation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts render offline with bundled ECharts assets and include data_preview and plot_stats for traceability.]

## Skill Version(s):

8.2.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

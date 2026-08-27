## Description:

Intelligent chart generation and data analysis skill. Reads user-supplied data files (CSV/Excel/JSON), analyzes data characteristics with LLM assistance, auto-recommends and generates interactive ECharts visualizations. Use when the user asks to analyze data, generate charts, create visualizations, or work with tabular data files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to inspect local tabular data files and generate offline interactive HTML charts. It is suited for data analysis and visualization workflows that need chart recommendations, pandas transforms, chart artifacts, and concise interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically runs model-generated pandas transform code under an overstated sandbox claim.

Mitigation: Use trusted datasets, review transform code before execution in sensitive workflows, and run the skill in a contained environment for private or high-value data.

Risk: The skill reads local data files and writes generated HTML charts that may contain sensitive source data or derived summaries.

Mitigation: Limit input paths to intended datasets and treat generated HTML outputs as sensitive until reviewed.

Risk: Generated charts and interpretations can be misleading if the transform uses the wrong aggregation grain or chart inputs.

Mitigation: Check the CLI's data_preview, data_rows, and plot_stats fields before relying on or sharing the chart interpretation.

## Reference(s):

- [Reference](artifact/references/REFERENCE.md)
- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash and Python snippets; generated artifacts are offline HTML charts with JSON CLI status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local CSV, TSV, TXT, Excel, and JSON files; writes interactive ECharts HTML; network access is not required.]

## Skill Version(s):

7.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

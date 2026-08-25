## Description:

Intelligent chart generation and data analysis skill. Reads user-supplied data files (CSV/Excel/JSON), analyzes data characteristics with LLM assistance, auto-recommends and generates interactive ECharts visualizations. Use when the user asks to analyze data, generate charts, create visualizations, or work with tabular data files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other agent users use this skill to parse tabular CSV, Excel, text, and JSON data, choose suitable chart types, and generate standalone interactive ECharts HTML visualizations. It is intended for local chart generation workflows that can tolerate review of generated transformation code and output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LLM-generated pandas transformation code runs locally and the provided sandbox is not a substitute for security review.

Mitigation: Review generated transform code before use, avoid adversarial prompts or untrusted transform snippets, and run the skill in an isolated environment when handling unfamiliar data.

Risk: Generated HTML charts may contain portions of the input or transformed dataset.

Mitigation: Treat chart files as data-bearing artifacts and share them only where the underlying dataset is approved for disclosure.

Risk: Unsupported inputs such as databases, streaming data, geo maps, files over 100 MB, deeply nested JSON, or non-tabular media can produce failed or misleading workflows.

Mitigation: Convert data to supported tabular formats first, keep files within documented limits, and report unsupported scenarios instead of forcing a chart.

## Reference(s):

- [Smart Charts Reference](references/REFERENCE.md)
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, pandas transform code, JSON status output, and generated HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated charts are standalone HTML files with bundled ECharts assets; successful CLI runs report the chart path in JSON.]

## Skill Version(s):

6.2.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

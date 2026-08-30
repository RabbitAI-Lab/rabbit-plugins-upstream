## Description:

Smart Charts helps agents analyze user-supplied CSV, Excel, and JSON data and generate offline interactive ECharts HTML visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use Smart Charts to inspect tabular data, choose suitable chart types, generate offline interactive HTML charts, and deliver short chart interpretations grounded in the tool output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated pandas transformation code runs locally in an in-process sandbox that security evidence describes as weak.

Mitigation: Review generated transformation code before use, run it only on data intentionally provided for charting, and prefer a controlled directory or isolated environment for outputs.

Risk: Untrusted prompts or files could influence transform_code and produce misleading or unsafe transformations.

Mitigation: Avoid using untrusted prompts or files to drive transform_code, and verify chart assumptions against the CLI data preview and plot statistics before relying on results.

## Reference(s):

- [Smart Charts Reference](artifact/references/REFERENCE.md)
- [Smart Charts Skill Definition](artifact/SKILL.md)
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output; chart artifacts are offline HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports CSV, TSV, TXT, Excel, and JSON inputs up to 100 MB; chart HTML renders without network access.]

## Skill Version(s):

8.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

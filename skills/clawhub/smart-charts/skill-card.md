## Description:

Intelligent chart generation and data analysis skill that reads user-supplied CSV, Excel, TSV, TXT, and JSON files, analyzes data characteristics with LLM assistance, and generates interactive ECharts visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other external users use this skill to inspect tabular data files, choose suitable chart types, transform data when needed, and produce offline interactive HTML visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may execute AI-generated pandas transformation code locally.

Mitigation: Use trusted datasets, review generated transform intent when handling sensitive data, and rely on the documented sandbox restrictions before running chart generation.

Risk: Generated HTML is active content and may include values from the source dataset.

Mitigation: Open outputs in a contained environment and avoid sharing generated HTML unless the embedded data is approved for disclosure.

Risk: The server security verdict recommends review before installation.

Mitigation: Review the skill and its local execution behavior before deployment, especially in environments with sensitive files or regulated datasets.

## Reference(s):

- [Smart Charts Reference](artifact/references/REFERENCE.md)
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, shell commands, Python transform code, JSON CLI results, and generated offline HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML is active browser content and may include source data; chart generation uses local file reads and writes.]

## Skill Version(s):

6.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

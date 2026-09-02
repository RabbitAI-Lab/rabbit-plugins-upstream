## Description:

Intelligent chart generation and data analysis skill that reads user-supplied CSV, Excel, and JSON files, analyzes data characteristics with LLM assistance, and generates interactive ECharts visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to convert tabular data files into interactive chart outputs and accompanying analysis. It is intended for chart generation, data visualization, and lightweight data exploration workflows using local CSV, Excel, and JSON files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically run generated pandas transformation code while processing local CSV, Excel, and JSON files.

Mitigation: Use it on non-sensitive datasets or inside an isolated environment, and review generated transform code before running it when the prompt or data source is untrusted.

Risk: The in-process blacklist and AST sandbox reduce exposure but should not be treated as a complete security boundary.

Mitigation: Review the skill before deployment and avoid granting it access to sensitive files or broad write locations unless the deployment environment is controlled.

## Reference(s):

- [Reference](references/REFERENCE.md)
- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, files, guidance]

**Output Format:** [Markdown guidance with shell commands, generated transform code, JSON status output, and interactive HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are produced from local tabular files and may include chart annotations, data previews, and plot statistics used for interpretation.]

## Skill Version(s):

8.1.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

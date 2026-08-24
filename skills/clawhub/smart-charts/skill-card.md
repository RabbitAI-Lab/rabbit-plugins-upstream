## Description:

Intelligent chart generation and data analysis skill that reads user-supplied CSV, Excel, JSON, TSV, or text files, analyzes tabular data characteristics with LLM assistance, and generates interactive ECharts visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and analysts use this skill to turn local tabular data files into offline interactive HTML charts and concise data-analysis deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Python transformation snippets execute locally in the agent process, and the stated sandbox should not be treated as a strong security boundary.

Mitigation: Use the skill on non-sensitive data when possible, review transform code before execution, and run it in a controlled workspace with limited file access.

## Reference(s):

- [Smart Charts reference](references/REFERENCE.md)
- [Smart Charts ClawHub page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated offline HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated charts are local HTML files with bundled ECharts assets and no network requirement.]

## Skill Version(s):

6.1.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

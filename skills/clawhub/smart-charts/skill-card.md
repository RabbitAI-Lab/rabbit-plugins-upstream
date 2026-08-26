## Description:

Intelligent chart generation and data analysis skill that reads user-supplied CSV, Excel, JSON, TSV, or text files, analyzes data characteristics with LLM assistance, and generates interactive offline ECharts visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to turn local tabular data files into interactive HTML charts and data visualization reports. It is suited for offline chart generation, data-shape inspection, and chart recommendations across common CSV, Excel, JSON, TSV, and text inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run generated pandas transformation code locally in a weak sandbox that may reach local file operations.

Mitigation: Run it in an isolated workspace or container, avoid exposing unrelated sensitive files, and review non-trivial transformation code before use.

Risk: The skill reads and writes local files while processing user-supplied datasets up to the documented size limit.

Mitigation: Limit the working directory to intended datasets and review generated HTML files before sharing them outside the workspace.

## Reference(s):

- [Smart Charts Reference](references/REFERENCE.md)
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with CLI commands, JSON status output, and offline HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated charts are local HTML files with bundled ECharts assets; no network access is required.]

## Skill Version(s):

6.2.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

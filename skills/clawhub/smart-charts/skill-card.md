## Description:

Intelligent chart generation and data analysis skill. Reads user-supplied data files (CSV/Excel/JSON), analyzes data characteristics with LLM assistance, auto-recommends and generates interactive ECharts visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other agent users use this skill to inspect CSV, Excel, or JSON data, choose an appropriate chart type, and generate interactive ECharts HTML visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated transformation code is executed in-process.

Mitigation: Review generated transform code when possible and run the skill in an isolated workspace, especially for sensitive or high-impact data.

Risk: Generated HTML charts may persist or expose user data.

Mitigation: Use non-sensitive data where possible and avoid sharing generated HTML files that contain private records.

Risk: Generated charts may load ECharts assets from public CDNs.

Mitigation: Use an offline or pinned local ECharts asset when generated charts may contain private data or when network dependency is undesirable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/neuhanli/skills/smart-charts)
- [Smart Charts reference](REFERENCE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated HTML chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated chart HTML may load ECharts from a CDN and may include transformed user data.]

## Skill Version(s):

5.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

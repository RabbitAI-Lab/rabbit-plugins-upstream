## Description:

Opportunities evaluates patent opportunity for a focused technology direction or technical solution by using PatSnap patent search and statistics tools to produce a traceable multi-page report with charts, data files, evidence mapping, scores, and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D, intellectual-property, and investment teams use this skill to evaluate whether a specific technology area is worth entering, using patent trend data, subfield statistics, representative patents, evidence-linked claims, and generated report files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authorized PatSnap MCP access for patent searches and statistics.

Mitigation: Install and run it only in an environment where the user is comfortable authorizing PatSnap MCP access.

Risk: Generated HTML reports fetch fonts and ECharts from external CDNs.

Mitigation: Open generated reports with awareness of those external requests, or modify templates to use local assets before viewing in restricted environments.

Risk: The skill creates a multi-file local report.

Mitigation: Use a dedicated output folder for each run to keep generated report files isolated and easier to review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/opportunities)
- [PatSnap open platform](https://open.zhihuiya.com/)
- [Example input](references/examples/example_input.md)
- [Example output structure](references/examples/example_output_structure.md)
- [ECharts 5.4.3](https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Multi-file report outputs including HTML, Markdown, JSON, and CSV files, plus a concise final text summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a required 10-file local report and uses claim_id labels to connect important conclusions to evidence sources.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

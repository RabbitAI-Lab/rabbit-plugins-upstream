## Description:

Analyzes fixed-camera office video to produce anonymous, zone-level workplace stress indices, heatmap colors, trends, and manager-facing suggestions for organizational health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace health, operations, and facilities teams use this skill to analyze office-area camera footage at an aggregate zone level, review stress heatmaps and trends, and support workplace environment planning without individual employee conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace footage is sent to a configured cloud service for analysis.

Mitigation: Confirm employee notice and consent, approved video sources, retention limits, and access controls before deployment.

Risk: The skill creates or reuses a persistent local or cloud identity for report history.

Mitigation: Review identity handling, report access permissions, and history retention so reports cannot be linked or exposed beyond the approved audience.

Risk: Stress heatmaps can be misused as individual performance, diagnosis, or surveillance signals.

Mitigation: Use only aggregate zone-level outputs, honor the minimum sample threshold, and prohibit individual employee conclusions or performance decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)
- [API interface reference](references/api_doc.md)
- [SMYX analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON analysis reports with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to be anonymous, zone-level aggregate workplace stress summaries, heatmap references, trends, alerts, and manager suggestions.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes workplace camera images or video to produce anonymous, zone-level group stress reports and heatmap-style outputs for organizational health monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise managers, workplace health teams, and developers use this skill to submit open-office camera footage or URLs and receive anonymous, area-level stress distribution reports, trend summaries, heatmap links, and manager-facing suggestions. It is intended for organizational health monitoring, not individual diagnosis, performance evaluation, or discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive workplace footage and sends analysis tasks or history lookups to cloud services.

Mitigation: Use it only with clear employee notice, lawful consent, approved upload destinations, and strict access and retention controls for footage, reports, tokens, and history.

Risk: Stress heatmap outputs could be misused as individual performance, diagnosis, disciplinary, or profiling evidence.

Mitigation: Restrict use to aggregated area-level organizational health monitoring and require policy controls that prohibit individual conclusions or employment actions from the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)
- [Workplace stress heatmap API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON report text with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces area-level aggregate stress metrics, heatmap links, historical report tables, alerts, and manager suggestions; individual identification is outside the stated output scope.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes approved fixed-camera office video anonymously to produce zone-level group stress indices, heatmap colors, trends, and manager-facing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workplace health or facilities teams use this skill to submit approved office camera footage or URLs and receive anonymous, zone-level stress heatmaps and structured reports for organizational-health monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Office footage and workplace stress outputs can be sensitive employee data.

Mitigation: Install only after workplace privacy and legal review; confirm employee notice or consent where required, approved camera sources, retention limits, and no personal profiling or performance use.

Risk: The skill uploads office footage to a remote service while creating or reusing local account identity and token state.

Mitigation: Confirm the remote service endpoint and local data/smyx-common-claw.db and data/smyx-api-key.txt behavior are acceptable before deployment.

Risk: Small groups in a workstation zone may make aggregate stress output effectively identifying.

Mitigation: Keep the documented minimum-sample protection and suppress stress_index for zones with fewer than 3 people.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured report text, Markdown tables for history views, or JSON detail output with report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include zone-level aggregate stress fields, trend fields, manager suggestions, and heatmap or report URLs; individual identity output is not intended.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

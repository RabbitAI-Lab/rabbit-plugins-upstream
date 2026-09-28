## Description:

Analyzes workplace camera footage to produce zone-level stress heatmaps, reports, and suggestions for managers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace managers and organizational health teams use fixed-camera footage to review aggregated stress indicators by office zone, view heatmaps, and consult historical reports when planning workplace improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workplace camera footage or video URLs may be sent to an external service.

Mitigation: Obtain clear employee notice and consent before use, limit retention, and approve the external service and its access controls.

Risk: Persistent internal user and report identities may undermine expectations of anonymous group-only analysis.

Mitigation: Verify that the service enforces anonymous, zone-level processing and restrict access to identities and historical reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured report or JSON; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Zone-level stress indicators, heatmap links, and manager suggestions; historical report links when requested.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

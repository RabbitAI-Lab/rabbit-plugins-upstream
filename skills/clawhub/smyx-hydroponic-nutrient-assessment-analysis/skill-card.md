## Description:

This skill analyzes hydroponic root and leaf images or videos to provide a qualitative visual assessment of nutrient concentration status and adjustment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and hydroponic growers use this skill to assess whether nutrient solution appears too concentrated, too dilute, or suitable from plant root and leaf imagery. It can also retrieve account-linked historical assessment reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or media URLs may be sent to the configured LifeEmergence/Open API service for analysis.

Mitigation: Use non-sensitive plant media, prefer isolated workspaces, and confirm endpoint ownership, retention, and deletion controls before deployment.

Risk: The skill can create or reuse a local account identity, store tokens locally, and retrieve cloud report history under that identity.

Mitigation: Avoid shared workspaces for execution, review local data storage expectations, and limit use to accounts whose report history may be safely queried.

Risk: The nutrient concentration result is based on visual symptoms and may be less precise than instrumented EC or ppm measurement.

Mitigation: Treat output as cultivation guidance and verify material decisions with appropriate measurement tools or expert review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [Hydroponic nutrient assessment API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or text containing structured analysis results, qualitative nutrient status, adjustment advice, and report links; JSON is available for detailed output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual assessment is qualitative and does not provide EC or ppm values; results may also be written to an output file when requested.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter declares 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

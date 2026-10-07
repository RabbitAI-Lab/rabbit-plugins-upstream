## Description:

Analyzes children's nighttime sleep recordings for rollovers, crying, and sleep talking, then provides sleep-quality reports and possible-restlessness alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers can use this skill to review children's nighttime sleep recordings, identify possible restlessness, and view sleep reports and historical results. Its findings are parenting aids, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's sleep audio/video or media URLs are sent to a cloud service.

Mitigation: Obtain guardian consent and confirm the service's retention and deletion terms before uploading.

Risk: Reports are linked to an automatically managed identity, with tokens stored locally.

Mitigation: Review token storage and access controls, and check whether history lookup and uploads can be enabled per run.

Risk: Restlessness and possible-nightmare alerts may be mistaken for medical diagnoses.

Mitigation: Use results only as parenting guidance and consult a pediatric or sleep specialist for persistent concerns.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured sleep-analysis report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and an optional saved result file.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

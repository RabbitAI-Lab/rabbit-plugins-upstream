## Description:

Analyzes classroom video to summarize class engagement, highlight low-engagement seat positions, and suggest teaching adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and school staff use the skill to review classroom video or report history for class-level engagement trends and teaching suggestions, with consent when students are filmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom videos or URLs containing minors are sent to the publisher's cloud service.

Mitigation: Obtain explicit school and parent consent, confirm the intended use and retention period, and share only necessary footage.

Risk: Persistent identities and tokens can link report history to an account in a shared workspace.

Mitigation: Avoid shared workspaces and disable history use until the publisher clarifies identity isolation and retention controls.

Risk: Visual engagement cues can misclassify ordinary classroom behavior.

Mitigation: Have teachers review trends in context; do not use seat alerts for individual evaluation or ranking.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-classroom-engagement-analysis-analysis)
- [Classroom engagement API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report or JSON analysis result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include engagement scores, seat-coordinate alerts, teaching suggestions, heatmap links, and report-history links.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

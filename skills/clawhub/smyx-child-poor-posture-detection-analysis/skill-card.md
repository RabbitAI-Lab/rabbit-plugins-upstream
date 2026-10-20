## Description:

Analyzes children's desk-area posture videos to estimate spinal curvature and head tilt, and provides posture findings and reminder text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and developers of study-area monitoring tools use this skill to review a child's posture video, receive reminder text, and retrieve prior posture reports. Visual estimates are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos of children or their URLs are sent to a remote analysis service.

Mitigation: Review the service before installation, obtain guardian consent, and share only media authorized for analysis.

Risk: History and report requests automatically link an identity to cloud-stored reports.

Mitigation: Avoid the history feature unless automatic identity linkage and cloud report retrieval are acceptable.

Risk: Camera-based spinal curvature estimates can be mistaken for a clinical assessment.

Mitigation: Use findings only as posture reminders, not as medical diagnoses or substitutes for clinical evaluation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [Posture analysis API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Posture findings and reminder text; JSON analysis results or a Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to cloud-hosted reports; does not produce audio or a medical diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release metadata; bundled SKILL.md says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

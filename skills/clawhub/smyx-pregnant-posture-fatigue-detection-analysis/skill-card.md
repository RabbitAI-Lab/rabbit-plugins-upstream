## Description:

Uses a fixed home camera to detect prolonged standing, bending, and related posture of a pregnant woman, track standing duration and bending frequency, and assess fatigue risk, with rest reminders for health reference only and not medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and care-program operators use this skill to analyze pregnancy-related home camera video or image input for posture, prolonged-standing duration, bending frequency, fatigue-risk reminders, and historical report lookup. Outputs are intended as health-reference monitoring and reminders, not medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pregnancy-related home footage or video URLs may be sent to remote API services.

Mitigation: Obtain explicit consent from the monitored person, use only appropriate footage, prefer privacy-preserving capture modes when available, and verify configured endpoints before use.

Risk: Reports may be associated with a persistent account identity, and tokens or profile data may be stored locally in the workspace.

Mitigation: Restrict workspace access, review local storage handling before deployment, and remove local credentials or account data when they are no longer needed.

Risk: The skill provides pregnancy-related fatigue reminders that could be mistaken for medical advice.

Mitigation: Present results only as visual posture and activity monitoring; direct users to qualified medical care for symptoms or clinical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pregnant-posture-fatigue-detection-analysis)
- [Pregnant posture fatigue detection API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown summaries and JSON reports with posture metrics, fatigue-risk alerts, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Historical report queries may return Markdown tables with cloud report links.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Based on computer vision, this skill analyzes respiratory videos or image inputs to detect coughing, phlegm, and wheezing episodes, count symptom frequency, and produce early health-alert reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit respiratory monitoring media or URLs for cloud-backed symptom analysis, history lookup, risk scoring, and health-monitoring reports. Results are for health reference and early anomaly alerts, not professional diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Respiratory videos, images, or URLs may be sent to LifeEmergence cloud services for analysis.

Mitigation: Use only media that the user is authorized to share, and avoid patient or regulated health data unless consent, retention terms, and backend authorization assurances are clear.

Risk: Reports can be linked to an internal identity and history lookup can retrieve cloud-stored reports.

Mitigation: Review identity linkage and history access behavior before deployment, and restrict use to environments where report access controls are acceptable.

Risk: Local account or token state may be stored in the workspace.

Mitigation: Run in a controlled workspace, review local state handling, and clear stored state when it is no longer needed.

Risk: Health outputs may be mistaken for medical diagnosis.

Mitigation: Present results as health reference and early anomaly alerts only, and direct users to professional medical care for diagnosis or urgent symptoms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [Respiratory symptom recognition API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports, JSON responses, and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include symptom counts, risk levels, health warnings, medical suggestions, history tables, report links, and optional saved output files.]

## Skill Version(s):

1.0.14 (source: server release metadata; SKILL.md frontmatter remains 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

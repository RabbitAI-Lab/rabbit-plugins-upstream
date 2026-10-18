## Description:

Analyzes children's nighttime audio and video for restless-sleep events and produces sleep-quality reports and possible-nightmare alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to review children's nighttime movements, crying, and sleep talking and receive sleep-quality summaries and possible-restlessness alerts. Its reports are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's bedroom audio and video may be sent to a cloud service.

Mitigation: Obtain guardian consent and confirm the service's retention, deletion, and access controls before using real recordings.

Risk: The skill silently creates and stores identity tokens in a local workspace database and can retrieve cloud report history.

Mitigation: Review account creation and storage behavior, restrict access to the workspace and reports, and use it only if this data flow is acceptable.

Risk: Possible-nightmare alerts and sleep-quality assessments may be mistaken for diagnoses.

Mitigation: Treat results as behavioral observations rather than medical advice; consult a clinician for persistent concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-nightmare-rollover-detection-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Reports, Guidance]

**Output Format:** [Markdown summaries and tables, with optional JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event counts, sleep-quality assessments, alerts, and report links.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

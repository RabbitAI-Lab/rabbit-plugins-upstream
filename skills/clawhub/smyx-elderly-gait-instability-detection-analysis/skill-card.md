## Description:

Analyzes fixed-camera walking videos of an elderly person to estimate gait metrics such as step length, gait speed, trunk sway, and cadence, then reports gait stability and fall-risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, rehabilitation staff, and developers can use this skill to analyze walking videos for objective gait metrics, gait-pattern summaries, and low/medium/high fall-risk screening. Results are auxiliary screening information and do not replace professional medical evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health-related gait videos and reports are sent to a configured cloud service.

Mitigation: Use only with informed consent from the recorded person or their authorized caregiver, and avoid uploading videos unless the deployment's privacy, retention, and deletion terms are acceptable.

Risk: The skill silently creates or reuses an identity and stores authentication tokens locally.

Mitigation: Review account-binding and token-storage behavior before installation, restrict filesystem access where possible, and prefer a release that documents token storage and deletion controls.

Risk: History lookup can retrieve cloud-stored reports with limited user confirmation.

Mitigation: Require operator confirmation before report-history retrieval and verify that the active identity is authorized to access the reports.

Risk: Fall-risk output and gait metrics may be mistaken for clinical diagnosis.

Mitigation: Present results as auxiliary screening only and route concerning findings to qualified medical or rehabilitation professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance]

**Output Format:** [Markdown or JSON text with optional saved result files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes structured gait metrics, fall-risk level, risk factors, alert text, medical follow-up hints, and cloud report history when requested.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

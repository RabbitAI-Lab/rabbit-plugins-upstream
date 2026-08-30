## Description:

Non-contact detection of heart rate, respiration, blood oxygen, and heart rate variability using camera footage without wearable devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit face-camera video files or video URLs for non-contact vital-sign analysis and to retrieve cloud-hosted analysis report history. The generated reports are for health reference and should not be treated as professional medical measurements or diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face or video health data and provided video URLs may be sent to the configured LifeEmergence/SMYX service.

Mitigation: Use the skill only with data approved for that service, verify the configured endpoint before execution, and avoid submitting sensitive videos unless the service terms and data handling are acceptable.

Risk: Cloud report history is tied to an internal identity and local workspace storage may contain account identifiers or service tokens.

Mitigation: Restrict workspace access, review local data storage before sharing or archiving the workspace, and rotate or remove service tokens when access is no longer needed.

Risk: Packaged development configuration includes private network endpoints.

Mitigation: Confirm production endpoints and configuration values before installation or execution in any shared or commercial environment.

Risk: Vital-sign outputs are health-reference reports rather than professional medical measurements.

Mitigation: Present results with the medical-use limitation and direct users to professional care for concerning or abnormal findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; execution returns JSON-like text reports and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local mp4/avi/mov files up to 10MB or a video URL; history lookup returns report lists from the configured cloud API.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter is 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

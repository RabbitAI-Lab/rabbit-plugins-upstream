## Description:

Based on facial video, this skill identifies abnormal rhythms such as premature beats, atrial fibrillation, tachycardia, and bradycardia to support early heart-health risk screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit facial video or a video URL for non-contact arrhythmia early-warning analysis and to retrieve prior cloud-hosted heart-risk reports. Results are screening support only and do not replace ECG testing or clinician diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive facial health video is uploaded to a cloud service and prior health reports can be retrieved.

Mitigation: Use only with appropriate consent and non-sensitive or approved media until data handling, retention, and report access controls are documented.

Risk: The skill silently creates or reuses an internal identity and stores service tokens locally.

Mitigation: Require explicit consent controls and secure credential storage before production use; review and clear local identity or token state during testing.

Risk: Active plaintext development endpoints are present in shipped configuration.

Mitigation: Verify that only production HTTPS endpoints are enabled before installation and remove or disable plaintext development endpoints.

Risk: Arrhythmia output is an early-warning screening result, not a medical diagnosis.

Mitigation: Present results as informational screening support and direct users with high-risk findings to professional ECG testing and clinician review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Arrhythmia API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a caller-provided file path; history queries return cloud report records with export links when available.]

## Skill Version(s):

1.0.17 (source: server release metadata; artifact frontmatter reports 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

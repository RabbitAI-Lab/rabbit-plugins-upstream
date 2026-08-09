## Description:

Based on facial video, identifies abnormal rhythms such as premature beats, atrial fibrillation, tachycardia/bradycardia, assists in early detection of heart health risks. | 心律失常早期预警技能，基于面部视频识别早搏、房颤、心动过速/心动过缓等异常节律，辅助心脏健康风险早发现

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit facial video for non-contact arrhythmia early-warning screening and to retrieve structured health-risk reports from the cloud service. Results should be treated as risk-screening information, not as a substitute for ECG testing or diagnosis by a cardiology professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive facial video and health-screening data may be uploaded to the lifeemergence cloud service.

Mitigation: Use only with informed consent, confirm that the service's privacy and retention terms are acceptable, and avoid highly sensitive videos unless the deployment has approved that data flow.

Risk: The skill may create or reuse a cloud-linked identity and retain account tokens in local workspace data.

Mitigation: Run only in trusted workspaces, restrict access to local skill data, and clear retained account data when the skill is no longer needed.

Risk: Historical health reports can be fetched from the cloud service.

Mitigation: Require explicit user confirmation before history lookups and verify that the current user is authorized to access the report history.

Risk: Arrhythmia early-warning output may be mistaken for a clinical diagnosis.

Mitigation: Present results as screening guidance only and direct high-risk users to professional ECG testing and cardiology review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-arrhythmia-early-warning-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown text with structured JSON content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write results to a user-selected output file; local inputs are limited to mp4, avi, or mov up to 10MB.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

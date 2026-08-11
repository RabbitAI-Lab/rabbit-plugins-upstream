## Description:

Based on computer vision, this skill analyzes respiratory-health videos to detect and count coughing, phlegm, and wheezing episodes for early anomaly alerts. | 基于计算机视觉分析呼吸道健康视频，检测并统计咳嗽、咳痰、喘息发作频次，用于健康异常早期提醒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit local respiratory-health videos or public video URLs for cloud-based symptom recognition, structured monitoring reports, and report-history lookup. It is intended for health reference and early anomaly awareness, not as a substitute for professional medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends respiratory-health videos or URLs to the Life Emergence cloud service.

Mitigation: Use only media that the user is authorized to process and avoid sensitive personal or patient media unless privacy, retention, consent, and account-management terms are acceptable.

Risk: The skill may create or reuse a local identity and store authentication tokens or local state in the workspace.

Mitigation: Run the skill in an isolated workspace, restrict access to local state, and clear stored identity or token data after use on shared systems.

Risk: Historical report queries can retrieve prior cloud reports associated with the local identity.

Mitigation: Confirm the intended identity context before listing reports and share report links only with authorized recipients.

Risk: Respiratory symptom analysis could be mistaken for a medical diagnosis.

Mitigation: Present outputs as health-reference monitoring information and direct users to professional medical care for diagnosis, urgent symptoms, or treatment decisions.

## Reference(s):

- [Respiratory Symptom Recognition API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown report text with embedded structured JSON; optional JSON or file output for detailed results and report history.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analyzes local video files or public video URLs, can list cloud report history, and may include report export links.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

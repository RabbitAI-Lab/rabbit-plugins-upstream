## Description:

Identifies strangers appearing in surveillance areas through facial comparison; supports video stream and image detection, suitable for stranger warnings in residential communities, units, access control, and other scenarios. | 陌生人识别技能，通过人脸比对识别监控区域出现的陌生人员，支持视频流和图片检测，适用于小区、单位、门禁等场景的陌生人预警

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to submit surveillance images or video for stranger recognition, known-person matching, stranger alerts, and historical report lookup. Because it processes face data and cloud report history, use should be limited to environments where the publisher's biometric data handling is approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles surveillance media, face data, biometric enrollment, cloud report access, and automatic account/token persistence.

Mitigation: Install only after confirming authorization to upload this data, enroll people, and use the automatic account and report-history behavior.

Risk: Retention, deletion, access-control, and audit details are not established in the provided evidence.

Mitigation: Ask the publisher for these details before use with real people or regulated environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Packaged API reference](references/api_doc.md)
- [Shared API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON text with structured recognition results, report history tables, warnings, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save a report to a caller-provided output file; report history is retrieved from the provider's cloud API.]

## Skill Version(s):

1.0.11 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

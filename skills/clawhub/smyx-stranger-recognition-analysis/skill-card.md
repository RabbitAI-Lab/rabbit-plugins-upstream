## Description:

Identifies strangers appearing in surveillance areas through facial comparison; supports video stream and image detection, suitable for stranger warnings in residential communities, units, access control, and other scenarios. | 陌生人识别技能，通过人脸比对识别监控区域出现的陌生人员，支持视频流和图片检测，适用于小区、单位、门禁等场景的陌生人预警

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators, facilities teams, and agent users use this skill to compare faces in surveillance images or video against a known-person database, identify unknown people, enroll known faces when authorized, and retrieve cloud-stored stranger recognition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles biometric media and face recognition results through a cloud-based workflow.

Mitigation: Use only with clear authorization and consent, define retention and deletion controls, and review service endpoint governance before production use.

Risk: The skill can enroll people into a face database and retrieve cloud-linked report history.

Mitigation: Restrict enrollment and history access to authorized users, audit report access, and confirm that report history is scoped to the intended identity.

Risk: The security verdict is suspicious because local identity creation and token persistence have limited user control or scoping.

Mitigation: Review local account and token storage behavior, avoid exposing internal identity values, and require deployment-specific security approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted structured reports with optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can output stranger recognition results, enrollment results, historical report lists, report links, warnings, and execution guidance.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Identifies strangers appearing in surveillance areas through facial comparison; supports video stream and image detection, suitable for stranger warnings in residential communities, units, access control, and other scenarios. | 陌生人识别技能，通过人脸比对识别监控区域出现的陌生人员，支持视频流和图片检测，适用于小区、单位、门禁等场景的陌生人预警

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators, property managers, and developers use this skill to analyze surveillance images or video streams for face comparison, known-person identification, stranger detection, stranger alerts, and history/report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends surveillance images or videos and identity-linked report data to a configured cloud service.

Mitigation: Deploy only where media capture, cloud processing, retention, and deletion are authorized and documented.

Risk: The skill supports biometric enrollment, report history lookup, and report links tied to an internal identity.

Mitigation: Restrict enrollment and history access to approved operators, audit report access, and avoid using shared identities for regulated data.

Risk: Security evidence flags silent default-user creation and token storage with insufficient user control.

Mitigation: Review identity initialization and token storage before shared or regulated use, isolate workspaces, and remove stored credentials when no longer needed.

Risk: The server security verdict is suspicious for this release.

Mitigation: Require privacy and security review before deployment, especially for consent, authorization, retention, deletion, and biometric handling controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [smyx_analysis API interface documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON structured analysis reports, report links, history lists, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; analysis uses image or video input and can save output when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

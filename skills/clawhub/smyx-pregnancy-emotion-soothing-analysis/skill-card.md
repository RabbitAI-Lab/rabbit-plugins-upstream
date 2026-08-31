## Description:

This skill analyzes opted-in fixed-camera and optional microphone inputs for pregnancy-related emotion signals, produces structured reports, and can guide soothing actions such as low-volume audio, warm lighting, or user-approved contact notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-support developers use this skill to analyze consented pregnancy home or prenatal waiting-room audio-video, identify emotion-related behaviors, and produce structured reports or soothing-action guidance. It is intended for support workflows and must not be used to make medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive pregnancy-related home or clinic audio-video and may upload content for cloud analysis.

Mitigation: Use only where the pregnant person has explicitly opted in, camera or microphone capture is clearly posted, and cloud upload and retention terms are acceptable.

Risk: The skill may send spouse or emergency-contact notifications based on emotion-related detections.

Mitigation: Require user-selected notification recipients and revocable consent before enabling contact notifications.

Risk: Local identity token storage may be present on the machine running the skill.

Mitigation: Deploy only on machines where local token storage is acceptable, and review token cleanup or rotation procedures for shared environments.

Risk: Security evidence flags the release as suspicious because sensitive monitoring controls need careful review.

Mitigation: Perform a privacy and security review before installation, with special attention to consent, retention, notification routing, and local credentials.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, historical report tables, and recommended soothing actions.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

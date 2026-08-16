## Description:

Assesses ornamental fish color vibrancy from aquarium image or video inputs by extracting HSV saturation and brightness signals, comparing them with species-specific baselines, and producing a structured vibrancy report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquarium operators, and developers use this skill to analyze supported fish images, videos, or URLs for color vibrancy scoring, species-baseline comparison, trend reporting, and management-oriented recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish images, videos, or submitted URLs may be processed by the publisher's cloud service.

Mitigation: Use non-sensitive media and avoid private or internal URLs unless the publisher provides acceptable consent, retention, deletion, and data-use controls.

Risk: The skill may create or reuse backend accounts and store local tokens in the workspace with limited user control.

Mitigation: Review local account and token storage before installation, restrict workspace access, and remove stored credentials when the skill is no longer needed.

Risk: Color-vibrancy reports can be misleading when inputs lack white-reference calibration, have poor lighting, or do not show the fish side clearly.

Mitigation: Require the documented input controls, including a white or gray reference, adequate lighting, species subtype, and side-view imagery; treat unreliable signals as needing retake rather than diagnosis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [Skill API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Usage Introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include HSV measurements, species-baseline comparison, vibrancy score, trend fields, recommended actions, and a report link.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

This skill analyzes child camera, video, and optional audio inputs with multimodal emotion recognition to classify states such as happy, sad, angry, fearful, crying, and calm, and to return structured reports and soothing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, teachers, and developers use this skill to submit child video/audio files or media URLs for emotion classification, negative-emotion alerting, soothing hints, and historical report lookup. Results are assistive observations and are not a substitute for professional child psychology or medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child video, audio, child-media URLs, and generated reports are sent to and queried from a configured remote backend.

Mitigation: Use only with guardian consent, avoid unnecessary identifiers in media, and confirm the publisher's retention, deletion, encryption, and access-control practices before use.

Risk: The skill can create or reuse a local account identity and store tokens in a workspace SQLite database.

Mitigation: Run in an isolated workspace, restrict access to workspace data files, and remove local identity/token storage when the skill is no longer needed.

Risk: Historical report listing and export links can expose stored child emotion reports.

Mitigation: Verify the active account context before listing or exporting reports, and review report links before sharing them outside the authorized caregiving or teaching context.

Risk: Emotion classifications and soothing hints may be inaccurate or overinterpreted as clinical conclusions.

Mitigation: Treat outputs as assistive observations for adult review and seek qualified professional support for persistent distress, safety concerns, or suspected clinical issues.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown report text with JSON-structured analysis, status messages, soothing guidance, and report/export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis output to a user-specified local file and may return historical report lists from the configured remote service.]

## Skill Version(s):

1.0.23 (source: server release metadata; artifact frontmatter is 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

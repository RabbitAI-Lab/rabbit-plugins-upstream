## Description:

Identifies acquaintances in videos or images through face photo comparison, supports database enrollment, and returns recognition results with person and location context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare faces in uploaded images or videos against an enrolled face database, then receive structured acquaintance-recognition results for home security or office personnel-management scenarios. Results should not be used for legal identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes highly sensitive face media through remote services.

Mitigation: Use only with consent from people in the images or videos and document remote biometric processing and retention before deployment.

Risk: Recognition results could be mistaken for authoritative identity verification.

Mitigation: Treat results as advisory and do not use the skill for legal identity verification.

Risk: The default configuration includes plaintext HTTP endpoints.

Mitigation: Change the deployment configuration to HTTPS-only endpoints before use.

Risk: The skill silently manages identity, creates default accounts, and may store reusable tokens in a shared plaintext database.

Mitigation: Avoid silent account creation and shared plaintext token storage; require explicit identity governance and protected credential storage.

## Reference(s):

- [Familiar Person Recognition API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured recognition report text, Markdown tables for history lists, or JSON detail output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and optional file output when an output path is supplied.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

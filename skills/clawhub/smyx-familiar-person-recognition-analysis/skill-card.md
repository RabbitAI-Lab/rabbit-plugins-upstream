## Description:

Identifies acquaintances in videos or images through face photo comparison, supports database enrollment, and reports who appears at which location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare uploaded images or videos against an enrolled face database for home or office acquaintance recognition, structured reporting, and historical report lookup. Results should support operational review and should not be treated as legal identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, or media URLs are sent to a cloud service for biometric-style recognition.

Mitigation: Use the skill only with appropriate consent and data handling approval, and avoid submitting media that should not leave the local environment.

Risk: The skill silently creates or reuses a persistent local/backend identity and links report history to it.

Mitigation: Review the identity behavior before deployment and require clear user consent, reset, and deletion procedures from the publisher.

Risk: Authentication tokens may be stored in the workspace SQLite database.

Mitigation: Limit workspace access, rotate credentials after testing, and inspect or clear local identity/token storage before sharing the workspace.

Risk: Recognition output can be wrong or misused as authoritative identification.

Mitigation: Treat results as reference-only operational analysis and require human review before any access, employment, legal, or safety decision.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and structured JSON returned from cloud analysis APIs, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include recognition results, annotations, recommendations, historical report records, and report links.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

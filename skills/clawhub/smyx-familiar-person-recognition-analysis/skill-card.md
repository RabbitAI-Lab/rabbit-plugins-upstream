## Description:

Identifies acquaintances in videos or images through face photo comparison, supports face database enrollment, and reports recognized people and their locations in the media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home, office, and operations users can use this skill to compare faces in uploaded images or videos against a pre-enrolled acquaintance database for identity recognition and report review. It is suitable for identity-checking workflows where results are reviewed as advisory analysis rather than treated as legal identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send biometric images, videos, URLs, identity values, and report-history requests to remote services.

Mitigation: Install and run it only when the publisher and backend endpoints are trusted and users are comfortable with remote processing of biometric media and recognition history.

Risk: The skill may silently create or reuse a backend account and persist tokens in the workspace data directory.

Mitigation: Review account-handling behavior and token storage before deployment, and restrict workspace access according to the sensitivity of the recognition data.

Risk: Face-recognition output can be incorrect or incomplete and is not suitable as a sole basis for legal identity verification.

Mitigation: Require human review for consequential decisions and present recognition results as advisory analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON report text with recognized-person results, report links, and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured analysis content, recognized identities and locations, risk notes, suggestions, and cloud report links.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

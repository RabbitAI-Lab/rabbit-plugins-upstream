## Description:

Identifies acquaintances in videos or images through face photo comparison, supports database enrollment, and returns recognition results indicating who appears at which location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze uploaded images, videos, local files, or media URLs for known-person recognition after faces have been enrolled in a personal face database. It is intended for home security monitoring and office-area personnel verification, with results treated as reference information rather than legal identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends face images, videos, media URLs, identity-linked request metadata, and report-history queries to remote Life Emergence/SMYX services.

Mitigation: Use only with appropriate consent and confirm data handling, retention, and deletion practices before processing biometric media.

Risk: The skill silently creates or reuses an account identity and stores tokens locally.

Mitigation: Confirm which account identity is used, where tokens are stored, and how local identity state is protected before deployment.

Risk: Recognition output is reference information and may be unsuitable for legal identity verification.

Mitigation: Require human review and a separate approved identity-verification process for high-stakes or legal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis results with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-hosted report history and may save returned analysis content to a user-specified output path.]

## Skill Version(s):

1.0.14 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

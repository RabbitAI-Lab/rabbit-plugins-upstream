## Description:

Identifies cat and dog breeds and distinguishes individual pets in multi-pet households from images, videos, or media URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to submit pet images, videos, or media URLs for breed identification, individual pet distinction, and retrieval of prior pet recognition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media is processed by a cloud service.

Mitigation: Use the skill only when users are comfortable sending pet images, videos, or URLs to the cloud service for analysis.

Risk: The skill can query account-linked report history and automatically reuse or create an identity.

Mitigation: Prefer a release that asks before history lookup or registration and clearly declares the identity and history permissions it uses.

Risk: Tokens and identity data may persist in the workspace data directory.

Mitigation: Run the skill in an isolated workspace and limit retained identity data before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON text with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pet counts, breed assessments, individual pet distinctions, confidence values, remarks, report links, and history lists.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Detects whether anyone has fallen within a specified target area and supports both image and short video analysis for home care and nursing-home safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, safety monitors, and developers use this skill to analyze uploaded images, short videos, or media URLs for possible fall events and to retrieve structured fall-detection reports. Results are for safety reference and should be confirmed by a person before emergency or care decisions are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Care-related images or videos and generated identifiers may be sent to remote services.

Mitigation: Confirm documented HTTPS production endpoints, obtain appropriate user consent, and review retention and deletion terms before normal use.

Risk: The skill may silently create or reuse an account, store authentication tokens in local SQLite storage, and query cloud history.

Mitigation: Review identity handling, token storage, access controls, and user disclosure before installation or deployment.

Risk: Server evidence reports private HTTP development endpoint configuration.

Mitigation: Replace development endpoints with documented production HTTPS endpoints and verify configuration before execution.

## Reference(s):

- [Fall Detection API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected fall status, monitoring results, risk prompts, suggestions, historical report rows, and report links.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

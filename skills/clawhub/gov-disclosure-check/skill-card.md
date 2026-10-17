## Description:

Checks government disclosure text for mentions of a decision basis, responsible department, deadline, remedy channel, and data source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and public-sector content reviewers use this skill to identify missing disclosure-field mentions in draft documents or records before human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A keyword check may be mistaken for legally validated disclosure compliance.

Mitigation: Treat results as a preliminary completeness check and have a qualified reviewer assess legal requirements before publication.

Risk: Broad tool permissions could expose documents or enable unnecessary changes.

Mitigation: Run locally with only the needed file access; decline network, WebFetch, Write, or broad filesystem access unless separately justified.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/gov-disclosure-check)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON with missing fields and a completeness result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-first CLI output; returns 0 when all field mentions are found, 1 when some are missing, and 2 for usage errors.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

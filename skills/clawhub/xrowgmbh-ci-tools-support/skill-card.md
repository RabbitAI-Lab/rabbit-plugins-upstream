## Description:

Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI Tools maintainers use the skill to triage support requests in GitLab, provide answers grounded in public documentation, protect private details, and identify when a maintainer should help.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow says to unlock an already locked discussion without first checking why it was locked.

Mitigation: Require maintainer approval and confirm the reason for the lock before changing it.

Risk: The component references needed to support answers were unavailable for review.

Mitigation: Obtain and review the referenced component documentation before relying on answers; restrict GitLab access to the intended project.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with descriptive links and, when useful, numbered checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should be grounded in public references, avoid repeating private details, and may ask one focused follow-up question.]

## Skill Version(s):

4.230.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

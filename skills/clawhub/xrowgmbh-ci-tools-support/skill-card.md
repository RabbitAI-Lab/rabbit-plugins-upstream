## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support maintainers and agents use this skill to triage eligible GitLab support requests and answer CI Tools catalog questions using public sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support responses could be sent to unapproved requesters or outside the CI Tools scope.

Mitigation: Confirm the requester domain against SUPPORT_TRUSTED_DOMAINS and limit replies and labels to eligible GitLab support requests.

Risk: Customer details or private logs could be disclosed in public threads.

Mitigation: Mark requests with sensitive details confidential, use public sources for answers, and hand off private customer-system cases to a maintainer.

## Reference(s):

- [ci-tools-support on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support replies and triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public-source citations, focused follow-up questions, and scoped label or confidentiality guidance.]

## Skill Version(s):

4.205.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

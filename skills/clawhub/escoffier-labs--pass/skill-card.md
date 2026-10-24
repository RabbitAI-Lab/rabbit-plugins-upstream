## Description:

A pull-request readiness skill that helps teams review changes and checks before filing or updating a PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[escoffier-labs](https://clawhub.ai/user/escoffier-labs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to check PR readiness, surface failed checks for resolution, and prepare a change for review. It requires author approval before creating a PR or pushing follow-up commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checklist guidance may be misleading if applied without checking the actual change.

Mitigation: Review recommendations against the diff and rerun relevant tests and lint checks before accepting them.

Risk: Referenced helper skills and the lint script may not be present in the workspace.

Mitigation: Check availability and perform an equivalent manual check rather than silently skipping a required gate.

Risk: A PR could be opened or updated before the author has approved the proposed description or follow-up.

Mitigation: Obtain the author's approval before creating a PR or pushing follow-up commits.

## Reference(s):

- [pass on ClawHub](https://clawhub.ai/escoffier-labs/skills/pass)
- [Publisher profile: escoffier-labs](https://clawhub.ai/user/escoffier-labs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [PR-readiness checklist and review guidance, with shell commands where relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires author approval before PR publication or follow-up pushes.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

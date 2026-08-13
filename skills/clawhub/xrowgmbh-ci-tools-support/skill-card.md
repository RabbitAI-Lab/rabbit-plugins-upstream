## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage GitLab support issues and discussion threads for CI Tools components, answer from public sources or explicit thread context, and hand off unsupported or unsafe requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support may be provided to an unapproved requester if the trusted-domain check is skipped.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS before use and verify the requester domain before drafting or posting support guidance.

Risk: Private customer details, private URLs, private logs, or internal project names could be exposed in a public reply.

Mitigation: Treat issues with private details as confidential and route private customer details or credential/access issues to a human maintainer.

Risk: Unsupported or invented CI component behavior could mislead users.

Mitigation: Ground answers in public documentation, public repository content, public GitLab history, or explicit thread context, and inspect the component template before describing inputs or behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support replies, focused follow-up questions, handoff or refusal text, and triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should cite public documentation, repository paths, issues, merge requests, or pipeline logs used as support.]

## Skill Version(s):

4.171.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog, answer from public documentation or provided context, and hand off requests that are private, unsafe, or outside scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent using this support skill could reply to or label GitLab issues with broader permissions than needed.

Mitigation: Grant only the GitLab permissions required for support replies and labels before installation.

Risk: Eligibility checks depend on the configured approved requester domains.

Mitigation: Set SUPPORT_TRUSTED_DOMAINS to the intended approved domains and verify it before use.

Risk: Support answers may expose private customer details if public and confidential contexts are mixed.

Mitigation: Keep issues confidential when they include customer details, private URLs, private logs, or internal project names, and ground public replies only in approved public or thread-provided information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown support replies, triage notes, labels, handoff messages, and focused follow-up questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses must be grounded in public CI Tools documentation, public repository content, public GitLab history, or details explicitly provided in the support thread.]

## Skill Version(s):

4.183.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

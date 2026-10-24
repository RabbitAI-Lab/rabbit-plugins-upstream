## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to triage eligible GitLab support issues and answer questions about CI Tools components using public information. It directs requests involving private systems, sensitive details, or unsupported topics to a human maintainer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support requests may include customer details, private URLs, logs, or internal project names.

Mitigation: Verify the approved requester domain, treat requests containing private details as confidential, and hand off requests that are outside the documented public-support scope.

Risk: Replies or label changes could be applied beyond the intended support projects.

Mitigation: Limit GitLab permissions to the intended support projects and configure SUPPORT_TRUSTED_DOMAINS.

## Reference(s):

- [CI Tools Support on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Concise GitLab issue or discussion replies, follow-up questions, and handoff or refusal guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite supporting public sources and avoid exposing private logs or customer details.]

## Skill Version(s):

4.225.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

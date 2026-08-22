## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support engineers and maintainers use this skill to triage GitLab support issues and discussion threads for the xrow-public/ci-tools catalog, answer eligible requests from public or provided context, and hand off unsafe or out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overly broad SUPPORT_TRUSTED_DOMAINS value could route support to requester domains that are not actually trusted.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS with only the domains trusted for CI Tools support before installing or enabling the skill.

Risk: Support threads can include customer details, private URLs, internal project names, or private logs.

Mitigation: Use confidential handling when private details are present and do not quote private logs into public places.

Risk: Requests about credentials, access recovery, harmful activity, private customer systems, or unrelated products could fall outside the skill's safe support scope.

Mitigation: Hand off to a human maintainer or refuse technical support when the request is outside scope, unsafe, or not grounded in public information or the thread context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support response or triage note]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public documentation, repository paths, issues, merge requests, or pipeline logs used for the answer.]

## Skill Version(s):

4.175.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

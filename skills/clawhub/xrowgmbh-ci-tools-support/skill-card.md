## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

External support maintainers and agents use this skill to triage GitLab support issues and discussions for the xrow-public/ci-tools components catalog, answer eligible requests from public information, and hand off unsafe or out-of-scope cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support could be provided to an ineligible requester if SUPPORT_TRUSTED_DOMAINS is misconfigured.

Mitigation: Maintain SUPPORT_TRUSTED_DOMAINS carefully and confirm the requester domain before giving technical support.

Risk: Private customer details, private URLs, private logs, or internal project names could be exposed in public replies.

Mitigation: Keep private details out of public replies, mark issues confidential when needed, and hand off cases involving private systems, credentials, access recovery, or unrelated products.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown support replies with citations to public documentation, repository paths, issues, merge requests, or pipeline logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should stay within CI Tools support scope, avoid public disclosure of private customer details, and ask one focused follow-up question when reproduction details are missing.]

## Skill Version(s):

4.169.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

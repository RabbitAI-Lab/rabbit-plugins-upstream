## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage GitLab support issues or discussions for the CI Tools components catalog, answer from public evidence, and hand off unsafe or out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support replies could expose private customer details, private URLs, private logs, or internal project names in public threads.

Mitigation: Check confidentiality before replying, avoid quoting private logs publicly, and hand off private customer systems or unclear cases to a human maintainer.

Risk: A broad or incorrect SUPPORT_TRUSTED_DOMAINS value could allow support responses for requesters outside the intended audience.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS narrowly and verify the requester domain before providing technical support.

Risk: The agent could provide inaccurate CI Tools behavior if it answers without inspecting public documentation, repository content, or provided thread details.

Mitigation: Ground each answer in public documentation, public repository content, public GitLab history, or explicit request context, and ask for one focused reproduction detail when evidence is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown support replies, follow-up questions, labels, refusals, or maintainer handoffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a carefully scoped SUPPORT_TRUSTED_DOMAINS value for requester eligibility checks.]

## Skill Version(s):

4.199.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

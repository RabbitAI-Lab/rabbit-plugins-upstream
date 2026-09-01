## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage GitLab support issues and discussion threads for the CI Tools components catalog, answer from public evidence, request reproducible details, or hand off unsafe or out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could provide support to an untrusted requester or for an unrelated issue.

Mitigation: Confirm the requester domain against SUPPORT_TRUSTED_DOMAINS, verify the issue is related to CI Tools, and hand off when eligibility checks fail.

Risk: Private customer details, private URLs, or logs could be exposed in a public reply.

Mitigation: Mark issues confidential when sensitive details are present and avoid quoting private logs into public places.

Risk: The agent could provide incorrect CI component behavior or invented inputs.

Mitigation: Answer only from public documentation, public repositories, public GitLab history, or request-provided context, and inspect the component template before describing inputs or behavior.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support replies, follow-up questions, handoff notes, and refusal guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public documentation, repository paths, issues, merge requests, or pipeline logs used as support evidence.]

## Skill Version(s):

4.184.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog using public documentation, public repository content, and details provided in the request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be used to answer support requests from unapproved requester domains.

Mitigation: Confirm SUPPORT_TRUSTED_DOMAINS is set correctly and verify the requester domain before providing technical support.

Risk: Private customer details, private URLs, private logs, or internal project names could be exposed in public replies.

Mitigation: Mark issues confidential when they contain sensitive details and avoid quoting private logs into public places.

Risk: The agent could give unsupported or incorrect CI Tools component guidance.

Mitigation: Answer only from public documentation, public repository content, public GitLab history, or details explicitly provided in the thread, and inspect component templates before describing inputs or behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown support replies, triage notes, handoff or refusal text, and cited follow-up questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public sources, avoid quoting private logs into public places, and hand off requests outside the approved support scope.]

## Skill Version(s):

4.182.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

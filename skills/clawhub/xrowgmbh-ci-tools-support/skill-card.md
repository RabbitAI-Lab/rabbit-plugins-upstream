## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog. It guides them to answer from public documentation, public repository history, public pipeline logs, or details explicitly provided in the request, and to hand off unsafe or out-of-scope cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be used in workflows where the agent can post replies or apply labels.

Mitigation: Confirm the approved domain list is accurate and grant only the GitLab permissions needed for support triage.

Risk: Support requests may include customer details, private URLs, private logs, or internal project names.

Mitigation: Keep those issues confidential, avoid quoting private logs into public places, and hand off requests that cannot be answered from public or explicitly provided information.

Risk: Incorrect support guidance could be given if component inputs or behavior are assumed.

Mitigation: Cite the public documentation, repository path, issue, merge request, or pipeline log used for the answer, and inspect the component template before describing behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support replies, follow-up questions, handoff notes, or refusal guidance with cited public sources when support is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to apply labels or preserve confidentiality when support requests include customer details, private URLs, private logs, or internal project names.]

## Skill Version(s):

4.172.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support engineers and maintainers use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog, answer from public sources or supplied thread context, and hand off unsafe or out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect trusted-domain configuration could allow support responses for ineligible requesters.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS before installation and verify requester eligibility before replying.

Risk: Broad GitLab permissions could let an agent comment or label beyond the support triage scope.

Mitigation: Grant only the GitLab permissions needed for support triage, especially if the agent can comment on issues or apply labels.

Risk: Private customer details, private URLs, logs, or internal project names could be exposed in public responses.

Mitigation: Mark issues confidential when they contain private details and avoid quoting private logs into public places.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support replies and concise triage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite public documentation, repository paths, issues, merge requests, or pipeline logs used to support an answer.]

## Skill Version(s):

4.192.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

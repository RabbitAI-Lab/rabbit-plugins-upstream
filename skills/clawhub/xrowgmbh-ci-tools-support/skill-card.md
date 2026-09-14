## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support engineers use this skill to triage GitLab support issues and discussion threads for the CI Tools components catalog, answer from public sources or provided context, and route unsafe or out-of-scope requests to a maintainer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may provide support to an unapproved requester or outside the CI Tools support workflow.

Mitigation: Install it only for CI Tools GitLab support agents and require SUPPORT_TRUSTED_DOMAINS to contain the approved requester domains.

Risk: A support reply could disclose or rely on private customer logs, private URLs, credentials, or internal project details.

Mitigation: Keep answers limited to public documentation, public repository history, public logs, and details explicitly provided in the thread; hand off requests involving private systems or credentials.

Risk: The agent could invent component inputs or behavior when public evidence is incomplete.

Mitigation: Require answers to cite the public documentation page, repository path, issue, merge request, or pipeline log used, and ask one focused follow-up question when a reproducible example is missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [xrowgmbh Publisher Profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown support replies, handoff notes, refusals, follow-up questions, and cited troubleshooting guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public documentation, repository paths, issues, merge requests, or pipeline logs used for support answers.]

## Skill Version(s):

4.191.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

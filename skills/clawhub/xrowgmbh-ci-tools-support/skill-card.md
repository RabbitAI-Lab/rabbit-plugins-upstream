## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents and maintainers use this skill to triage eligible GitLab issues and discussions about CI Tools components, answer from public information, and hand off requests outside its scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An outdated approved-domain list could cause support to be given to an ineligible requester.

Mitigation: Maintain SUPPORT_TRUSTED_DOMAINS and verify the requester domain before answering.

Risk: Customer details or private logs could be disclosed in a public reply.

Mitigation: Check confidentiality before replying, avoid quoting private logs publicly, and hand off private-system requests to a maintainer.

Risk: Issue replies or label changes could exceed the intended support-triage scope.

Mitigation: Limit the GitLab account to the permissions needed for support triage and review replies and labels before applying them.

## Reference(s):

- [CI Tools Support skill on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [GitLab thread replies and triage guidance in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers cite public sources; ineligible requests receive a brief handoff or refusal and appropriate label guidance.]

## Skill Version(s):

4.217.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

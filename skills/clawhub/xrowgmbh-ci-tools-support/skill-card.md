## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support maintainers use this skill to triage eligible CI Tools GitLab support requests and reply with answers grounded in public documentation, repository content, or thread context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support could be given to an unapproved requester or for an out-of-scope issue.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS correctly and verify requester eligibility and CI Tools relevance before responding.

Risk: Customer details or private logs could be exposed in a public reply.

Mitigation: Mark issues containing private details confidential, avoid quoting private logs publicly, and hand off sensitive cases to a maintainer.

Risk: Excess GitLab permissions could allow unintended replies or label changes.

Mitigation: Give the agent account only the GitLab permissions needed for support replies and label changes.

## Reference(s):

- [CI Tools Support skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown guidance]

**Output Format:** [Markdown support replies and triage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites public sources and may request reproduction details or recommend handoff.]

## Skill Version(s):

4.218.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

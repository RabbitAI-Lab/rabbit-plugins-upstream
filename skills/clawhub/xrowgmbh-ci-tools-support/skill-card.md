## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog. It guides responses that rely on public documentation, public repositories, public GitLab history, or context explicitly provided in the request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support may be given to an ineligible requester or for an out-of-scope issue.

Mitigation: Verify the requester domain with SUPPORT_TRUSTED_DOMAINS, confirm the issue is related to CI Tools, and hand off anything outside the public CI Tools catalog.

Risk: Public replies may expose private logs, customer details, private URLs, or internal project names.

Mitigation: Mark issues confidential when sensitive details appear and do not quote private logs into public replies.

Risk: Incorrect component guidance may be provided if behavior or inputs are assumed.

Mitigation: Inspect the relevant public component template or documentation, cite the source used, and ask one focused follow-up question when a reproducible example is missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain-text support replies with source citations and triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public sources, avoid quoting private logs into public places, and hand off out-of-scope or unsafe requests.]

## Skill Version(s):

4.185.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

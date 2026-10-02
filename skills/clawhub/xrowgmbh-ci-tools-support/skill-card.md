## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents and maintainers use this skill to triage eligible CI Tools GitLab support requests and answer from public documentation, repositories, and issue context. Requests outside its scope are handed off to a human maintainer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support responses could disclose private customer details or internal URLs in a public issue.

Mitigation: Confirm issue confidentiality, avoid quoting private logs publicly, and review public replies before posting.

Risk: Support could be offered to an unapproved requester or an out-of-scope issue.

Mitigation: Check the requester domain against SUPPORT_TRUSTED_DOMAINS and confirm the issue is about CI Tools; otherwise hand off or refuse and review any label change.

## Reference(s):

- [CI Tools Support skill on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support replies and triage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include public-source citations, a focused follow-up question, or a handoff and label recommendation.]

## Skill Version(s):

4.213.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents and maintainers use this skill to triage GitLab support issues for the CI Tools components catalog and draft responses grounded in public documentation, public repository content, GitLab history, or details provided in the request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support responses could expose customer details, private URLs, private logs, or internal project names if confidentiality is not checked first.

Mitigation: Confirm the request confidentiality state before replying, avoid quoting private logs in public places, and hand off private customer or internal-system requests to a human maintainer.

Risk: Support could be provided to requesters outside the intended trusted-domain workflow.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS correctly and verify the requester domain before answering or labeling an issue.

Risk: The agent could give inaccurate CI component guidance if it relies on assumptions instead of source material.

Mitigation: Inspect the relevant public component template, documentation, repository history, issue, merge request, or pipeline log before answering, and cite the evidence used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support replies, triage notes, and handoff or refusal guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public evidence and stay within the intended CI Tools support workflow.]

## Skill Version(s):

4.176.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support maintainers and developers use this skill to triage eligible GitLab support issues for the CI Tools components catalog and answer from public documentation, public repository content, public GitLab history, or details provided in the thread.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Support could be provided to an untrusted requester if the approved-domain list is misconfigured.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS before use and verify requester eligibility before responding.

Risk: Private customer details, private URLs, or private logs could be exposed in a public support thread.

Mitigation: Treat issues containing private details as confidential and avoid quoting private logs into public places.

Risk: Incorrect CI Tools component guidance could be posted if behavior or inputs are assumed.

Mitigation: Inspect the relevant public component template and cite the documentation, repository path, issue, merge request, or pipeline log used for the answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown support replies and concise triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite public documentation, repository paths, issues, merge requests, or pipeline logs; gated by SUPPORT_TRUSTED_DOMAINS.]

## Skill Version(s):

4.174.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

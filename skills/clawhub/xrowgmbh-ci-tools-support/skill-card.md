## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support maintainers use this skill to triage eligible GitLab support issues and compose grounded replies for the CI Tools components catalog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could respond to ineligible support requests or expose private support details if requester-domain and confidentiality checks are skipped.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS correctly, verify confidentiality before replying, and hand off requests involving private systems, credentials, or unsafe activity.

Risk: Support replies could be misleading if component behavior is answered from memory rather than checked against public evidence.

Mitigation: Inspect the relevant component template or public documentation first and cite the public documentation page, repository path, issue, merge request, or pipeline log used for the answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown support replies and triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should cite public documentation, repository paths, issues, merge requests, or pipeline logs used as evidence.]

## Skill Version(s):

4.201.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support agents use this skill to triage eligible GitLab support issues and discussion threads for the CI Tools components catalog, answer from public sources, request focused reproduction details, or hand off out-of-scope requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may provide support to requesters outside the approved support population if trusted email domains are configured too broadly.

Mitigation: Configure SUPPORT_TRUSTED_DOMAINS carefully and verify requester domain eligibility before answering.

Risk: The skill may expose or amplify private customer details if confidential issues, private URLs, or private logs are handled in public replies.

Mitigation: Keep issues confidential when customer details or private artifacts are present, do not quote private logs publicly, and hand off cases that require private system context.

Risk: The skill may give incorrect CI component guidance if it answers from assumptions rather than source material.

Mitigation: Cite public documentation, repository paths, issues, merge requests, or pipeline logs, and inspect component templates before describing component inputs or behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown support replies, triage notes, labels, and handoff or refusal guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPPORT_TRUSTED_DOMAINS configuration for requester eligibility checks.]

## Skill Version(s):

4.197.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

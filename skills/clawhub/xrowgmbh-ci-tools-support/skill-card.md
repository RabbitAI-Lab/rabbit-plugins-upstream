## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams use this skill to triage eligible CI Tools GitLab support requests and answer questions using public documentation and repository information. It guides handoffs when a request is outside scope or cannot be answered safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could reply to an unapproved requester or act outside the intended support project.

Mitigation: Configure approved requester domains and limit GitLab permissions to the relevant support project.

Risk: Customer details or private logs could be exposed in public replies.

Mitigation: Check issue confidentiality before replying and keep private details out of public threads.

## Reference(s):

- [CI Tools Support skill on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [GitLab discussion replies and support-triage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cite public sources, ask for reproduction details, or recommend handoff and labeling.]

## Skill Version(s):

4.203.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

CI Tools maintainers and users can use this skill to triage support requests and provide actionable answers grounded in public component documentation, repository history, and sanitized request details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags the skill as suspicious because its workflow can reopen locked discussions without checking why they were locked or getting maintainer approval.

Mitigation: Review the moderation workflow before installation; verify the reason for any lock and obtain maintainer approval before reopening a discussion.

Risk: The security scan is incomplete because it could not resolve a local path-like reference.

Mitigation: Review the unresolved reference and scan coverage before relying on the security assessment.

## Reference(s):

- [CI Tools Support skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support replies with explanations, checks, and references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Links to public documentation and safe next steps; asks one focused question when context is missing.]

## Skill Version(s):

4.242.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

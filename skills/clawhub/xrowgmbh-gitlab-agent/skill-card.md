## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this agent to discover and complete assigned GitLab work, make code or configuration changes, and prepare merge requests for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security report flags possible GitLab actions beyond the stated assigned-work scope, including changes to projects that fail an access check.

Mitigation: Verify project access and authorization before enabling write actions, and review proposed changes before they are sent.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [GitLab changes, Code, Configuration, Shell commands, Markdown]

**Output Format:** [GitLab updates, code or configuration changes, shell commands, and Markdown status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May make remote GitLab changes while processing assigned work.]

## Skill Version(s):

1.147.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

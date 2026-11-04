## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to discover assigned GitLab work, follow project access and assignment gates, and deliver or review issues and merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags that the skill may change GitLab projects after access checks fail.

Mitigation: Review before enabling the recurring job, use a dedicated account limited to approved projects, and keep denied discovery read-only.

Risk: The security review flags that work could be accepted from unintended collaborators.

Mitigation: Resolve collaborators without ambiguous username or group matches, and explicitly decide whether automatic assignment and self-merging are permitted.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Agent source project](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [GitLab work items and merge requests, shell commands, code, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitLab work items, merge requests, labels, and related project artifacts.]

## Skill Version(s):

1.128.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

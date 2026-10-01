## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to work on assigned GitLab issues and merge requests, check project access, and deliver changes for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Standing permission allows the agent to push changes and modify GitLab workflows without per-action confirmation.

Mitigation: Use a dedicated automation account with tightly scoped project access and protected branches; retain clear owner control.

Risk: A personal or broadly privileged token could extend autonomous changes beyond the intended projects.

Mitigation: Avoid personal or broadly privileged tokens; restrict the token and review project memberships and assignments before use.

## Reference(s):

- [GitLab Agent release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [Documentation style](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Markdown]

**Output Format:** [Markdown, code changes, and GitLab work items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update issues, labels, merge requests, branches, and CI pipelines.]

## Skill Version(s):

1.95.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Operates assigned GitLab work with owner-verified project access and guarded merge request delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to process assigned GitLab issues and merge requests, maintain branches and forks, and deliver changes through review and pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GitLab write access can affect issues, branches, merge requests, labels, reviewers, pipelines, forks, and potentially variables or releases.

Mitigation: Use a tightly scoped GitLab account and token restricted to the intended projects; remove unneeded variable, release, fork, and collaborator actions.

Risk: Recurring autonomous execution may make changes without a separate approval step.

Mitigation: Review the bootstrap and schedule, run the agent manually first, and enable recurring work only after confirming its scope.

Risk: Instructions that skip CI or maintain forks may bypass expected checks or alter upstream-related work.

Mitigation: Remove or narrow CI-skip and fork-maintenance instructions unless explicitly needed; review resulting changes before merging.

## Reference(s):

- [GitLab Agent release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab permissions and roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [Documentation style](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [GitLab issues, comments, merge requests, repository changes, and agent status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update GitLab projects and run on a recurring schedule when enabled.]

## Skill Version(s):

1.105.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

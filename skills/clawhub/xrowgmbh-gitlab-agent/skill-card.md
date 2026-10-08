## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to triage assigned GitLab work, update code and issues, and deliver merge requests with project-access checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring automation can change repositories, issues, merge requests, forks, and CI with limited human oversight.

Mitigation: Use a dedicated GitLab bot with least-privilege tokens and access limited to approved projects; review the recurring schedule before enabling unattended runs.

Risk: External upstream contributions and fork maintenance can modify repositories outside the usual project workflow.

Mitigation: Review permitted external upstream projects and fork-maintenance rules before enabling the skill.

Risk: Commit pushes may skip CI before a later pipeline is started.

Mitigation: Review CI-skip behavior and require successful pipeline results before merging.

Risk: Reviewer assignment and collaboration settings can allow changes to proceed without appropriate human review.

Mitigation: Review collaborator and reviewer settings and require human approval for sensitive changes.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [Documentation style reference](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [GitLab issue and merge request updates, code changes, and command or configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update repository branches, forks, issues, merge requests, and CI pipelines.]

## Skill Version(s):

1.106.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

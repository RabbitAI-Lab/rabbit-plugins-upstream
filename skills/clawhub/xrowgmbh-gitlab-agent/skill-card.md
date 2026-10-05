## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to discover and complete assigned GitLab issues and merge requests, including code changes, reviews, and pipeline follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GitLab write access can change code, merge requests, labels, reviewers, pipelines, and forks without per-action approval.

Mitigation: Use a dedicated, least-privileged GitLab automation account and restrict access to projects where these autonomous actions are acceptable.

Risk: A recurring job can continue making changes without a new prompt.

Mitigation: Leave recurring operation disabled unless autonomous work is explicitly intended; review granted token scope before enabling it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab project roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab Agent skill project](https://gitlab.com/xrow-public/skills)
- [Documentation style reference](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown and code or shell commands for GitLab tasks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also create or update GitLab issues, merge requests, comments, labels, and pipelines.]

## Skill Version(s):

1.98.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

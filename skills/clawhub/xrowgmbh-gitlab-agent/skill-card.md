## Description:

Operates assigned GitLab work with owner-verified project access and guarded merge request delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to process assigned GitLab issues and merge requests, deliver code changes, and coordinate reviews and CI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended GitLab writes can alter projects, issues, merge requests, and CI workflows.

Mitigation: Use a dedicated automation account with narrowly scoped project access; review the recurring job and permitted actions before enabling it.

Risk: External upstream contributions, fork maintenance, and pipeline controls may extend the impact of unattended runs.

Mitigation: Review upstream contribution rules, fork maintenance, and the ci.skip workflow before granting access.

Risk: Access to CI variables or releases could affect sensitive configuration and published artifacts.

Mitigation: Review and restrict permissions to manage CI variables and releases before installation.

## Reference(s):

- [GitLab Agent release on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab project roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [Documentation style guide](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Markdown, Shell commands]

**Output Format:** [Text and Markdown, including code changes and GitLab issue or merge request content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update GitLab issues, merge requests, branches, and workflow labels.]

## Skill Version(s):

1.96.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

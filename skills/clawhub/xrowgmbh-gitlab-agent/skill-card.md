## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to operate assigned GitLab issues and merge requests, enforce owner/project access checks, and deliver changes through guarded merge-request workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can repeatedly make broad GitLab changes without asking, including some admin-like actions beyond assigned work.

Mitigation: Review before installing and use only a dedicated low-privilege GitLab bot account limited to intended projects.

Risk: The skill depends on GitLab token authority and may perform no-confirmation automation across issues, merge requests, pipelines, forks, variables, and releases.

Mitigation: Avoid broad token scopes and do not enable recurring operation until no-confirmation behavior, fork maintenance, ci.skip usage, merge/release/variable authority, and project scoping are acceptable.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [CI Tools Label Component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and GitLab CLI/API workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, and GITLAB_TOKEN.]

## Skill Version(s):

1.81.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

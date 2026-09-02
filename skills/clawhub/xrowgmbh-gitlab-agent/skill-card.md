## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent work assigned GitLab issues and merge requests, create branches and merge requests, manage workflow labels, and respond to CI and review feedback under owner and assignment gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad autonomous GitLab write actions with developer-level access.

Mitigation: Use a narrowly scoped GitLab token, restrict allowed projects, and install only where autonomous issue and merge request work is intended.

Risk: Recurring execution and default ci.skip behavior can conflict with project governance.

Mitigation: Enable recurring jobs only after a manual run succeeds and review project policy before allowing ci.skip.

Risk: Variable and release operations can affect project behavior or distribution.

Mitigation: Remove or tightly control variable and release operations before deployment unless they are explicitly required.

## Reference(s):

- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [Label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [Skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, GitLab CLI commands, status comments, merge request descriptions, code changes, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and jq, plus a GitLab token supplied through GITLAB_TOKEN.]

## Skill Version(s):

1.84.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

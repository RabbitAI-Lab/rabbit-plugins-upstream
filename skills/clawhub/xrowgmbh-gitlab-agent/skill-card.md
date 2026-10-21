## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to work on assigned GitLab issues, incidents, and merge requests, including preparing code changes and merge-request delivery. It uses project-access and assignment checks to scope that work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine discovery can modify projects that fail owner authorization and accept work from unintended collaborators.

Mitigation: Make denied projects read-only, resolve collaborators to exact group identities, and restrict project and fork scope. Use a dedicated least-privilege account and require explicit approval for vulnerability exceptions.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles documentation](https://docs.gitlab.com/user/permissions/#default-roles)
- [Documentation style](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, API Calls]

**Output Format:** [Markdown, shell commands, code changes, and GitLab issue or merge-request updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitLab work items, labels, comments, branches, and merge requests.]

## Skill Version(s):

1.115.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

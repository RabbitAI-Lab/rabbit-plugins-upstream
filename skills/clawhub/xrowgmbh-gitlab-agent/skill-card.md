## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review assigned GitLab issues, tasks, incidents, and merge requests, and to prepare guarded updates or merge-request work. It checks project access and workflow conditions before acting, with human review retained where required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic GitLab changes may exceed the intended scope of owner-approved, assigned work.

Mitigation: Before recurring runs, request fixes for denied-project writes and ambiguous collaborator matching; restrict the account to intended projects, explicitly scope incident and fork automation, and retain human reviews for merges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab public skills repository](https://gitlab.com/xrow-public/skills)
- [GitLab default role permissions](https://docs.gitlab.com/user/permissions/#default-roles)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline code blocks and GitLab updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed changes to GitLab issues, tasks, incidents, and merge requests; execution is subject to project access and review controls.]

## Skill Version(s):

1.114.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

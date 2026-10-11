## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to discover assigned GitLab work, implement changes, and manage issues, incidents, merge requests, reviews, and pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous runs can make GitLab changes without asking for confirmation.

Mitigation: Use a tightly scoped, write-capable GitLab account and restrict its project membership.

Risk: A recurring job can repeatedly mutate labels, assign incidents, create merge requests, push branches, and manage reviewers or pipelines.

Mitigation: Review the recurring job before enabling it and confirm a manual run succeeds first.

## Reference(s):

- [GitLab Agent ClawHub release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab project permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [Documentation style guidance](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [GitLab issues, comments, merge requests, commits, and workflow updates; Markdown and code changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update labels, assign incidents, push branches, and manage reviewers and pipelines.]

## Skill Version(s):

1.110.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

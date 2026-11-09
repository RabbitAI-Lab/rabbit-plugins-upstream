## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to process assigned GitLab issues and merge requests, prepare code changes, and deliver work under project membership and assignment gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied security assessment rates the skill suspicious with medium confidence over the breadth of its GitLab actions; its analysis is also marked partial.

Mitigation: Review the reported actions and access gates before enabling the skill, and limit its GitLab token to the projects and permissions needed for the assigned work.

## Reference(s):

- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)
- [Maintained GitLab Agent skill source](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)
- [ClawHub GitLab Agent release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, GitLab issue and merge request updates]

**Output Format:** [Task-dependent text, code changes, and GitLab updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies with the assigned GitLab task.]

## Skill Version(s):

1.134.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

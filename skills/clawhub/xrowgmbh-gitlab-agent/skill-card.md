## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to discover assigned GitLab issues and merge requests, make scoped code changes, and manage delivery through review and CI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic GitLab changes may extend beyond the owner-approved work the assistant is intended to handle.

Mitigation: Limit the GitLab account to intended projects, require unambiguous collaborator selection, prevent writes after failed owner checks, and review these controls before enabling recurring automation.

## Reference(s):

- [GitLab user permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)
- [OpenClaw skill creation guide](https://docs.openclaw.ai/tools/creating-skills)
- [Maintained GitLab Agent skill source](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, API calls, Guidance, Markdown]

**Output Format:** [GitLab work item and merge request updates, code and configuration changes, shell commands, and Markdown summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May make GitLab changes for assigned work after project access and assignment checks.]

## Skill Version(s):

1.130.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

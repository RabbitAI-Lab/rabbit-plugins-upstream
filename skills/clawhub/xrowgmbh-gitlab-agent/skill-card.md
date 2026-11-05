## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project maintainers use this agent to process assigned GitLab issues and merge requests, manage the work queue, and prepare code changes and reviews. It uses project-access and assignment checks to guide those tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access checks may still allow unintended GitLab changes or collaborator access.

Mitigation: Keep recurring automation disabled until the identified access issues are fixed; use a dedicated account scoped to approved projects.

Risk: Local process isolation does not contain changes made with authenticated GitLab access.

Mitigation: Validate deployment permissions and external CI components, and require authorized risk acceptance before suppressing vulnerabilities.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab contribution guide](https://docs.gitlab.com/development/contributing/#make-changes-and-open-a-merge-request)
- [OpenClaw skill creation guide](https://docs.openclaw.ai/tools/creating-skills)
- [Discovery performance notes](references/discovery-performance.md)
- [Documentation style guide](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, GitLab issue and merge request updates]

**Output Format:** [Markdown with shell commands and code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can perform GitLab changes for work that passes the documented access and assignment checks.]

## Skill Version(s):

1.129.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

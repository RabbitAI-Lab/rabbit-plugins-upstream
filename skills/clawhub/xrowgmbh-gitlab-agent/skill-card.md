## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use the agent to discover assigned GitLab issues and merge requests, check access and assignment, and deliver authorized changes through guarded workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied security summary reports access-boundary and write-scope concerns, and notes that the scan was partial.

Mitigation: Review those concerns before enabling the skill; avoid supplying a write-enabled GitLab token unless its authorized tasks require one, and monitor any authorized write actions.

## Reference(s):

- [GitLab Agent source](https://gitlab.com/xrow-public/helm-openclaw/-/tree/main/profile/eugene-harold-krabs/skills/gitlab-agent)
- [GitLab permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [OpenClaw skill creation guidance](https://docs.openclaw.ai/tools/creating-skills)
- [Discovery performance notes](references/discovery-performance.md)
- [Documentation style guidance](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Analysis, Code, Shell commands, Configuration, Markdown]

**Output Format:** [GitLab work item and merge request updates, code changes, and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform GitLab writes using the configured GITLAB_TOKEN.]

## Skill Version(s):

1.130.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

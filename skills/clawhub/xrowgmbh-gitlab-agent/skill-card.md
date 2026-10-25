## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this agent to handle assigned GitLab issues, work items, and merge requests, including review and delivery tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization-denied work may still lead to project modifications.

Mitigation: Fix writes on authorization denial and use a GitLab account restricted to intended projects; review manual behavior before enabling unattended operation.

Risk: Ambiguous collaborator matching may allow work from unintended collaborators.

Mitigation: Correct collaborator matching, explicitly limit fork maintenance and automatic merging, and keep recurring jobs disabled until the behavior is reviewed.

## Reference(s):

- [GitLab Agent release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab skills project](https://gitlab.com/xrow-public/skills)
- [GitLab role permissions](https://docs.gitlab.com/user/permissions/#default-roles)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Guidance, Configuration]

**Output Format:** [GitLab actions with concise text or Markdown summaries; configuration examples may use JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions and results depend on configured GitLab credentials, project access, and assignment status.]

## Skill Version(s):

1.118.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

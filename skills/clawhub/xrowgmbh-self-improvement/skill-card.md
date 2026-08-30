## Description:

A GitLab-focused skill that helps an agent propose self-improvement changes as merge requests for the helm-openclaw project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to have an agent reflect on improvement opportunities, open focused GitLab merge requests, and close stale self-created merge requests for the helm-openclaw project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The personal self-improvement framing can understate that the skill may create and close merge requests in a specific GitLab project.

Mitigation: Review before installing, use a GitLab token scoped only to the intended helm-openclaw project, and run it only where the agent is allowed to create and close merge requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the glab CLI and GITLAB_TOKEN for GitLab operations.]

## Skill Version(s):

1.84.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

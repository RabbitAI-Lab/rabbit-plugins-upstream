## Description:

A skill that prompts an agent to reflect on improvement opportunities and create or manage GitLab merge requests for the helm-openclaw project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to record self-improvement findings as GitLab merge requests and to close stale merge requests created by the agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a GitLab token to create, assign, or close merge requests in a live project.

Mitigation: Install only with a tightly scoped GitLab token and require user approval before creating, assigning, or closing merge requests.

Risk: The security verdict is suspicious because the skill is presented as self-improvement while enabling live GitLab merge request management.

Mitigation: Review the skill before installation and confirm that GitLab project access is intended for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown with GitLab merge request actions and possible glab command usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and a GitLab token when performing GitLab operations.]

## Skill Version(s):

1.94.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

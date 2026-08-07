## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to reflect on possible improvements to the helm-openclaw project and prepare focused GitLab merge requests. The skill can also guide cleanup of older self-authored merge requests that have not been accepted after recent activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on a live GitLab project with a token capable of merge request actions, including creating, assigning, and closing merge requests.

Mitigation: Install only for the intended GitLab project, use a minimally scoped token, and review each proposed merge request action before execution.

Risk: The skill is framed as personal self-improvement but its behavior can affect repository workflow state.

Mitigation: Review the skill behavior before use and be especially careful with closing older merge requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with proposed GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN; actions target the helm-openclaw GitLab project.]

## Skill Version(s):

1.79.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

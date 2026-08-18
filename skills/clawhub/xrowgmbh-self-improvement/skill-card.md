## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to identify meaningful improvements for the helm-openclaw project and propose them through focused merge requests. It can also direct the agent to close stale self-created merge requests after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill description under-discloses GitLab write actions that can create, assign, or close merge requests.

Mitigation: Install only when the agent is expected to act on the helm-openclaw GitLab project with a GitLab token, and require approval before creating, assigning, or closing merge requests.

Risk: The skill can direct an agent to close older self-created merge requests after 10 days without acceptance.

Mitigation: Review the target merge request, recent activity, and review state before allowing closure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab Project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown prose, code changes, shell commands, and GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN for GitLab operations.]

## Skill Version(s):

1.84.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

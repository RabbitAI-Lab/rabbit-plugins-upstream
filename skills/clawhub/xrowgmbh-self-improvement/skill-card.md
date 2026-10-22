## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using the helm-openclaw GitLab project can ask their agent to turn useful learnings into separate, self-assigned merge requests and close their own merge requests that remain unaccepted for 10 days after recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish agent-generated ideas and close the agent's merge requests without requiring approval.

Mitigation: Use a project-restricted GitLab token, review and approve proposed content and closures, and consult the separate gitlab-agent skill before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Markdown, GitLab merge requests]

**Output Format:** [Markdown merge request findings and ideas, submitted as a GitLab merge request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also close the agent's own merge requests that meet the stated inactivity condition.]

## Skill Version(s):

1.117.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

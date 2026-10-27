## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

GitLab agents use this skill to record substantive self-improvement findings in a self-assigned merge request, keep unrelated issues separate, and close their own merge requests that remain unaccepted for 10 days after recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs an agent to publish merge requests and close its own older merge requests without explicitly requiring user approval.

Mitigation: Confirm the destination project before enabling the skill, use credentials limited to that project, and require approval of merge request content and proposed closures.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Findings and improvement ideas in GitLab merge request content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the glab command-line tool and GITLAB_TOKEN.]

## Skill Version(s):

1.122.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

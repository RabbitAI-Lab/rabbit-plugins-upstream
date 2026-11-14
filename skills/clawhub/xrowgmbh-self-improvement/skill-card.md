## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to reflect on an agent's work, prepare a merge request for a worthwhile improvement in the xrow-public/helm-openclaw GitLab project, and close the agent's own merge requests that remain unaccepted for 10 days after the latest activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish findings in merge requests and close its own older merge requests without clear task-specific authorization.

Mitigation: Check the target project and planned actions, and ensure merge request creation or closure can be reviewed and authorized before execution.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, GitLab merge request content and actions]

**Output Format:** [Markdown guidance and GitLab merge request updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and a GITLAB_TOKEN for GitLab project access.]

## Skill Version(s):

1.144.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

GitLab agents use this skill to reflect on possible improvements, propose distinct findings in merge requests, and close their own older merge requests that have not been accepted after 10 days without recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to publish findings to a preset GitLab project and close older merge requests without a clear approval step.

Mitigation: Require approval of the destination, publication content, and each closure candidate; restrict cleanup to this workflow's requests and use narrowly scoped GitLab access.

Risk: Repository ownership and the permissions of the GitLab token are unverified.

Mitigation: Verify project ownership and token permissions before enabling the skill.

## Reference(s):

- [GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown findings and merge request descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the configured GitLab project and requires the glab command and GITLAB_TOKEN.]

## Skill Version(s):

1.130.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

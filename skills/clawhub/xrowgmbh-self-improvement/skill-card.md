## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to reflect on prior work and prepare focused improvement merge requests in the xrow-public/helm-openclaw project. It directs the agent to assign new merge requests to itself and close its own merge requests after 10 days without acceptance since recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to create and close merge requests in a fixed project without clearly requiring authorization for those actions.

Mitigation: Confirm helm-openclaw is the intended project, and review proposed content and require approval before posting or closing merge requests.

Risk: The GitLab token may grant more access than the skill needs.

Mitigation: Restrict GITLAB_TOKEN to the permissions needed for this project.

Risk: The referenced gitlab-agent skill and destination project visibility are unverified.

Mitigation: Verify the referenced skill and confirm the project's visibility before use.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, GitLab merge request content]

**Output Format:** [Markdown merge request proposal and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets the helm-openclaw GitLab project.]

## Skill Version(s):

1.128.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

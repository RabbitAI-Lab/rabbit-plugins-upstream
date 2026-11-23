## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

GitLab agents use this skill to identify useful improvements for the helm-openclaw project and propose separate changes in merge requests. It also directs the agent to close its own merge requests after 10 days without acceptance or recent activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs an agent to create merge requests and close its own older requests, actions that may be outside the user's intent.

Mitigation: Review proposed content before submission and require confirmation before closing merge requests.

## Reference(s):

- [helm-openclaw project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Markdown merge request proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create merge requests and close its own older merge requests.]

## Skill Version(s):

1.151.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

An agent can reflect on improvements to the helm-openclaw GitLab project and, when it finds a substantive change, write the findings in a new merge request assigned to itself. The instructions also direct it to close its own merge requests that remain unaccepted for 10 days after recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs an agent to publish information and create, assign, or close GitLab merge requests, with unclear authorization and privacy boundaries according to the security assessment.

Mitigation: Before installation, review the requested GitLab actions and destination, and decide whether those publishing and merge request actions are authorized.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown findings and ideas for a GitLab merge request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions say to stop when no valuable improvement is found or the proposed change is cosmetic.]

## Skill Version(s):

1.134.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

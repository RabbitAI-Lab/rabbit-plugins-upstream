## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to identify worthwhile improvements in the helm-openclaw project, propose each improvement in a separate merge request assigned to themselves, and close their own merge requests that have been inactive for ten days.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs publication of merge requests and closure of older merge requests without clearly requiring authorization.

Mitigation: Review and approve proposed publications and closures, confirm the project is intended, and restrict the GitLab token to authorized projects and permissions.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown merge request proposals and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to create self-assigned merge requests and close eligible older merge requests in GitLab.]

## Skill Version(s):

1.130.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

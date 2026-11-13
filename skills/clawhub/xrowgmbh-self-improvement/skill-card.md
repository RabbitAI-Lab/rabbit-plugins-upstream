## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

An agent maintaining xrow-public/helm-openclaw uses this skill to identify worthwhile improvements, document each focused change in a GitLab merge request, and close its own stale unaccepted merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and close GitLab merge requests; ClawScan flags unclear project-specific authorization and safeguards for what gets shared.

Mitigation: Before installing, review whether you want these merge-request actions and whether the safeguards around publishing and closing requests are acceptable.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Findings and proposed improvements documented in a GitLab merge request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks the agent to keep separate issues in separate merge requests.]

## Skill Version(s):

1.141.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides an agent to propose improvements on a specified GitLab project through merge requests and close its older, unaccepted requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using a GitLab-connected agent can document improvement ideas as assigned merge requests for the helm-openclaw project and close their own stale, unaccepted requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The general self-improvement framing can obscure that the skill directs an agent to use GitLab credentials on a specified external project.

Mitigation: Use only when work on that exact project under your GitLab identity is intended; confirm the repository and merge-request content before submission.

Risk: The agent may close its own older, unaccepted merge requests after ten days without recent activity.

Mitigation: Require explicit confirmation of each merge request before closure.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Text and GitLab merge-request descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, assign, and close merge requests on the named GitLab project.]

## Skill Version(s):

1.95.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

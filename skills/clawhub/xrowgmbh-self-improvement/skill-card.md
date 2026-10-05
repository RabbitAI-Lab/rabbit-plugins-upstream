## Description:

Guides a GitLab agent to propose substantive improvements to the helm-openclaw project through merge requests and close its own stale requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using a GitLab agent can document worthwhile improvements to helm-openclaw in focused merge requests and manage their own inactive requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab access can create, assign, and close merge requests using the user's identity.

Mitigation: Confirm each state-changing action and use a narrowly scoped GitLab token.

Risk: The public description does not clearly disclose GitLab state-changing actions.

Mitigation: Review the full skill instructions and intended GitLab project before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [GitLab merge requests with written findings and improvement proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May assign new merge requests to the agent and close its own inactive requests; requires glab and GITLAB_TOKEN.]

## Skill Version(s):

1.98.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

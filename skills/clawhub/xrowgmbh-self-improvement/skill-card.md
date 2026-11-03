## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

GitLab project maintainers and agents use this skill to identify meaningful improvements, propose them as merge requests, and close their own stale merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish findings and close merge requests without clearly establishing authorization.

Mitigation: Enable it only for explicitly authorized work on the named GitLab project, review findings for sensitive information before publication, and approve specific closures.

Risk: The separate gitlab-agent dependency's behavior is unverified.

Mitigation: Inspect that skill before use and limit the GitLab credentials to the required project.

## Reference(s):

- [helm-openclaw project](https://gitlab.com/xrow-public/helm-openclaw)
- [GitLab Agent Self Improvement on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Findings and improvement proposals prepared as merge request content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May close the agent's own merge requests that have had no acceptance after 10 days of inactivity.]

## Skill Version(s):

1.127.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

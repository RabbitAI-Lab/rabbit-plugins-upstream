## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to reflect on work in the named GitLab project and prepare focused improvement merge requests. It also directs the agent to close its own merge requests that have had no acceptance after 10 days since recent activity or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs GitLab publishing and closure of older merge requests without clearly tying those actions to the user's request.

Mitigation: Use only for deliberate work on the named project; review proposed changes and confirm which merge requests may be closed before allowing those actions.

Risk: A GitLab token may allow actions beyond the intended project scope.

Mitigation: Review the separate gitlab-agent skill and limit the token's permissions to the required work.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Markdown, GitLab merge request content]

**Output Format:** [Markdown findings and improvement proposals submitted as focused GitLab merge requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Targets the named GitLab project; the skill asks for merge requests to be assigned to the agent itself.]

## Skill Version(s):

1.118.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents working on the helm-openclaw GitLab project use this skill to reflect on improvements, propose focused merge requests, and close stale self-authored merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and close merge requests on the named GitLab project using GITLAB_TOKEN.

Mitigation: Install only for agents intended to operate on that project, scope the token narrowly, and review merge-request actions before accepting changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text with possible GitLab CLI commands and merge-request content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN for GitLab operations.]

## Skill Version(s):

1.81.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

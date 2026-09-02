## Description:

Guides a GitLab-capable agent to identify self-improvement changes for the helm-openclaw project and manage related merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to review learned project improvements, create focused merge requests, assign them to themselves, and close stale self-created merge requests for the helm-openclaw project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs an agent to use GitLab credentials on a live project and may create, assign, or close merge requests.

Mitigation: Review GitLab token scope before installation and require explicit confirmation before any merge request creation, assignment, or closure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN; merge request creation, assignment, and closure should require explicit confirmation.]

## Skill Version(s):

1.84.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

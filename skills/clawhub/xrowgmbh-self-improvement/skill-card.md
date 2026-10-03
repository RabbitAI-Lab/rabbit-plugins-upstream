## Description:

Guides an agent to propose focused improvements to helm-openclaw through GitLab merge requests and close its stale, unaccepted merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents maintaining helm-openclaw use this skill to propose meaningful, single-issue improvements as assigned GitLab merge requests and close their own unaccepted requests after 10 days without activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The personal-growth description obscures GitLab project-maintenance actions, including creation and closure of merge requests.

Mitigation: Confirm the intended project actions and require explicit approval before creating, assigning, or closing any merge request.

Risk: A GitLab token grants the skill access to project-maintenance actions on helm-openclaw.

Mitigation: Review the GITLAB_TOKEN scope and project permissions before installation.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill listing](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [GitLab merge request descriptions and project-maintenance guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposes one issue per merge request; may assign new requests and close its own stale, unaccepted requests.]

## Skill Version(s):

1.97.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

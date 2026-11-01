## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to identify worthwhile improvements to the helm-openclaw project, prepare and assign focused merge requests, and close their own merge requests that have gone without activity for ten days. Use it only for explicitly authorized GitLab maintenance, with review of proposed content and approval of closures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may publish or close merge requests in a fixed GitLab project without clearly establishing user approval.

Mitigation: Use only for explicitly authorized GitLab maintenance; confirm the target project, review content before publication, approve closures, restrict credentials to the intended project, and inspect the separate gitlab-agent skill before enabling this workflow.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [Markdown, API Calls]

**Output Format:** [Merge request descriptions and GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates one merge request per distinct improvement and may close the agent's own stale merge requests.]

## Skill Version(s):

1.124.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

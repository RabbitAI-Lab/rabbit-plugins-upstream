## Description:

Guides a GitLab agent to propose substantive improvements to helm-openclaw and manage its own merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to identify meaningful improvements to helm-openclaw, propose each issue in a separate merge request, and manage previously proposed changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The self-improvement description does not clearly convey that the skill can create, assign, or close GitLab merge requests.

Mitigation: Review the skill before installing and require explicit approval before any merge-request changes.

Risk: A GitLab token with broad permissions may allow changes beyond the intended project.

Mitigation: Use a GitLab token limited to the intended project.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Merge-request descriptions and GitLab merge requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, assign, or close merge requests; requires glab and a GitLab token.]

## Skill Version(s):

1.96.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

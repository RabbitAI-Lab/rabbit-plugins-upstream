## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this agent to discover and complete assigned GitLab issues, work items, and merge requests, including code changes and review workflows. It is intended for owner-authorized project work with security and assignment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated workflows may accept unintended collaborators or modify projects that fail the authorization check.

Mitigation: Use a dedicated GitLab account restricted to approved projects; require unambiguous collaborator selection and verify denied projects receive no writes before enabling recurring runs.

Risk: Incident adoption and fork maintenance can extend automated work beyond the intended task scope.

Mitigation: Require explicit authorization for incident adoption and fork maintenance, and keep denied, unassigned, or ambiguous targets pending.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab project permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [GitLab skills project](https://gitlab.com/xrow-public/skills)
- [documentation-style.md](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Text, Markdown]

**Output Format:** [GitLab issue and merge request updates, code changes, and Markdown comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, and a GitLab token.]

## Skill Version(s):

1.117.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

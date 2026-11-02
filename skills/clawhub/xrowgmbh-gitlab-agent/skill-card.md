## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to manage assigned GitLab issues and merge requests with project access and assignment checks. It provides guidance and helper tooling for discovery, review, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization flaws could cause changes to excluded projects or acceptance of unintended collaborators.

Mitigation: Before granting write access or enabling recurring runs, review the authorization checks; verify denied projects remain untouched and collaborator acceptance uses exact group identities.

Risk: An authenticated GitLab account can make changes that are not contained by local isolation, and live permissions or deployment configuration have not been verified.

Mitigation: Use a dedicated account limited to intended projects, restrict fork maintenance to approved projects, and require security acceptance for vulnerability exceptions.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [OpenClaw skill creation guidance](https://docs.openclaw.ai/tools/creating-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown instructions, shell commands, configuration examples, and Python helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab authentication and the glab, jq, and uv command-line tools.]

## Skill Version(s):

1.124.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

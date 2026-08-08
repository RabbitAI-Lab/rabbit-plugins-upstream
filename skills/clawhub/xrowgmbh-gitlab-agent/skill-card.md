## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an assigned agent discover GitLab issues and merge requests, verify owner-created project access, manage workflow labels, create branches and merge requests, and drive review-ready delivery through GitLab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent standing GitLab developer-level authority to change assigned projects without asking for confirmation each time.

Mitigation: Use a tightly scoped GitLab token, limit project membership, and enable the skill only for projects where this level of delegated authority is acceptable.

Risk: Recurring automation, fork maintenance, and CI/CD variable operations can broaden operational impact if enabled beyond the intended workflow.

Mitigation: Review the recurring job before enabling it and remove or constrain fork maintenance and CI/CD variable operations unless they are explicitly needed.

Risk: Work on unauthorized project objects could expose or modify GitLab content outside the owner-approved scope.

Mitigation: Keep the owner membership security gate enabled so work fails closed when active project membership is missing, incomplete, or not created by the configured owner.

## Reference(s):

- [ClawHub GitLab Agent](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/Components/label)
- [CI Tools](https://ci-tools.xrow.de/)
- [OpenClaw skill creation guidance](https://docs.openclaw.ai/tools/creating-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and GitLab CLI/API actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and jq, with GITLAB_TOKEN as the primary environment variable.]

## Skill Version(s):

1.80.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

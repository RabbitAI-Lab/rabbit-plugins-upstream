## Description:

Operates assigned GitLab work with owner-verified project access and guarded merge request delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to discover assigned GitLab issues, incidents, and merge requests, then implement and track work through review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated autonomous writes can affect issues, branches, merge requests, labels, incidents, and pipelines.

Mitigation: Use a dedicated least-privilege GitLab token, limit project access, and require explicit approval for remote writes where appropriate.

Risk: Recurring execution can continue making changes without a fresh request.

Mitigation: Review the scheduled-job setup and enable it only after a successful manual run.

Risk: CI-skip pushes and variable or release management can bypass expected review or affect deployment settings.

Mitigation: Remove CI-skip behavior if every push must run CI, and gate variable and release changes behind explicit approval.

## Reference(s):

- [Documentation style guide](references/documentation-style.md)
- [GitLab permissions and roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [OpenClaw skill authoring guidance](https://docs.openclaw.ai/tools/creating-skills)
- [GitLab skill project](https://gitlab.com/xrow-public/skills)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with GitLab links and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitLab issues, branches, merge requests, labels, and comments.]

## Skill Version(s):

1.109.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

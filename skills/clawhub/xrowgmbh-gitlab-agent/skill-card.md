## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to work on assigned GitLab issues and merge requests, including code changes, reviews, and workflow updates within permitted projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous GitLab writes can affect projects beyond the intended task if token permissions are broad.

Mitigation: Use a narrowly scoped GitLab token and review the projects and actions it permits before enabling the agent.

Risk: Recurring execution can repeat changes without a fresh human check.

Mitigation: Test a manual run first, review the recurring job setup, and monitor subsequent runs.

Risk: CI skipping, release or variable changes, and cross-project or fork actions may have wider consequences.

Mitigation: Consider requiring human approval for these actions.

## Reference(s):

- [GitLab project permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [OpenClaw skill documentation](https://docs.openclaw.ai/tools/creating-skills)
- [Documentation style guidance](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Markdown, Configuration instructions]

**Output Format:** [Markdown, shell commands, and code changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitLab branches, merge requests, issues, labels, and comments.]

## Skill Version(s):

1.97.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

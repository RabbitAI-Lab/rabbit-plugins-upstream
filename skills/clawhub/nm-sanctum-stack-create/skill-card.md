## Description:

Initializes a stacked branch set from an ordered plan, one branch per slice with parent-child links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn a sequential implementation plan into a local stack of dependent Git branches. It is intended for workflows where each change must land after the previous slice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill intentionally changes local Git branch state.

Mitigation: Review the base branch, generated branch names, and working-tree status before running checkout commands.

Risk: A poorly sliced plan can create confusing branch dependencies.

Mitigation: Confirm that each slice is a single logical concern with a clear dependency on the previous slice before creating branches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-create)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ordered progress-tracking items and Git branch topology checks.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

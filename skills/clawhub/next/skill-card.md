## Description:

Next suggests follow-up actions after task completion, including stall checks, ask gates, and context-specific next-step options for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill after completing work to decide, present, and route follow-up actions such as verification, task creation, fix escalation, cleanup, or project checklist updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-trigger and steer follow-up work rather than acting as a passive suggestion helper.

Mitigation: Review the auto-trigger behavior before installation and keep user confirmation gates active for decision points.

Risk: The skill may inspect task lists, local backlog files, and GitHub state to compose next-action options.

Mitigation: Use it only in workspaces where that project context is appropriate for the agent to read.

Risk: The skill can route selected follow-ups into task creation, fix, cleanup, project checklist updates, or PR-related wording.

Mitigation: Review proposed actions before execution, especially in repositories where unintended follow-up work or public PR actions would be costly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next)
- [Ask Gates](ask-gates.md)
- [Stall Detection](stall-detect.md)
- [Suggestion Patterns](suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with selectable next-action options and occasional inline commands or checklist entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect local task state and project backlog files before proposing follow-up actions.]

## Skill Version(s):

0.7.2 (source: release metadata and changelog, released 2026-08-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

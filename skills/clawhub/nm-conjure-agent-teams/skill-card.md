## Description:

Coordinates Claude agent teams via filesystem protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to coordinate multiple Claude Code agents on parallel implementation, review, refactoring, and task-management workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Team workflows can launch, terminate, restart, and reassign Claude/tmux teammate sessions with limited explicit operator guardrails.

Mitigation: Use the skill in a controlled workspace and require human approval before recovery, shutdown, or reassignment actions on critical work.

Risk: The workflow creates persistent team, task, inbox, and lock files under ~/.claude that can affect later agent sessions if left stale.

Mitigation: Before removing lock files or deleting team state, confirm no related agents or tmux panes are still running and inspect the affected team/task directories.

Risk: Parallel agents can create conflicting file changes or duplicate work when tasks overlap or stalled agents are automatically released.

Mitigation: Use role and risk-tier assignment rules, approval gates for high-risk tasks, and worktree isolation for parallel editing when file ownership may overlap.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-agent-teams)
- [Conjure plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may describe persistent team, task, and inbox files under ~/.claude and tmux or iTerm2 teammate sessions.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Use when executing implementation plans with independent tasks in the current session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to execute implementation plans with mostly independent tasks by coordinating implementer and reviewer subagents, preserving progress in plan-scoped artifacts, and routing blockers or review findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow is designed to proceed through implementation tasks with limited human check-ins.

Mitigation: Review the implementation plan before running the skill and stop when ambiguity, blockers, or review conflicts require a human decision.

Risk: The skill coordinates commits, review packages, reports, and temporary workspace files in the repository.

Mitigation: Use an isolated worktree or workspace, keep artifacts plan-scoped, and inspect commits and review reports before merge.

Risk: Subagents may produce incomplete or incorrect implementation work when task requirements are flawed or underspecified.

Mitigation: Use the required per-task review, bounded fix loop, scoped re-review, and final whole-branch review before considering the branch complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/subagent-driven-development)
- [Implementer prompt template](artifact/implementer-prompt.md)
- [Task reviewer prompt template](artifact/task-reviewer-prompt.md)
- [Scoped re-review prompt template](artifact/re-review-prompt.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples and prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create plan-scoped task briefs, review packages, reports, and progress ledgers in the repository during use.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

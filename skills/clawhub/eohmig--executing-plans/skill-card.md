## Description:

Use when you have a written implementation plan to execute in a separate session with review checkpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to load, review, execute, verify, and report on a written implementation plan with explicit checkpoints for blockers and clarification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unreviewed implementation plan could cause an agent to make incorrect or unwanted code changes.

Mitigation: Review the plan before execution and stop for clarification when the plan has blockers, unclear instructions, critical gaps, or repeated verification failures.

Risk: Executing development work on a primary branch could mix experimental changes with production history.

Mitigation: Use an isolated workspace or git worktree and do not start implementation on main or master without explicit user consent.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown guidance with possible code changes, shell commands, and status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

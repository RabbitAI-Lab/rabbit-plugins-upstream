## Description:

Run iterative agent loops until success criteria are met with bounded autonomous iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and agent operators use Loop to retry tasks with clear success criteria, verification steps, and bounded iteration. It is useful when a task has a fixable failure path and needs repeated attempts with concise learnings carried forward.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repeated attempts can multiply cost or continue work after several failures.

Mitigation: Use clear success criteria, set a bounded iteration count, and stop when failures indicate a different approach is needed.

Risk: Loop state and attempt summaries may be stored locally under ~/loop.

Mitigation: Avoid storing secrets or sensitive task details in loop summaries, and review local logs when handling confidential work.

Risk: A task that modifies important files could be retried multiple times.

Mitigation: Review file-changing tasks before allowing the loop to continue and require explicit approval for destructive actions.

## Reference(s):

- [Loop on ClawHub](https://clawhub.ai/ivangdavila/skills/loop)
- [Loop Examples](examples.md)
- [Memory Between Iterations](memory.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and structured iteration summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May record loop state and iteration summaries under ~/loop when used.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

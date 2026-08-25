## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to route explicit loop requests into durable task or project queues, run bounded worker ticks, inspect evidence, manage revisions, and report governed completion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to manage durable queues and invoke a CLI that may run worker tasks in a selected workspace.

Mitigation: Confirm the workspace, queue, worker, and routing target; run planning, doctor, and smoke checks before enabling execution.

Risk: Code queue workflows can prepare patches or cleanup actions that affect repository state.

Mitigation: Use review bundles, patch verification, and apply-plan commands first; require explicit confirmation flags before applying patches or cleaning worktrees.

Risk: Scheduler or notification setup can create persistent task wakeups or route progress to the wrong conversation.

Mitigation: Install scheduler and notification routing only after a successful manual tick, and verify source metadata and delivery routing before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm Package Reference](references/npm-package.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration paths, and task evidence references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or inspect loop runtime artifacts, queue status, review bundles, patch plans, and verification summaries through explicit CLI workflows.]

## Skill Version(s):

0.15.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

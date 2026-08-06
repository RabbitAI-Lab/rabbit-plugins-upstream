## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to route explicit loop requests into governed task or project workflows with queue execution, verification, revision handling, and completion reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loop execution can direct Codex to operate task and project workflows in a workspace.

Mitigation: Install only when that operating model is intended, and inspect queue, task, run, and acceptance evidence before treating work as complete.

Risk: Patch application, worktree cleanup, scheduling, external notifications, production changes, credential work, and device instrumentation can affect local or external systems.

Mitigation: Require the explicit confirmation gates described by the skill before allowing those actions.

Risk: A dispatcher-successful run can still produce incomplete or unacceptable work.

Mitigation: Review final judgement, acceptance reviews, checkpoints, verification evidence, unmet checks, blockers, and revision records before reporting completion.

## Reference(s):

- [npm Package](references/npm-package.md)
- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/loop-engineering)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown guidance with inline shell commands and file/path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces governed workflow guidance and commands for explicit loop invocations; no fixed token cap.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

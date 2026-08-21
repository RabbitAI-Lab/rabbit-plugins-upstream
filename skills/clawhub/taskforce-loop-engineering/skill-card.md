## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route explicit Loop Engineering requests into durable task or project queues with scoped execution, progress reporting, verification, revisions, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loop execution can create queue files, run worker ticks, manage code worktrees, send scoped notifications, or configure scheduler integration.

Mitigation: Review installation and execution plans before mutation, and require explicit confirmation for patch application, cleanup, deployment, credential changes, external posting, and long-running scheduler setup.

Risk: A dispatcher-successful run can still fail acceptance or omit required project work.

Mitigation: Inspect final judgement, acceptance reviews, checkpoints, verification evidence, amendments, and project completion contracts before reporting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and structured status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or reference queue, project, worktree, verification, revision, and scheduler artifacts when the Loop Engineering CLI is installed and explicitly invoked.]

## Skill Version(s):

0.15.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

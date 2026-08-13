## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route explicitly requested task or project work into durable loop workflows with queue state, verification evidence, revisions, progress reporting, and governed completion semantics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation or routing could target the wrong workspace, queue, worker agent, scheduler, or notification destination.

Mitigation: Review the plan-only installer output before enabling writes, and stop if the root path, queue, worker agent, scheduler, or notification routing is not exactly intended.

Risk: Confirmation flags authorize real workspace changes.

Mitigation: Use confirmation flags only after reviewing the requested action, then run the documented doctor and smoke checks before important loop tasks.

Risk: A dispatcher-successful run can still fail the intended task or project acceptance criteria.

Mitigation: Inspect final judgement, acceptance reviews, checkpoints, and verification evidence before reporting completion or advancing project status.

## Reference(s):

- [npm Package](references/npm-package.md)
- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [taskforce-loop-engineering GitHub repository](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands, configuration paths, and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce queue, project, verification, patch, notification, and closeout artifacts when the corresponding CLI is installed and authorized.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

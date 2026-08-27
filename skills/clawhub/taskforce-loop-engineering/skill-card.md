## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route explicit loop requests into durable task or project queues, run bounded execution ticks, track verification evidence, and manage revisions or human gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or routing a loop against the wrong workspace, queue, worker, scheduler, or notification target can send work to the wrong environment.

Mitigation: Review the installer plan output before writes, confirm the root, queue, worker, scheduler, and notification routing, then run doctor and smoke checks before real tasks.

Risk: A loop run may involve destructive changes, production configuration, credentials, paid usage, or external messaging beyond the user's original authority.

Mitigation: Require explicit approval before destructive, production, credential, paid, or external-message actions and treat missing approval as a human gate.

Risk: Dispatcher success can be mistaken for accepted task or project completion.

Mitigation: Inspect final judgement, acceptance reviews, checkpoints, and verification evidence before reporting completion; distinguish task or milestone status from total project status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)
- [GitHub repository listed by skill documentation](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce queue, task, project, checkpoint, review, and verification artifact paths for follow-up inspection.]

## Skill Version(s):

0.15.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

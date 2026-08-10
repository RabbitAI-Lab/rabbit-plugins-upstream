## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to route explicit loop requests into durable task or project queues, run bounded worker ticks, inspect verification evidence, and manage revisions, human gates, and completion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the CLI can create queue artifacts and execute worker ticks in the workspace.

Mitigation: Use the skill only after explicit loop invocation, verify the CLI or integration first, and review installation plans before confirming writes.

Risk: Scheduler setup, notifications, patch application, cleanup, production changes, credentials, paid usage, and external messages can have higher operational impact.

Mitigation: Require deliberate user approval for those actions and run doctor or smoke checks after integration changes.

Risk: Dispatcher exit status alone can misrepresent completion.

Mitigation: Inspect final judgement, acceptance reviews, checkpoints, and verification evidence before reporting a loop complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm Package Reference](references/npm-package.md)
- [Taskforce Loop Engineering Repository](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create queue, project, scheduler, worktree, review, patch, and notification artifacts when explicitly invoked and confirmed.]

## Skill Version(s):

0.9.0 (source: server release metadata and references/npm-package.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

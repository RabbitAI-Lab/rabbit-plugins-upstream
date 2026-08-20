## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent-workflow operators use this skill to route explicit loop requests into durable task or project queues, verify progress and acceptance artifacts, manage revisions, and complete work only when governed checks pass.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automate local workflow actions when explicitly invoked.

Mitigation: Use it only for intentional loop orchestration, review queue state and generated artifacts, and require human authorization for external messages, destructive actions, credential changes, production changes, paid usage, or device/process instrumentation.

Risk: Platform integrations, schedulers, notifications, patch application, and cleanup can change how work is routed or applied in a workspace.

Mitigation: Review generated installation plans before confirmation, run doctor and smoke checks after integration changes, and require explicit confirmation flags before applying patches or cleaning worktrees.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and operational status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local loop runtime artifacts, queue state, verification evidence, and human authorization gates.]

## Skill Version(s):

0.15.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

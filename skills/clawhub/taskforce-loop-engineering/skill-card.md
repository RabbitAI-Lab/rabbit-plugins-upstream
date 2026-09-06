## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to route explicit loop requests into durable task or project queues, verify progress artifacts, manage revisions and human gates, and report completion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed integrations can create local services and modify loop or workspace artifacts.

Mitigation: Review the install plan first, run doctor and smoke workflows, and only confirm installation when the target root, queue, worker, and dashboard exposure match the intended deployment.

Risk: Loop execution can produce code patches, queue state changes, project artifacts, or human-gate decisions.

Mitigation: Use the skill's confirmation-gated commands, inspect generated evidence, and require explicit approval for patch application, worktree cleanup, external actions, credentials, destructive operations, and production changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON artifact references, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer to queue, project, gate, verification, review, patch, and dashboard artifacts created by the loop tooling.]

## Skill Version(s):

0.15.15 (source: server release evidence and npm package reference)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

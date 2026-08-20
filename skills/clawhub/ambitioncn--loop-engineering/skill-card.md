## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route explicit loop requests into durable task or project queues, inspect progress and evidence, manage revisions, and apply governed completion semantics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loop setup and execution can change workspace state through queue configuration, scheduler setup, patch application, or worktree cleanup.

Mitigation: Review read-only plans and diagnostics first, then require explicit confirmation flags for installation, patch application, cleanup, and scheduler changes.

Risk: A loop could route progress or terminal notifications to the wrong conversation or workspace if source metadata is missing or incorrect.

Mitigation: Preserve source channel, target, account, message id, and reply-to metadata, and fail closed when delivery routing is incomplete.

Risk: External messages, credential changes, production deployment changes, paid API use, destructive deletion, and device instrumentation exceed ordinary loop authority.

Mitigation: Treat those actions as separate human-approval gates and stop until the required authorization is provided.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/loop-engineering)
- [npm package reference](artifact/references/npm-package.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code]

**Output Format:** [Markdown with inline shell commands, file paths, JSON artifact references, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize read-only diagnostics before mutation, explicit confirmation for gated actions, and evidence-backed task or project status.]

## Skill Version(s):

0.15.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

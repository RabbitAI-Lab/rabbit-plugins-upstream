## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route explicit loop requests into durable task or project execution workflows with queueing, progress updates, verification evidence, revision handling, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loop tasks can modify code, contact external services, use paid APIs, or touch credentials through the configured runner.

Mitigation: Review workspace loop configuration before installation and keep the skill's explicit confirmation gates for external writes, destructive actions, production changes, credential changes, and paid usage.

Risk: Progress notifications or terminal results could be routed to the wrong conversation if delivery metadata is missing or incorrect.

Mitigation: Preserve source channel, target, account, message id, and reply-to metadata, and fail closed when delivery routing is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces workflow routing instructions, status guidance, verification expectations, and CLI command examples for an agent.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

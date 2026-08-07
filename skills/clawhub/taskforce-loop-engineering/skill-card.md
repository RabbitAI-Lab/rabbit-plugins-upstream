## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route explicit loop-engineering requests into durable task or project queues with progress reporting, verification, revision handling, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking the related CLI may run an npm-distributed package in the local workspace.

Mitigation: Confirm the package source is trusted before installation or npx use, and review any generated installation plan before confirming it.

Risk: Persistent queues, scheduler ticks, and task artifacts can change how work is executed and retained in a workspace.

Mitigation: Enable queues or schedulers only in workspaces where durable task artifacts and automated runner ticks are appropriate, and run manual verification before adding scheduled cadence.

Risk: Loop tasks can approach external, destructive, production, credential, or instrumentation actions if a user asks for them.

Mitigation: Require explicit human confirmation for those higher-impact actions and treat missing authorization as a stop condition.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm Package](references/npm-package.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON references, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task contracts, plans, queue status summaries, verification evidence summaries, revision requests, and human-approval prompts.]

## Skill Version(s):

0.7.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

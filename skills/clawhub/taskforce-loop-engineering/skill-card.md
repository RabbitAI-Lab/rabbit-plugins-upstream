## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route explicitly requested loop work into durable task or project queues, run bounded execution ticks, inspect evidence, manage revisions, and report completion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can create durable task queues and write local runtime or configuration files.

Mitigation: Confirm the intended workspace, queue, and worker before installation or execution, and review the generated installation plan before using confirmation flags.

Risk: Optional scheduler or platform integration wiring can route future loop work automatically.

Mitigation: Enable scheduler or integration changes only after a successful manual tick and use doctor and smoke checks to verify the target platform, routing, and queue.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)
- [Official repository named in skill artifact](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local runtime and configuration artifacts when the user explicitly invokes loop workflows and confirms gated operations.]

## Skill Version(s):

0.15.5 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

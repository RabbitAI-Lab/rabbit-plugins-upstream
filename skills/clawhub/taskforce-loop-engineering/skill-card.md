## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to run explicit task and project loops that queue work, execute bounded worker-agent ticks, track verification evidence, manage revisions, and report completion status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can queue work, run worker agents, and write local runtime or configuration artifacts.

Mitigation: Review the installation plan, verify the selected workspace and queue, and run doctor or smoke checks before using mutable workflows.

Risk: Destructive, production, credential, paid, external-message, and instrumentation actions could exceed the user's intended authority if treated as implicit loop permissions.

Mitigation: Keep separate confirmation gates for those action classes and fail closed when authorization or delivery routing is missing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm Package Reference](artifact/references/npm-package.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local runtime and configuration artifacts when the underlying CLI and integrations are installed and explicitly invoked.]

## Skill Version(s):

0.15.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

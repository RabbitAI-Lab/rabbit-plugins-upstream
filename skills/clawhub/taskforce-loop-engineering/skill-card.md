## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route explicit Loop Engineering requests into durable task or project queues, with verification, revision handling, progress reporting, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A loop integration installed against the wrong root, queue, worker, scheduler, or notification target could route work or progress updates incorrectly.

Mitigation: Review the read-only installation plan first and confirm the intended root path, queue name, worker agent, scheduler, and notification target before enabling writes.

Risk: Patch application, cleanup, external posting, production changes, credential changes, or scheduled automation can have higher operational impact.

Mitigation: Use read-only doctor/status commands first and require explicit approval before these actions.

Risk: Assuming a CLI or platform integration exists can produce misleading queue status or execution results.

Mitigation: Check the CLI and integration with the documented help, doctor, and smoke commands before running real tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)
- [GitHub repository listed in skill artifact](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline bash code blocks and structured status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include confirmation gates, queue/status summaries, and verification evidence paths.]

## Skill Version(s):

0.15.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to route explicit loop requests into durable task or project queues with progress reporting, verification evidence, revisions, and governed completion. It supports loop-based code work, project intake, queue status review, and controlled handoff through the taskforce-loop-engineering CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent toward queue execution, patch application, cleanup, external messages, credential changes, production changes, or scheduled execution when a user explicitly invokes loop workflows.

Mitigation: Require the confirmation prompts described by the artifact and server security guidance before those actions, and review generated plans or evidence before allowing mutation.

Risk: A ClawHub skill installation may not include the CLI or OpenClaw integration needed to execute loop commands.

Mitigation: Check CLI availability first, use the read-only OpenClaw install plan, and run doctor or smoke verification before using the integration for a real task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [Project repository listed in artifact](https://github.com/ambitioncn/taskforce-loop-engineering)
- [npm package reference](references/npm-package.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, code]

**Output Format:** [Markdown with inline shell commands and structured status or evidence references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference workspace loop artifacts, project specs, queue state, verification evidence, patch review bundles, and completion reports.]

## Skill Version(s):

0.7.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

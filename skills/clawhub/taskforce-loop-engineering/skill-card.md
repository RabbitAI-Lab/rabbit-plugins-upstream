## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to route explicit loop requests into durable task or project queues with verification, revision handling, progress reporting, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-managed task queues can write loop and project artifacts and run bounded worker steps in a workspace.

Mitigation: Review selected workspace roots, queue names, worker-agent ids, installer plan summaries, and scheduler setup before enabling writes or automatic continuation.

Risk: The skill may target the wrong local deployment if the CLI or platform integration is missing or misconfigured.

Mitigation: Check the CLI with help commands first, review plan-only installer output, then run doctor and smoke checks before using real tasks.

Risk: Some actions, including destructive changes, production configuration, credential changes, outreach, or paid API usage, require authority beyond ordinary loop invocation.

Mitigation: Require explicit human confirmation for those actions and treat missing permission as a stop condition.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [npm Package Reference](references/npm-package.md)
- [GitHub Repository](https://github.com/ambitioncn/taskforce-loop-engineering)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce loop or project artifact paths, status summaries, verification notes, and human-authorization prompts.]

## Skill Version(s):

0.14.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

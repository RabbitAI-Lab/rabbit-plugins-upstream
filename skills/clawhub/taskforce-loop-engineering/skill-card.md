## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use the skill when they explicitly request a task or project loop. It guides durable work through checkpoints, verification, revisions, progress reporting, and human approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking the separately distributed CLI can download and execute code, and the skill documentation may not match the installed implementation.

Mitigation: Review and pin the CLI version before installation, verify the implementation providing the needed feature, and treat npx invocations as code execution.

Risk: Integration setup can configure a worker, scheduler, notifications, and a dashboard for a chosen workspace.

Mitigation: Review the installation plan's platform, workspace, worker, scheduler, notification destination, and spending budget; keep the dashboard local unless Tailnet access is deliberately restricted, then run the documented doctor and smoke checks.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [Documented project repository](https://github.com/ambitioncn/taskforce-loop-engineering)
- [npm package and CLI commands](artifact/references/npm-package.md)
- [OpenClaw multi-IM diagnostics](artifact/references/openclaw-diagnostics.md)
- [Task and project acceptance guidance](artifact/references/scope-task-acceptance.md)
- [Frozen-input verification guidance](artifact/references/frozen-input-verification.md)
- [Context budget and durable handoff](artifact/references/context-budget.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes workflow steps and confirmation gates for task execution, integration setup, and verification.]

## Skill Version(s):

0.16.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

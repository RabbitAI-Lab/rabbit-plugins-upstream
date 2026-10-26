## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use the skill to coordinate bounded agent tasks, maintain project queues, verify work, and manage revisions and human approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded CLI code may execute during package inspection or installation.

Mitigation: Pin and review the CLI version before installation; do not assume `npx --help` is side-effect-free.

Risk: Background work can affect a workspace, use ongoing resources, run persistent services, or send notifications.

Mitigation: Before confirming, review the workspace, worker, notification destination, usage budget, and persistent services; keep the dashboard local unless Tailnet access is intended.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [Publisher installation and removal instructions](https://github.com/ambitioncn/taskforce-loop-engineering#readme)
- [Context budget guidance](references/context-budget.md)
- [npm package and CLI reference](references/npm-package.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown, Status reports]

**Output Format:** [Markdown guidance, shell commands, JSON configuration and task artifacts, and progress/status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workspace changes and background work depend on explicit task actions; patch application and worktree cleanup require separate confirmation.]

## Skill Version(s):

0.16.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

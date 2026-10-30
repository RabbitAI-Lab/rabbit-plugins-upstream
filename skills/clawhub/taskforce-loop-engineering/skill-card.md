## Description:

Durable explicit task/project loops with verification, revisions, live progress, and governed completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they explicitly request Loop Engineering to manage a bounded task or project through queued work, verification, revisions, progress reporting, and governed completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Background task execution can create saved task records and incur model costs.

Mitigation: Review the installation plan’s workspace, worker, scheduler, and notification destination; use a reviewed, pinned CLI version and an explicit task scope.

Risk: A Tailnet dashboard has no separate application login, so access depends on Tailnet controls.

Mitigation: Keep the dashboard local unless Tailnet access is intended, and restrict that access with Tailscale ACLs or Grants.

Risk: Even a help command executes the downloaded package.

Mitigation: Review and pin the CLI package before invocation, and inspect its installation plan before enabling writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/taskforce-loop-engineering)
- [Frozen input verification](artifact/references/frozen-input-verification.md)
- [Context budget and recovery](artifact/references/context-budget.md)
- [Scope and task acceptance](artifact/references/scope-task-acceptance.md)
- [npm package and CLI commands](artifact/references/npm-package.md)
- [OpenClaw multi-IM diagnostics](artifact/references/openclaw-diagnostics.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide task or project plans, queue actions and status, verification guidance, and progress or completion summaries, depending on the explicit request and installed integration.]

## Skill Version(s):

0.16.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

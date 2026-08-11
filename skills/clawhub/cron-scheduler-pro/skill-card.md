## Description:

定时调度专家 helps agents manage local recurring and one-time scheduled tasks with timezone confirmation, run previews, cleanup, file-lock based writes, retry, and circuit-breaker guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to turn natural-language schedule requests into local job definitions and operational guidance for recurring checks, reports, reminders, and health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for local write and command-execution authority for persistent scheduled Agent tasks.

Mitigation: Install only in trusted workspaces, review scheduled job definitions before enabling them, and inspect the local job store regularly.

Risk: The security evidence notes conflicting documentation about local-only behavior, API keys, and execution mode.

Mitigation: Confirm whether the release is truly local-only before use and avoid providing API keys unless a specific scheduled task explicitly requires them.

Risk: Cleanup and lock-file actions can affect persisted scheduler state.

Mitigation: Back up the scheduler memory directory before cleanup and remove lock files only after confirming no scheduler process is using them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cron-scheduler-pro)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes local job-store files, scheduler commands, execution status, and operational checks.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

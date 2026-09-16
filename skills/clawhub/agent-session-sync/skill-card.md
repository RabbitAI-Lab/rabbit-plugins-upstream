## Description:

Session Sync helps agents migrate, back up, inspect, and archive local chat histories across multiple AI coding agents so users can continue prior conversations in dsh or other supported targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chendestiny](https://clawhub.ai/user/chendestiny)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to move AI coding-agent session context between tools, export Markdown archives, and review local session state before applying changes. It is most relevant when a user wants to continue a prior conversation in another agent or preserve session history during tool migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can export, restore, delete, and mutate broad local session histories across multiple agents.

Mitigation: Start with selftest, status, and dry-run commands; use explicit source and scope limits, keep backups, and require review before any apply operation.

Risk: One-line remote shell installers increase installation review risk.

Mitigation: Prefer a reviewed local or marketplace install, or inspect installer contents before running remote installation commands.

Risk: The local web dashboard exposes session inspection and export surfaces.

Mitigation: Run the dashboard only when needed and avoid using it while browsing untrusted sites.

Risk: Restores, pruning, and target-agent mutations can be overwritten or conflict if target agents are still running.

Mitigation: Fully close target agents before restore, prune, or regression-test operations and verify results after changes.

## Reference(s):

- [Server-resolved source repository](https://github.com/Chendestiny/agent-session-sync)
- [Release commit](https://github.com/Chendestiny/agent-session-sync/commit/f257a1f3055a48278c99cf7437e3c6b6b5f2c874)
- [English README](https://github.com/Chendestiny/agent-session-sync/blob/f257a1f3055a48278c99cf7437e3c6b6b5f2c874/README_EN.md)
- [Agent operator manual](https://github.com/Chendestiny/agent-session-sync/blob/f257a1f3055a48278c99cf7437e3c6b6b5f2c874/AGENTS.md)
- [Session format documentation](https://github.com/Chendestiny/agent-session-sync/blob/f257a1f3055a48278c99cf7437e3c6b6b5f2c874/docs/FORMATS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown and text guidance with shell commands and local session, backup, archive, or configuration file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default workflows are dry-run oriented and require explicit source, scope, and apply confirmations before broad session changes.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

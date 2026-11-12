## Description:

Init Hooks helps agents manage persistent OpenClaw startup hooks that run inline commands, local shell or Python scripts, or remote CDN packages across restarts and rebuilds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to install, add, inspect, edit, disable, delete, run, and log startup hooks that should persist across agent restarts or rebuilds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent startup hooks can run arbitrary local or remote code across restarts and rebuilds.

Mitigation: Install only when persistent startup code is required, review every hook before enabling it, and audit post-init.sh, start.sh, hooks.json, dispatcher.sh, and last-run.log regularly.

Risk: Remote URL hooks can execute code fetched from external sources.

Mitigation: Avoid remote URL hooks unless the source is fully trusted and pinned; prefer reviewed local scripts for sensitive environments.

Risk: Vague agent requests could add or run hooks with broader impact than intended.

Mitigation: Require explicit user intent before adding, enabling, or running hooks and review proposed commands before execution.

## Reference(s):

- [Init Hooks README](artifact/README.md)
- [Hook authoring best practices](artifact/references/best-practices.md)
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/init-hooks)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are single-stream operational guidance for managing OpenClaw startup hooks and related configuration sync.]

## Skill Version(s):

1.0.0 (source: server release metadata and README changelog, released 2026-07-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

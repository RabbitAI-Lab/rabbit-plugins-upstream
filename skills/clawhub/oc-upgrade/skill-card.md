## Description:

Provides an environment-aware OpenClaw upgrade runbook that probes the host and routes agents through Windows schtasks or Linux systemd upgrade steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangsuann](https://clawhub.ai/user/tangsuann)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators maintaining OpenClaw use this skill to plan and execute version upgrades while checking the host environment, Node compatibility, plugins, backups, restart handling, verification, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make broad local maintenance changes to an OpenClaw installation.

Mitigation: Confirm the target version, review host-specific scheduled-task or systemd commands before execution, and complete the documented environment, Node, plugin, and service checks first.

Risk: Backup steps can create additional copies of secret configuration such as .env files.

Mitigation: Treat backups as sensitive, restrict their permissions, and remove or rotate them after the upgrade or rollback window closes.

Risk: Upgrade or restart handling can interrupt the gateway if the wrong platform path is used.

Mitigation: Use the documented platform-specific restart flow, set the post-restart notification before changing services, verify health checks, and use the rollback procedure on any failed acceptance check.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tangsuann/skills/oc-upgrade)
- [OpenClaw releases](https://github.com/openclaw/openclaw/releases)
- [npm registry](https://registry.npmjs.org/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown runbook with PowerShell and bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes environment-specific Windows and Linux branches, backup, notification, verification, and rollback steps.]

## Skill Version(s):

1.9.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

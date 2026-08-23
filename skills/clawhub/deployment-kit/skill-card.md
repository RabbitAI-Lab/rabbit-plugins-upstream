## Description:

Deployment Kit helps agents deploy and maintain VPS services with deploy scripts, systemd and cron templates, watchdog restarts, heartbeat checks, and Telegram alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to prepare, restart, verify, and monitor VPS-hosted services they own. It is suited for operational deployment workflows that need shell scripts, service templates, heartbeat checks, and alerting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad restart and background-process authority can interrupt services or affect unintended processes.

Mitigation: Review and edit scripts before installation, test on staging, use fixed service names or an allowlist, and avoid broad pkill patterns.

Risk: Heartbeat and log files in /tmp can be weak local control points for production monitoring.

Mitigation: Move heartbeat and log files out of /tmp where possible and use restrictive permissions for operational state files.

Risk: Telegram credentials sourced from an environment file can be exposed if file parsing or permissions are too permissive.

Mitigation: Replace shell sourcing with strict variable parsing and apply restrictive permissions to the Telegram environment file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/deployment-kit)
- [Telegram API endpoint](https://api.telegram.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash snippets and service template files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deployment, watchdog, notification, and systemd service assets; no evaluation artifacts were provided.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

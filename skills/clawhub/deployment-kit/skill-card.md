## Description:

Deploy and maintain VPS services with scripts for restart, verification, heartbeat monitoring, and Telegram alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to prepare VPS deployment commands and service templates for applications they own. It helps restart services, verify health endpoints, configure watchdog checks, and send Telegram alerts when a heartbeat becomes stale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment commands can restart services, change runtime state, and cause downtime on a VPS.

Mitigation: Use only on systems you control, review scripts before running them, test with --dry-run or staging first, and keep a rollback plan.

Risk: Telegram bot credentials can be exposed if stored or logged carelessly.

Mitigation: Store TG_BOT_TOKEN and TG_CHAT_ID in ~/.config/tg-alert.env with chmod 600 and avoid putting credentials in scripts, logs, shell history, or git.

Risk: Broad sudo permissions or arbitrary process patterns can affect unintended services.

Mitigation: Avoid broad sudo access and prefer known systemd unit names over arbitrary pkill process patterns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/deployment-kit)
- [Telegram Bot API endpoint](https://api.telegram.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference systemd units, cron entries, deployment scripts, health checks, and Telegram alert environment variables.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

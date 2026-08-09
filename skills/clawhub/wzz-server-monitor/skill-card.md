## Description:

Monitors Linux server CPU, memory, and disk usage, then sends SMTP email alerts when configured thresholds are exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiuyiwzz](https://clawhub.ai/user/xiuyiwzz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure local Linux resource monitoring, check current resource status, test SMTP alerting, and install a cron-based monitoring check.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs an ongoing user-level cron job for local monitoring.

Mitigation: Review install.sh before running it and remove the wzz-server-monitor crontab entry when monitoring is no longer needed.

Risk: SMTP credentials and alert recipients are required for email notifications.

Mitigation: Store the SMTP secret in ~/.config/resource-monitor/.smtp_secret with restricted permissions and verify recipients before sending tests or alerts.

Risk: Alert emails can disclose server identifiers and resource status.

Mitigation: Use appropriate recipient lists and templates for the operational environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xiuyiwzz/skills/wzz-server-monitor)
- [README](artifact/README.md)
- [Configuration Example](artifact/assets/config.example.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to run monitor.py commands that read server metrics, write local config and state files, install a user crontab, and send SMTP email when configured.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

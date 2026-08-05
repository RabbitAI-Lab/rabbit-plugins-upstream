## Description:

Monitors server CPU, memory, and disk usage and sends SMTP email alerts when configured thresholds are exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiuyiwzz](https://clawhub.ai/user/xiuyiwzz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to configure and run a Linux server resource monitor that checks CPU, memory, and disk thresholds, sends SMTP alerts, and helps inspect monitor status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can add a recurring cron job that runs the monitor every five minutes.

Mitigation: Review the crontab entry before running assets/install.sh and remove it when monitoring is no longer needed.

Risk: SMTP email alerts require server, recipient, and secret configuration.

Mitigation: Review the SMTP host and recipients before testing or installing, and store the SMTP secret in a permission-restricted file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiuyiwzz/skills/wzz-server-monitor)
- [README](artifact/README.md)
- [Skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run the bundled monitor script, validate configuration, send a test email, or install a recurring Linux cron check.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

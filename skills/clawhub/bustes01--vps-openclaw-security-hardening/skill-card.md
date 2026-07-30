## Description: <br>
Production-ready security hardening for VPS running OpenClaw AI agents, including SSH hardening, firewall configuration, audit logging, credential management, and alerting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bustes01](https://clawhub.ai/user/bustes01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to harden a dedicated Ubuntu or Debian VPS that runs OpenClaw AI agents. It provides installation, verification, rollback, monitoring, and alerting workflows for SSH, UFW, auditd, fail2ban, cron jobs, and credential file permissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses root-level SSH, firewall, audit, package-management, and cron authority, so a bad install path can lock users out or alter host security behavior. <br>
Mitigation: Review the installer before execution, install only on a disposable or dedicated VPS, confirm SSH key access and a working sudo account first, keep an active session open, and use the included verification and rollback scripts. <br>
Risk: Alerting can send security logs, login summaries, audit events, or tokens to external services when notification channels are configured. <br>
Mitigation: Configure Telegram, Discord, Slack, webhook, or email alerting only after confirming that sending those security events to the selected service is acceptable. <br>
Risk: The artifact warns against using the skill on machines with sensitive personal data or unrelated production workloads. <br>
Mitigation: Use a dedicated VPS or test VM, avoid hosts with sensitive personal or financial data, and test the workflow before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bustes01/skills/vps-openclaw-security-hardening) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [CHANGELOG.md](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces privileged VPS hardening and verification workflows for Ubuntu and Debian systems.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

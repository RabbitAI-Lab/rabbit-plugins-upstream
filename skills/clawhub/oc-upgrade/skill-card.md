## Description: <br>
OpenClaw Upgrade guides an agent through a standard OpenClaw upgrade workflow, including environment checks, Node compatibility checks, IPv4/IPv6 registry checks, plugin compatibility review, backup, upgrade, validation, restart, and rollback steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tangsuann](https://clawhub.ai/user/tangsuann) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw operators and developers use this skill when upgrading an OpenClaw installation and need a repeatable operational checklist with compatibility checks, backup steps, post-upgrade validation, restart guidance, and rollback instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow reads ~/.openclaw/.env and creates versioned plaintext backups that may contain secrets. <br>
Mitigation: Review the token lookup before installation, restrict permissions on backup files, and delete or encrypt secret-bearing backups after the upgrade is verified. <br>
Risk: The workflow can upgrade global OpenClaw packages, which may affect other users on the same host. <br>
Mitigation: Run the included same-host and WSL user checks, confirm compatibility with affected users, and require explicit approval before executing the global npm upgrade. <br>
Risk: The workflow can restart the OpenClaw gateway and interrupt active sessions. <br>
Mitigation: Use the gateway restart path when available, set the one-time completion notification before restart, validate service recovery, and use the documented rollback path if checks fail. <br>
Risk: Cross-user and WSL discovery can expose local installation details beyond the current user. <br>
Mitigation: Limit discovery to hosts where the operator is authorized to inspect other OpenClaw installs, and remove or narrow cross-user discovery when that scope is not needed. <br>
Risk: A one-time cron notification is scheduled as part of the restart workflow. <br>
Mitigation: Confirm delete-after-run behavior, review the notification payload for sensitive details, and clean up the scheduled task manually if the upgrade is cancelled. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tangsuann/skills/oc-upgrade) <br>
- [OpenClaw Release Notes API](https://api.github.com/repos/openclaw/openclaw/releases/tags/v${TARGET_VER}) <br>
- [npm Registry](https://registry.npmjs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command blocks and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes pre-upgrade checks, approval gates, backup verification, validation criteria, restart guidance, and rollback commands.] <br>

## Skill Version(s): <br>
1.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Helps an agent perform a zero-downtime OpenClaw Gateway upgrade by checking release notes, confirming with the user, backing up the current install, running npm install, checking Node.js compatibility, restarting the service, and rolling back on failure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luffertlu](https://clawhub.ai/user/luffertlu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to upgrade a live OpenClaw Gateway installed with npm and managed by user systemd. It is intended for agent-assisted maintenance where the user reviews release notes and confirms the upgrade before the script changes packages or restarts the service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The upgrade changes a global OpenClaw package, edits the user systemd unit, and restarts a live gateway service. <br>
Mitigation: Review release notes, confirm the target host and service name, and run only when a maintenance window or operator approval is appropriate. <br>
Risk: A Node.js version mismatch could leave the upgraded service unable to start. <br>
Mitigation: Use the documented compatibility pre-check and ExecStart node path correction before restart; stop and upgrade Node.js first if no compatible runtime is found. <br>
Risk: The upgrade can fail after package installation or service restart. <br>
Mitigation: Keep the fallback backup in place until the health check passes, use the rollback path on failure, and review logs under ~/.openclaw. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/luffertlu/skills/self-upgrade-gateway) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command execution steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational guidance and may invoke the bundled shell script for package changes, systemd unit edits, service restart, health checks, logs, backup cleanup, or rollback.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

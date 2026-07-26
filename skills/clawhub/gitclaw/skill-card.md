## Description: <br>
Back up the OpenClaw agent workspace to a GitHub repository and keep it synced with a cron-driven commit and push script. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marian2js](https://clawhub.ai/user/marian2js) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use GitClaw to back up an OpenClaw agent workspace to a user-controlled GitHub repository and keep it synchronized on a schedule. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flagged broad GitHub workspace syncing with persistent cron automation and limited review controls. <br>
Mitigation: Install only when repeated GitHub backup is intended, review the files before any push, and confirm the crontab entry and local backup script can be removed. <br>
Risk: Workspace backups can send secrets, logs, or other unintended files to GitHub. <br>
Mitigation: Use a private repository, exclude secrets and logs before the first push, and review repository visibility before enabling scheduled sync. <br>
Risk: Setup can require sudo package installation and recurring cron configuration. <br>
Mitigation: Require approval before sudo installs or cron setup, and verify the installed script at ~/.openclaw/gitclaw/auto_backup.sh before relying on it. <br>


## Reference(s): <br>
- [GitClaw homepage](https://gitclaw.ai) <br>
- [GitClaw on ClawHub](https://clawhub.ai/marian2js/skills/gitclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and a Bash backup script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a repository name, repository visibility, and optional backup frequency; may request GitHub authentication and reports the repo URL, schedule, and local script path after setup.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

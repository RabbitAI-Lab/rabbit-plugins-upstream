## Description: <br>
Optimized OpenClaw backup skill for creating full snapshots with workspace archive splitting, change summaries, restore instructions, and Discord notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cccarv82](https://clawhub.ai/user/cccarv82) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to install, configure, and run automated backups of OpenClaw state, including cron setup, workspace archive splitting, backup reporting, and restore guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The backup can copy sensitive OpenClaw data to the configured Git remote. <br>
Mitigation: Use a private repository, review the backup contents before the first push, and avoid storing sensitive tokens in backed-up files where possible. <br>
Risk: The backup script can force-push to BACKUP_REPO_URL. <br>
Mitigation: Use a dedicated backup repository or branch and verify BACKUP_REPO_URL before enabling scheduled runs. <br>
Risk: Scheduled backups can repeatedly send OpenClaw state to the remote without interactive review. <br>
Mitigation: Run the script manually first, inspect the generated backup and report, then enable cron only after confirming the scope is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cccarv82/skills/openclaw-backup-optimized) <br>
- [Backup skill configuration](references/CONFIG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and PowerShell commands, plus a Node.js backup script and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup steps, cron commands, restore guidance, backup reports, archive parts, SHA256 hashes, Git commits, and optional Discord messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

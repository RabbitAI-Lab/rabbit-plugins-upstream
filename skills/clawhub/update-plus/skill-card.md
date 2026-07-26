## Description: <br>
Full backup, update, and restore for OpenClaw - config, workspace, and skills with auto-rollback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hopyky](https://clawhub.ai/user/hopyky) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use Update Plus to back up OpenClaw configuration, workspace, and skill directories, check for updates, run updates with rollback support, and restore from backups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool can overwrite or delete OpenClaw data during restore and update workflows. <br>
Mitigation: Review the configuration and targets before use, run check or dry-run first, and keep a known-good backup before restoring or updating. <br>
Risk: Backups can include sensitive OpenClaw data and may be uploaded to remote storage. <br>
Mitigation: Encrypt backups before enabling cloud sync and keep remote_storage.path dedicated to this tool. <br>
Risk: Cron-based automatic updates can apply future code changes without an interactive review. <br>
Mitigation: Enable cron only when unattended updates are acceptable, and review the schedule, logs, and source before relying on it. <br>
Risk: The evidence flags a missing entrypoint that should be verified before use. <br>
Mitigation: Confirm the expected executable exists and matches the documented commands before installation or execution. <br>


## Reference(s): <br>
- [Update Plus on ClawHub](https://clawhub.ai/hopyky/skills/update-plus) <br>
- [hopyky publisher profile](https://clawhub.ai/user/hopyky) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Example configuration](artifact/update-plus.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in backup archives, logs, restored files, git updates, cron entries, notifications, and optional encrypted or remote-synced backups when executed.] <br>

## Skill Version(s): <br>
4.0.3 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Secure sync for OpenClaw memory and workspace. Use /sync to push, /restore to pull, /sync-status to check. Supports versioned snapshots and disaster recovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arakichanxd](https://clawhub.ai/user/arakichanxd) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to back up, sync, inspect, and restore OpenClaw memory files, workspace rules, daily logs, and custom skills through versioned repository snapshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads sensitive OpenClaw memory, profile, workspace-rule, daily-log, and custom-skill files to a remote repository. <br>
Mitigation: Use an empty dedicated private repository, a fine-grained token limited to that repository, and review /sync --dry-run before uploading. <br>
Risk: Restore operations can overwrite local memory files and skill directories, and --force skips the confirmation prompt. <br>
Mitigation: Avoid /restore --force unless a separate backup exists; verify the selected version and use the local backup created before restore for recovery if needed. <br>
Risk: The backup token is stored in ~/.openclaw/.backup.env and is used for recurring or manual sync operations. <br>
Mitigation: Restrict file permissions on ~/.openclaw/.backup.env, use the least-privileged token available, and rotate the token if exposure is suspected. <br>
Risk: Optional 12-hour auto-sync can repeatedly upload changed workspace data. <br>
Mitigation: Enable recurring sync only when recurring uploads are intended, and periodically review the private repository contents and token permissions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/arakichanxd/skills/claw-sync) <br>
- [Source Repository](https://github.com/arakichanxd/Claw-Sync) <br>
- [README.md](https://github.com/arakichanxd/Claw-Sync/blob/main/README.md) <br>
- [SKILL.md](https://github.com/arakichanxd/Claw-Sync/blob/main/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, Files] <br>
**Output Format:** [Command-line text output, configuration snippets, git repository snapshots, and local backup files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can push, restore, list, and inspect backups; dry-run mode previews sync scope without writing remote changes.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

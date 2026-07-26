## Description: <br>
Lightweight session cleanup tool for OpenClaw that removes old session backups, checkpoints, and trajectory files to prevent disk bloat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and maintainers use this skill to report on and clean stale local session backups, checkpoints, trajectory logs, trajectory indexes, and lock files so session storage does not grow unchecked. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup settings can move session artifacts that a user still expects to keep. <br>
Mitigation: Run with --dry-run first, review the reported files, and choose retention windows before executing cleanup. <br>
Risk: A recurring cron entry can continue moving matching artifacts on schedule after cleanup needs change. <br>
Mitigation: Add scheduled cleanup only when recurring cleanup is intended, and review the cleanup log and cron configuration periodically. <br>
Risk: Moved files remain in the local trash area and may contain session data. <br>
Mitigation: Review local trash contents and logs before restoring or permanently removing files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/session-cleanup) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports dry-run, report-only, retention-window options, and cron setup guidance; cleanup actions move matching files to local trash.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

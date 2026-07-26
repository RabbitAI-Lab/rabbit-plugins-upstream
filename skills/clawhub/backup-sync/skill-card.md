## Description: <br>
Intelligent file backup with compression and verification for backup, sync, integrity checks, deduplication, restore, and manifest tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Smart Backup to create local file backups, preview and run directory syncs, verify backup integrity, identify duplicate files, and restore files from manifest-backed backups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Backup and restore operations can copy or overwrite local files when run against important directories. <br>
Mitigation: Run backup, sync, and restore with dry-run first, and use force or delete options only after reviewing the planned changes. <br>
Risk: Backups contain full file contents and manifests contain full paths. <br>
Mitigation: Store backup directories in private locations and avoid targeting secrets or system directories unless that exposure is intentional. <br>


## Reference(s): <br>
- [Smart Backup on ClawHub](https://clawhub.ai/jlacroix82/skills/backup-sync) <br>
- [Publisher profile](https://clawhub.ai/user/jlacroix82) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local backup manifests and status output; no external dependencies are required.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

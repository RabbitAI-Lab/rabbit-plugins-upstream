## Description: <br>
Set up scheduled automated backups with version tracking and cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zfanmy](https://clawhub.ai/user/zfanmy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to configure cron-scheduled backups of directories or files, trigger backups when versions change, list backup archives, and clean up older backups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create persistent cron jobs from user-provided paths and schedules. <br>
Mitigation: Use trusted absolute paths and inspect the generated crontab entry before relying on scheduled execution. <br>
Risk: Version-triggered backups can execute user-supplied shell text when a version source is provided as a command string. <br>
Mitigation: Prefer a version file or a trusted command path; avoid unreviewed command strings as version sources. <br>
Risk: Cleanup permanently deletes matching backup archives according to the retention policy. <br>
Mitigation: Test cleanup in a dedicated backup directory and set retention and minimum-backup values before using it on important data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zfanmy/skills/cron-backup) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command examples and shell script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates timestamped tar.gz backup archives, cron entries, backup logs, version records, and backup listings when its scripts are run.] <br>

## Skill Version(s): <br>
0.3.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Back up OpenClaw customizations, including memory, configuration, skills, and workspace data, to cloud or local storage with scheduling and retention. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vidarbrekke](https://clawhub.ai/user/vidarbrekke) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure recurring backups of local OpenClaw data, optionally uploading archives through rclone and keeping local or remote retention under control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Backups may contain sensitive OpenClaw memory, configuration, skills, workspace data, and project files. <br>
Mitigation: Review the configured backup paths, test local-only mode first, and use encrypted storage or an encrypted rclone remote for offsite backups. <br>
Risk: Setup can create recurring scheduler entries through LaunchAgent, cron, or Task Scheduler. <br>
Mitigation: Inspect generated scheduler files or entries after installation and run the backup script manually before enabling recurring execution. <br>
Risk: Remote retention settings can delete older backup archives from the configured rclone destination. <br>
Mitigation: Verify the rclone remote, destination prefix, and retention period before enabling cloud mode. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vidarbrekke/skills/claw-backup) <br>
- [rclone installation documentation](https://rclone.org/install/) <br>
- [Node.js](https://nodejs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated backup or scheduler files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate a customized backup shell script, macOS LaunchAgent plist, cron entry guidance, rclone destination settings, retention settings, logs, checksums, and restore notes.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.15) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

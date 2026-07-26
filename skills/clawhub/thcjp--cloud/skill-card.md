## Description: <br>
Cloud helps users choose, organize, sync, share, and back up files across consumer cloud storage services such as iCloud, Google Drive, Dropbox, and OneDrive. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill for consumer cloud storage selection, cleanup, sync troubleshooting, backup planning, sharing, and basic security guidance. It is scoped to personal storage services and is not intended for infrastructure cloud platforms such as AWS, Azure, or S3. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution even though its consumer cloud-storage function is primarily advisory. <br>
Mitigation: Install it only in agent environments that restrict shell access or require explicit confirmation before running commands. <br>
Risk: Cleanup or deletion advice can remove files from synced devices or cloud accounts. <br>
Mitigation: Verify service-specific behavior and confirm backups before deleting or moving synced files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cloud) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance with optional shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include service-selection recommendations, cleanup steps, backup practices, file-sharing advice, and account security guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Backup Clawdbot workspace and config to GitHub with git-crypt encryption for daily automated backups and manual backup or restore operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[louzhixian](https://clawhub.ai/user/louzhixian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Clawdbot users use this skill to configure encrypted GitHub backups for ~/clawd and ~/.clawdbot, run daily or manual backups, and restore those repositories on a new machine. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive workspace or configuration files could be pushed to GitHub before git-crypt filters are active or verified. <br>
Mitigation: Use private repositories, initialize git-crypt before the first push, and confirm encrypted paths are unreadable from a fresh clone before enabling automation. <br>
Risk: Automated backups can commit and push unintended local files if repository status and ignore rules are not reviewed. <br>
Mitigation: Inspect `git status` and `.gitignore` rules before scheduling the backup script, and keep noisy or sensitive paths excluded unless encrypted. <br>
Risk: Losing exported git-crypt keys can make encrypted backups unrecoverable. <br>
Mitigation: Export workspace and config keys and store them in a secure password manager or another protected backup location. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/louzhixian/skills/git-crypt-backup) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and a shell script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes git-crypt setup steps, .gitattributes examples, restore commands, and a backup script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

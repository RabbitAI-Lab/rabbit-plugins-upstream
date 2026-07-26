## Description: <br>
Comprehensive backup, update, and restore workflow with dynamic workspace detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pasogott](https://clawhub.ai/user/pasogott) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to prepare Clawdbot updates by checking upstream state, validating local setup, creating backups, following update guidance, and restoring from trusted backups when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Backups may contain credentials, sessions, authentication tokens, and workspace data. <br>
Mitigation: Keep ~/.clawdbot-backups private, preferably encrypted, and do not share generated backup archives. <br>
Risk: Restore operations can overwrite current Clawdbot configuration, state, and workspaces. <br>
Mitigation: Restore only from trusted backups after reviewing the target backup and confirming the interactive restore prompt. <br>
Risk: Dynamic workspace discovery follows paths from ~/.clawdbot/clawdbot.json. <br>
Mitigation: Run the dry run first and review configured workspace paths before creating a full backup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pasogott/skills/clawdbot-skill-update) <br>
- [Publisher profile](https://clawhub.ai/user/pasogott) <br>
- [Clawdbot project repository](https://github.com/clawdbot/clawdbot) <br>
- [Clawdbot Skill Update homepage](https://github.com/pasogott/clawdbot-skill-update) <br>
- [npm package: @clawdbot/skill-update](https://www.npmjs.com/package/@clawdbot/skill-update) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and local backup archive files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local backup directories under ~/.clawdbot-backups and can overwrite local Clawdbot state during restore.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

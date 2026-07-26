## Description: <br>
Automatically update Clawdbot and all installed skills once daily, then message the user with a summary of what changed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pntrivedy](https://clawhub.ai/user/pntrivedy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External Clawdbot users and developers use this skill to configure daily cron-based updates for Clawdbot and installed skills, with concise reports about successful updates and failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Daily unattended updates can change Clawdbot and all installed skills without per-update approval. <br>
Mitigation: Enable only when unattended updates are intended; review the cron entry and any helper script, prefer dry-run or manual review in sensitive environments, and keep a rollback path. <br>
Risk: Detailed update summaries can expose operational metadata if delivered through third-party channels. <br>
Mitigation: Use only delivery channels approved for that information, or reduce summary detail when sharing through third-party services. <br>


## Reference(s): <br>
- [Auto Updater 1.0.0 on ClawHub](https://clawhub.ai/pntrivedy/skills/auto-updater-1-0-0) <br>
- [Agent Implementation Guide](references/agent-guide.md) <br>
- [Update Summary Examples](references/summary-examples.md) <br>
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating) <br>
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub) <br>
- [Cron Jobs](https://docs.clawd.bot/cron) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks and update-summary templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May configure a recurring cron job and optional helper script for daily unattended updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

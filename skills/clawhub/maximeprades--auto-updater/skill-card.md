## Description: <br>
Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maximeprades](https://clawhub.ai/user/maximeprades) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Clawdbot users use this skill to schedule daily checks that update Clawdbot and installed skills, then receive a concise summary of what changed or failed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Daily automatic updates can change Clawdbot and every installed skill without review before each update. <br>
Mitigation: Enable the skill only when automatic daily updates are intended; consider dry-run or notify-only behavior and limit updates to trusted skills where possible. <br>
Risk: Scheduled update commands can fail because of permissions, network timeouts, or package conflicts. <br>
Mitigation: Review each delivered update summary, keep logs for failures, and use manual update or diagnostic commands such as dry-run checks and doctor only after reviewing the issue. <br>
Risk: A persistent cron job may continue applying changes after the user no longer wants automatic updates. <br>
Mitigation: Keep the documented cron removal command available and remove or disable the job when automatic updates are no longer desired. <br>


## Reference(s): <br>
- [Auto-Updater Skill on ClawHub](https://clawhub.ai/maximeprades/skills/auto-updater) <br>
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating) <br>
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub) <br>
- [Cron Jobs](https://docs.clawd.bot/cron) <br>
- [Agent Implementation Guide](artifact/references/agent-guide.md) <br>
- [Update Summary Examples](artifact/references/summary-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and cron configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup guidance and update-summary text for scheduled daily maintenance.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

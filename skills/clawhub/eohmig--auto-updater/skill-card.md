## Description: <br>
Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eohmig](https://clawhub.ai/user/eohmig) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure scheduled Clawdbot and skill updates, including cron setup, update commands, and daily summary reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled updates can automatically change Clawdbot and all installed skills without clear per-run approval. <br>
Mitigation: Enable unattended updates only intentionally, and add a review or approval step before applying updates. <br>
Risk: Update commands may pull unreviewed versions into the local agent environment. <br>
Mitigation: Use allowlists, trusted channels, version pinning, backups, and rollback instructions before enabling the cron job. <br>


## Reference(s): <br>
- [Agent Implementation Guide](references/agent-guide.md) <br>
- [Update Summary Examples](references/summary-examples.md) <br>
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating) <br>
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub) <br>
- [Cron Jobs](https://docs.clawd.bot/cron) <br>
- [Auto Updater on ClawHub](https://clawhub.ai/eohmig/skills/auto-updater) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command blocks and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces cron setup instructions, update commands, troubleshooting guidance, and summary message formats.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

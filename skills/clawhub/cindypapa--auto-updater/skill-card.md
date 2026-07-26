## Description: <br>
Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cindypapa](https://clawhub.ai/user/cindypapa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and ClawHub users use this skill to configure scheduled update checks for Clawdbot and installed skills, apply available updates, and receive concise update summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unattended daily updates can change Clawdbot and every installed skill without review. <br>
Mitigation: Start with dry-run or notification-only checks, then enable automatic updates only for trusted or allowlisted skills. <br>
Risk: A problematic update could affect future agent behavior. <br>
Mitigation: Pin critical skills where possible and keep a rollback path before enabling unattended updates. <br>
Risk: Update failures may leave Clawdbot or skills partially updated. <br>
Mitigation: Review each delivered update summary, surface errors clearly, and use the documented manual update commands when intervention is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cindypapa/skills/auto-updater) <br>
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating) <br>
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub) <br>
- [Cron Jobs](https://docs.clawd.bot/cron) <br>
- [Agent Implementation Guide](references/agent-guide.md) <br>
- [Update Summary Examples](references/summary-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command blocks, cron configuration, an optional shell script, and update summary text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets Darwin and Linux according to ClawHub metadata; schedule, timezone, delivery, and update cadence can be configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

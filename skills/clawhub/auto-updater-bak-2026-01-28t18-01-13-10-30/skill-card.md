## Description: <br>
Automatically update Clawdbot and all installed skills once daily. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nicoataiza](https://clawhub.ai/user/nicoataiza) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Clawdbot users use this skill to configure daily update checks that update Clawdbot, update installed skills, and report what changed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unattended daily updates can automatically change Clawdbot and all installed skills. <br>
Mitigation: Review the generated cron entry and update script before enabling, prefer pinning or allowlisting trusted skills where possible, and keep a rollback or backup plan. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nicoataiza/skills/auto-updater-bak-2026-01-28t18-01-13-10-30) <br>
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating) <br>
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub) <br>
- [Cron Jobs](https://docs.clawd.bot/cron) <br>
- [Agent Implementation Guide](references/agent-guide.md) <br>
- [Update Summary Examples](references/summary-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup guidance and update summaries for daily cron-based auto-updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

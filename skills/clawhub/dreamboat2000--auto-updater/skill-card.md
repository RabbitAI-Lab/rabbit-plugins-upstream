## Description: <br>
Automatically update Clawdbot and all installed skills once daily. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dreamboat2000](https://clawhub.ai/user/dreamboat2000) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Clawdbot users use this skill to configure unattended daily updates for Clawdbot and installed skills, then receive a concise summary of what changed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill configures unattended daily updates that can change Clawdbot and every installed skill without a manual review step. <br>
Mitigation: Use the documented dry-run and manual update commands when review is required before code changes are applied. <br>
Risk: A persistent cron job can continue applying updates after the user no longer wants automatic changes. <br>
Mitigation: Confirm the user knows how to remove the Daily Auto-Update cron job or disable cron in configuration before enabling it. <br>
Risk: Update commands may fail because of permissions, network timeouts, or package conflicts. <br>
Mitigation: Report partial success clearly, surface errors in the summary, and direct the user to manual remediation such as checking permissions, connectivity, or running Clawdbot diagnostics. <br>


## Reference(s): <br>
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating) <br>
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub) <br>
- [Cron Jobs](https://docs.clawd.bot/cron) <br>
- [Agent Implementation Guide](references/agent-guide.md) <br>
- [Update Summary Examples](references/summary-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces cron setup guidance, update commands, verification steps, and human-readable update summaries.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

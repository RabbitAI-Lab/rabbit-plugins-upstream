## Description:

Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cindypapa](https://clawhub.ai/user/cindypapa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Clawdbot users use this skill to configure daily automated updates for Clawdbot and installed skills, then receive concise update summaries and failure reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sets up persistent unattended updates that can modify Clawdbot and every installed skill without per-update approval.

Mitigation: Review carefully before installing; prefer dry-run or notification-only updates, pin or approve versions where possible, and confirm how to remove the cron job before enabling it.

Risk: Automatic update commands can fail due to permissions, network issues, package conflicts, or source-install git conflicts.

Mitigation: Log update output, report partial success and failures clearly, run Clawdbot doctor after updates, and use the documented manual commands when intervention is needed.

## Reference(s):

- [ClawHub Auto Updater skill page](https://clawhub.ai/cindypapa/skills/auto-updater)
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating)
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub)
- [Cron Jobs](https://docs.clawd.bot/cron)
- [Agent Implementation Guide](references/agent-guide.md)
- [Update Summary Examples](references/summary-examples.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces cron setup instructions, update commands, troubleshooting guidance, and concise update summary messages.]

## Skill Version(s):

1.0.0 (source: server release metadata, artifact metadata, and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

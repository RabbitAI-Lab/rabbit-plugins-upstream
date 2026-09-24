## Description:

Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Clawdbot users use this skill to configure unattended daily updates for Clawdbot and installed skills, with a concise summary of changed versions and any failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended scheduled updates can change Clawdbot and all installed skills without per-update approval.

Mitigation: Prefer notify-only or dry-run operation, pin or allowlist trusted updates, and keep a rollback or removal plan before enabling daily automation.

Risk: Automatic updates may fail because of permissions, network issues, or package conflicts.

Mitigation: Review delivered update summaries, keep logs for failed runs, and use the documented manual commands to diagnose or roll back partial failures.

## Reference(s):

- [Agent Implementation Guide](references/agent-guide.md)
- [Update Summary Examples](references/summary-examples.md)
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating)
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub)
- [Cron Jobs](https://docs.clawd.bot/cron)
- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/auto-updater)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces setup guidance and update summaries for scheduled Clawdbot and skill updates.]

## Skill Version(s):

1.0.0 (source: server evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

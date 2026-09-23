## Description:

Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dreamboat2000](https://clawhub.ai/user/dreamboat2000)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Clawdbot users use this skill to configure recurring update checks that update Clawdbot and installed skills, then report what changed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic daily updates can change Clawdbot and all installed skills without a review step.

Mitigation: Prefer dry-run or notification-only workflows, pin or approve versions before applying them, and avoid running the updater under a highly privileged account.

Risk: A recurring cron job may continue applying changes after the user's risk tolerance or environment changes.

Mitigation: Document how to inspect and remove the cron job before enabling it, and periodically review whether automatic updates remain appropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dreamboat2000/skills/auto-updater)
- [Agent Implementation Guide](artifact/references/agent-guide.md)
- [Update Summary Examples](artifact/references/summary-examples.md)
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating)
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub)
- [Cron Jobs](https://docs.clawd.bot/cron)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command blocks and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces setup guidance, cron configuration commands, and update summary formats.]

## Skill Version(s):

1.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

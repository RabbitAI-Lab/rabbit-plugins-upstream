## Description:

Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Clawdbot users use this skill to configure a daily update routine that updates Clawdbot and installed skills, then reports what changed or failed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scheduled auto-update routine can change Clawdbot and installed skills without per-update review.

Mitigation: Prefer check-only or dry-run update checks before applying changes, and review update summaries promptly.

Risk: A recurring cron job can continue running after the user's needs or trust assumptions change.

Mitigation: Document and verify the removal path with `clawdbot cron remove "Daily Auto-Update"` or disable cron in configuration.

Risk: Update failures may leave Clawdbot or skills only partially updated.

Mitigation: Report partial success and errors clearly, then guide the user to manual remediation for failed components.

## Reference(s):

- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating)
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub)
- [Cron Jobs](https://docs.clawd.bot/cron)
- [Agent Implementation Guide](references/agent-guide.md)
- [Update Summary Examples](references/summary-examples.md)
- [ClawHub Skill Page](https://clawhub.ai/eohmig/skills/auto-updater)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May configure a recurring cron job and produce update status summaries.]

## Skill Version(s):

1.0.0 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

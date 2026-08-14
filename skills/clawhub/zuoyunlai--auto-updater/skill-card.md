## Description:

Automatically update Clawdbot and all installed skills once daily. Runs via cron, checks for updates, applies them, and messages the user with a summary of what changed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Clawdbot operators use this skill to schedule recurring checks that update Clawdbot and installed skills, then receive a concise report of what changed or failed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A recurring update job can change Clawdbot and all installed skills without per-update approval.

Mitigation: Use this only when unattended updates are acceptable; prefer dry-run notifications, allowlists, manual approval before apply, or manual updates when stability and auditability are required.

## Reference(s):

- [Agent Implementation Guide](references/agent-guide.md)
- [Update Summary Examples](references/summary-examples.md)
- [Clawdbot Updating Guide](https://docs.clawd.bot/install/updating)
- [ClawdHub CLI](https://docs.clawd.bot/tools/clawdhub)
- [Cron Jobs](https://docs.clawd.bot/cron)
- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/auto-updater)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Markdown, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces cron setup guidance and update summary messages; may include optional helper script content.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release metadata, artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

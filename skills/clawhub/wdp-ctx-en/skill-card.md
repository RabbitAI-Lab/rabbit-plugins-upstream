## Description:

Use when the user runs /wdp-ctx-en to save, load, verify, export, or clear the project's context so it survives session reset and can be resumed by any coding agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckystar513](https://clawhub.ai/user/luckystar513)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to persist project context across restarts, context clears, compaction, and agent handoffs. It manages stable project profiles, incremental work snapshots, drift checks, exports to AGENTS.md, document listing, and snapshot cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional reminder hooks persist in Claude configuration and run on session or compaction events.

Mitigation: Review hook entries before installation, prefer project-local settings for tighter scope, and confirm that installed hooks only emit reminder prompts.

Risk: Project profiles, snapshots, and exported AGENTS.md content can preserve sensitive project state if users include it.

Mitigation: Follow the skill's locations-not-secrets rule: record where credentials live, but do not write secrets, tokens, or passwords into generated documents.

Risk: The clear subcommand removes snapshot files.

Mitigation: Require the delete list and second confirmation before deletion, keep profile.md by default, and use --keep when pruning older snapshots.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckystar513/skills/wdp-ctx-en)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown documents, concise text reports, JSON hook messages, and shell/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project profile and snapshot Markdown files, can export a marked AGENTS.md section, and optional hooks emit prompt-only reminders.]

## Skill Version(s):

1.1.2 (source: ClawHub release evidence and README changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

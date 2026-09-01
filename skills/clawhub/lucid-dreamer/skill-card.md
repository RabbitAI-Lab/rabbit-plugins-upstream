## Description:

Lucid Dreamer helps an AI agent review workspace memory and recent daily notes on a schedule, producing reports and optional memory updates for stale facts, unresolved todos, recurring problems, decisions, contradictions, and cleanup opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to keep long-term memory files current by generating scheduled review reports, tracking suggestions, and optionally applying high-confidence memory changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled runs read USER.md, MEMORY.md, and recent daily notes, which may contain sensitive personal or operational details.

Mitigation: Set CLAWD_DIR explicitly, avoid storing secrets in plaintext markdown, and use the skill only in workspaces whose memory files are appropriate for summarization.

Risk: The security review reports that the nightly prompt can directly edit and commit long-term memory despite documentation saying auto-apply is off by default.

Mitigation: Keep auto-apply and aggressive cleanup disabled unless unattended edits are intended, and review generated reports, diffs, and local commits regularly.

Risk: On OpenClaw 2.0, Lucid's historical 03:00 schedule can collide with the built-in memory sweep and risk conflicting edits to MEMORY.md.

Mitigation: Disable one memory sweep or schedule Lucid at a different time before enabling nightly automation.

## Reference(s):

- [Lucid Dreamer on ClawHub](https://clawhub.ai/robbyczgw-cla/skills/lucid-dreamer)
- [README](README.md)
- [Architecture](ARCHITECTURE.md)
- [Auto-Apply Configuration](config/auto-apply.md)
- [Honcho.dev](https://honcho.dev)
- [Gigabrain](https://github.com/legendaryvibecoder/gigabrain)
- [Nuggets](https://github.com/NeoVertex1/nuggets)
- [ByteRover Context Engine PR](https://github.com/openclaw/openclaw/pull/50848)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown review reports, JSON state, and shell/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces files under the configured workspace path and may propose or apply memory edits depending on configuration.]

## Skill Version(s):

0.8.0 (source: frontmatter, changelog released 2026-08-31, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

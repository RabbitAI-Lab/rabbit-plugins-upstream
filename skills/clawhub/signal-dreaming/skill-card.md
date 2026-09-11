## Description:

Consolidate daily session logs into L2 topic files and a compact MEMORY.md index, in three bounded phases with backups, lifecycle and secret guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lzyling](https://clawhub.ai/user/lzyling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to have an agent consolidate daily Markdown memory logs into durable topic notes, a compact MEMORY.md index, and a dream log while preserving backups and secret handling rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill rewrites MEMORY.md, memory/dream-log.md, and topic files, so the first upgraded consolidation can restructure existing workspace memory.

Mitigation: Run the first 5.0.0 consolidation manually, confirm backups under .backup/memory-dreams, and review the final dream summary before returning it to a schedule.

Risk: Backups may contain local memory content that should not be synced or published.

Mitigation: Keep .backup/memory-dreams out of public archives and sync targets.

Risk: The skill reads daily workspace memory logs and may consult workspace configuration while planning consolidation.

Mitigation: Prefer field-scoped reads or documented defaults instead of loading the full OpenClaw config into context.

## Reference(s):

- [Signal Dreaming full protocol](references/dream-protocol.md)
- [Signal Dreaming audit helper](references/dream-audit.sh)
- [Signal Dreaming version history](references/changelog.md)
- [Signal Dreaming on ClawHub](https://clawhub.ai/lzyling/skills/signal-dreaming)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown file edits, shell command invocations, configuration snippets, and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces updates to workspace memory files and a final dream summary; it does not emit structured machine-readable state.]

## Skill Version(s):

5.0.0 (source: server release metadata and references/changelog.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

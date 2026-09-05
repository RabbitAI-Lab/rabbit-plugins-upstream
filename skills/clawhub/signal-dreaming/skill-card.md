## Description:

Consolidate daily session logs into L2 topic files and a compact MEMORY.md index, in three bounded phases with backups, lifecycle and secret guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lzyling](https://clawhub.ai/user/lzyling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to consolidate Markdown daily logs into durable topic memory and a compact workspace memory index while preserving backups, lifecycle state, and secret-redaction rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill periodically reads and rewrites local workspace memory files.

Mitigation: Use an explicit workspace root, review the allowed write paths, and keep backups enabled before changes to MEMORY.md or L2 topic files.

Risk: Daily logs may contain credentials or sensitive values that should not be promoted into curated memory.

Mitigation: Omit or redact suspected secrets, report the source file for manual review, and use the included filename-only audit helper as a lightweight post-write check.

Risk: Incorrect path selection could modify files outside the intended memory surfaces.

Mitigation: Restrict writes to L2 files, MEMORY.md, memory/dream-log.md, and .backup/memory-dreams/; drop out-of-bounds targets and report them.

## Reference(s):

- [Signal Dreaming Skill Page](https://clawhub.ai/lzyling/skills/signal-dreaming)
- [Signal Dreaming Full Protocol](references/dream-protocol.md)
- [Dream Audit Helper](references/dream-audit.sh)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON cron configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local MEMORY.md, memory/*.md topic files, and memory/dream-log.md updates when followed by an agent.]

## Skill Version(s):

4.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Consolidate daily session logs into L2 topic files and a compact MEMORY.md index, in three bounded phases with backups, lifecycle and secret guards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lzyling](https://clawhub.ai/user/lzyling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to consolidate raw daily Markdown logs into durable topic memory, maintain a compact MEMORY.md index, and record dream-log progress for future runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently rewrites workspace memory, so incorrect consolidation can make stale, inaccurate, or private notes more durable.

Mitigation: Use explicit invocations or tightly scoped scheduled payloads, review the write plan and dream summary, and keep the protocol's required backups before rewrites.

Risk: The audit helper has an environment-variable command-execution weakness when run with untrusted inherited environment variables.

Mitigation: Run the helper only in trusted sessions with controlled environment variables, especially for scheduled runs.

Risk: The protocol only redacts authentication secrets and is not a general privacy classifier.

Mitigation: Apply workspace privacy rules before logs are written, and do not rely on this skill to withhold non-credential private content from memory.

## Reference(s):

- [Signal Dreaming Full Protocol](references/dream-protocol.md)
- [Dream Audit Helper](references/dream-audit.sh)
- [ClawHub Skill Page](https://clawhub.ai/lzyling/skills/signal-dreaming)

## Skill Output:

**Output Type(s):** [markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown memory updates, concise run summaries, and optional shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update MEMORY.md, memory/dream-log.md, memory/<topic>.md, and .backup/memory-dreams/*.bak in the target workspace.]

## Skill Version(s):

4.0.3 (source: server release evidence and SKILL.md version note)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

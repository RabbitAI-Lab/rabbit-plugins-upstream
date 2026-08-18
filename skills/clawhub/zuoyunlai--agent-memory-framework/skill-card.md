## Description:

Provides a three-layer persistent memory framework for agents, including daily notes, long-term memory, and archive rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add persistent local memory to an agent, with rules for initializing memory files, writing daily notes, distilling long-term memory, and archiving stale entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory files may contain personal, sensitive, or regulated information.

Mitigation: Review what is written to MEMORY.md and memory/ before relying on it, and avoid storing secrets or regulated personal data unless that is explicitly intended.

Risk: Private memory may be exposed if loaded in shared or multi-user contexts.

Mitigation: Load long-term and archived memory only in direct private sessions, and avoid reading MEMORY.md or memory/archive/ in shared contexts.

Risk: Optional cron automation can update local memory without active supervision.

Mitigation: Enable cron-based distillation only when unattended local memory updates are acceptable, and review the resulting memory changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/agent-memory-framework)
- [Memory system conventions](artifact/references/conventions.md)
- [Memory distillation workflow](artifact/references/distillation.md)
- [Long-term memory template](artifact/assets/MEMORY.md)
- [Daily memory template](artifact/assets/daily.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration instructions, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with file templates and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local memory structure and operating rules; no external API calls are described.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

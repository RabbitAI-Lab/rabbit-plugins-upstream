## Description:

Self-Evolving Memory helps agents deploy a local-first, layered memory system with safe recording, consolidation, rollback, promotion scoring, indexing, recall planning, and evidence-ledger workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fxbin](https://clawhub.ai/user/fxbin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to initialize, repair, and operate durable local memory for an AI agent. It is intended for workflows such as lightweight memory capture, consolidation, rollback checks, promotion decisions, index maintenance, and verified recall planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to keep durable local memory about a user, the agent's work, and relationship or context data.

Mitigation: Install only when durable memory is desired, review retention behavior, and disable or review scheduled consolidation when automatic profiling or long-term retention is not acceptable.

Risk: Memory files could accidentally contain plaintext credentials or sensitive secrets.

Mitigation: Keep SECRET.md handle-only, store credentials in an external secret store, and use the disclosed secret-scanning and migration workflow before retaining memory files.

Risk: Optional retrieval and scheduling capabilities depend on the host environment and may not be available.

Mitigation: Use the documented manual scheduling path and allowlisted local retrieval fallback when host Calendar, scheduler, or semantic memory search capabilities are absent.

## Reference(s):

- [Server-resolved source repository](https://github.com/fxbin/skills/tree/main/self-evolving-memory)
- [ClawHub skill page](https://clawhub.ai/fxbin/skills/self-evolving-memory)
- [Quick Start Guide](artifact/references/quick-start-guide.md)
- [Deployment Guide](artifact/references/deployment-guide.md)
- [Design Principles](artifact/references/design-principles.md)
- [Positioning](artifact/docs/positioning.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with structured checklists, file templates, JSON examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should keep SECRET.md handle-only, avoid plaintext credentials in memory files, and account for optional host scheduling and retrieval capabilities.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact VERSION is v7.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

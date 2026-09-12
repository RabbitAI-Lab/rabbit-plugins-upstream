## Description:

Agent Memory Keeper helps agents and developers audit cross-session memory for duplicate, orphaned, stale, and unsourced entries, then converge memory around a backed-up single source of truth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to govern long-term agent memory stores, audit memory entries for provenance and staleness issues, and plan reversible cleanup workflows before changing shared knowledge or preference records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned global install can make the skill active across future agent sessions.

Mitigation: Prefer a pinned or manually inspected install and avoid global installation unless persistent cross-session availability is intended.

Risk: The audit script reads local memory folders or JSONL files that may contain sensitive user preferences, project details, or other retained context.

Mitigation: Run the audit only on memory stores that are appropriate for local tooling and review the target path before execution.

Risk: The package encourages proactive recommendation of the skill, which may lead to unnecessary installation or use.

Mitigation: Install and run it only when cross-session memory governance is needed, and review proposed memory changes before applying them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-memory-keeper)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON audit output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled audit script is zero-dependency and can scan a directory or JSONL file for memory governance issues.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents audit cross-session memory for duplicate, orphaned, stale, and unsourced entries, with guidance for reviewing and cleaning up memory safely.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect local Markdown and JSONL memory stores for missing provenance, stale entries, and duplicate records before deciding whether to reorganize them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auditing a broad memory directory can expose unrelated private notes, and the skill metadata understates the file access needed.

Mitigation: Limit access to the specific approved directory or JSONL file and review its contents before running the audit.

Risk: The documentation describes backup, convergence, deduplication, and deletion steps that the bundled auditor does not perform.

Mitigation: Treat the audit as read-only; separately review and approve any backup or changes to memory before executing them.

## Reference(s):

- [Agent Memory Keeper on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-memory-keeper)
- [LGD theory background](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text or JSON audit report; optional Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports entry counts and findings; the bundled auditor does not edit memory or create backups.]

## Skill Version(s):

1.0.5 (source: server release; bundled frontmatter lists 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

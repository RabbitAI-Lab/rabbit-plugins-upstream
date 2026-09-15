## Description:

Find and reclaim what an agent accumulates on disk: oversized sessions, duplicated transcripts, stale embedding caches, abandoned trees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to audit agent storage growth, classify reclaimable disk usage, and plan cautious transcript, cache, database, and workspace cleanup before or during maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintenance steps can lead an agent toward deleting cache entries, transcript data, or abandoned workspace trees.

Mitigation: Limit agent access to the intended storage scope, work from backups or copies for rebuilds, and manually confirm deletion targets before execution.

Risk: Using a database client that cannot see extension-backed or virtual tables can leave derived indexes inconsistent.

Mitigation: Prefer supported agent commands, restrict direct deletes to plain tables with no triggers, and test full rebuilds on a copy first.

Risk: Deleting recently unreferenced cache entries can cause avoidable recomputation or remote provider calls.

Mitigation: Apply a grace window and keep longer retention for remote-provider cache entries.

## Reference(s):

- [Classifying what accumulates](references/classification.md)
- [Worked audit](examples/audit-session.md)
- [ClawHub skill page](https://clawhub.ai/posthuman/skills/agent-storage-maintenance)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, tables, and command-oriented procedures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill emphasizes measurement before deletion, manual confirmation for destructive actions, and before-and-after reporting.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

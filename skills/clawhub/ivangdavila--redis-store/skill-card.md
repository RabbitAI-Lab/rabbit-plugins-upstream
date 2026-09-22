## Description:

Designs, tunes, and debugs Redis data structures, memory limits, persistence, Streams and queues, locks, replication, cluster behavior, and redis-cli diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design Redis-backed features, produce Redis commands and client examples, diagnose incidents, tune memory and persistence settings, and plan migrations or cluster operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Redis commands may affect live production data or availability, especially SCAN plus UNLINK, FLUSH, CONFIG SET, SHUTDOWN, failover, or script-cache commands.

Mitigation: Review commands before execution, require explicit destructive confirmation, and rehearse high-impact operations on staging or restored copies when practical.

Risk: Live redis-cli diagnostics can expose operational details or secrets through command arguments, key names, logs, backups, or local notes.

Mitigation: Use secret-safe connection methods, avoid putting credentials in command lines or key names, and review locally stored Redis context under ~/Clawic/data/redis-store/.

Risk: Guidance that changes memory, eviction, persistence, or cluster settings can trade correctness, durability, and latency against each other.

Mitigation: Measure current Redis state first, preserve backups or rollback paths, and match changes to the declared workload and data-loss budget.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/redis-store)
- [Redis Skill Source](artifact/SKILL.md)
- [Setup and Local Preferences](artifact/setup.md)
- [Redis Security Guide](artifact/security.md)
- [redis-cli Forensics Guide](artifact/cli.md)
- [Memory, Eviction, and Big Keys](artifact/memory-eviction.md)
- [Persistence, Backups, and Restores](artifact/persistence.md)
- [Cluster Operations](artifact/cluster.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Redis commands, shell commands, client code snippets, configuration examples, and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use redis-cli for live diagnostics and may store Redis-related preferences or observed context under ~/Clawic/data/redis-store/.]

## Skill Version(s):

1.0.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

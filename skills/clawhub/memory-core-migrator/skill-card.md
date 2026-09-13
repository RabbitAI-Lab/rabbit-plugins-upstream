## Description:

Safely migrates OpenClaw memory from LanceDB Pro, official LanceDB list captures, QMD, or Markdown into memory-core.

This skill is ready for commercial/non-commercial use.

## Publisher:

[airbing11](https://clawhub.ai/user/airbing11)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use this skill to plan, audit, stage, and review memory migrations into memory-core while preserving rollback evidence and requiring explicit approvals for production changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory exports, backups, run state, reports, and staged Markdown may contain sensitive personal data or credentials.

Mitigation: Keep run directories outside indexed memory paths, treat all generated evidence as production-sensitive, and do not publish logs or fixtures containing real memory, credentials, channel IDs, or personal data.

Risk: A memory cutover can lose access to source facts or make rollback harder if performed without a verified backup and stable environment identity.

Mitigation: Require a verified backup, count/hash reconciliation, frozen recall baseline, source recoverability, drift checks, and a fresh run-bound approval before any cutover, rollback, promotion, or retirement action.

Risk: Direct database parsing, vector copying, or automatic deletion can corrupt memory semantics or remove needed evidence.

Mitigation: Use supported export or Markdown paths, rebuild derived indexes in memory-core, report duplicates without deleting automatically, and never write directly to memory-core SQLite internals.

Risk: Unsupported source schemas or changed CLI capabilities can produce incomplete migrations.

Mitigation: Detect installed capabilities, fail closed on unknown schemas, reconcile scoped export totals against fresh stats, and stop on count, ID, hash, scope, agent, configuration, or capability drift.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/airbing11/skills/memory-core-migrator)
- [Compatibility policy](references/compatibility.md)
- [Operations and rollback](references/operations.md)
- [Recall benchmark methodology](docs/benchmark-methodology.md)
- [Security policy](SECURITY.md)
- [memory-lancedb-pro CLI reference](https://github.com/CortexReach/memory-lancedb-pro/blob/63495671fde55f2c8e3d6eb95267381d1889cca9/cli.ts#L649-L1034)
- [OpenClaw memory-lancedb CLI reference](https://github.com/openclaw/openclaw/blob/1391f7cd2d40ab5bbcf2f5f831d3a64f520e72d7/extensions/memory-lancedb/memory-cli.ts#L107-L233)
- [QMD CLI reference](https://github.com/tobi/qmd/blob/facd35e01359e59d938bc9418e93fb9318addee3/src/cli/qmd.ts#L3567-L3601)
- [OpenClaw retired-QMD migration reference](https://github.com/openclaw/openclaw/blob/1391f7cd2d40ab5bbcf2f5f831d3a64f520e72d7/src/commands/doctor/shared/legacy-config-migrations.runtime.retired-memory-qmd.ts#L92-L205)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, markdown, files]

**Output Format:** [Markdown guidance with inline shell commands; CLI outputs include JSONL, JSON reports, staged Markdown, and run evidence files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are local-first and safety-gated; production changes require verified backups, drift checks, and run-bound approvals.]

## Skill Version(s):

0.1.0-rc.1 (source: package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

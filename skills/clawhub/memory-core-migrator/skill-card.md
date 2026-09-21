## Description:

Safely migrates OpenClaw memory from LanceDB Pro, official LanceDB list captures, QMD, or Markdown into memory-core.

This skill is ready for commercial/non-commercial use.

## Publisher:

[airbing11](https://clawhub.ai/user/airbing11)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to plan, audit, stage, benchmark, cut over, and roll back OpenClaw memory migrations into memory-core while preserving evidence and review gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive memory exports, reports, backups, logs, and staged memory files.

Mitigation: Protect the run directory as sensitive, keep outputs outside indexed memory paths, and avoid publishing memory text, credentials, channel IDs, private paths, or personal data.

Risk: Migration inputs or outputs can be incomplete, drift from the source, or produce misleading audit conclusions.

Mitigation: Use copied exports and dry-runs first, require count and ID reconciliation, inspect approximate-audit completeness, and stop on count, hash, capability, configuration, agent, or scope drift.

Risk: Production cutover, promotion, retirement, or rollback can affect the live memory backend.

Mitigation: Require verified backups and run-bound approvals before production actions, keep rollback artifacts, and preserve source data during the rollback window.

Risk: Secret-like metadata redaction does not guarantee that secrets embedded in memory text are removed.

Mitigation: Review exports and staged Markdown before sharing or indexing, and treat generated artifacts as potentially sensitive even after metadata redaction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/airbing11/skills/memory-core-migrator)
- [README](README.md)
- [Security policy](SECURITY.md)
- [Compatibility policy](references/compatibility.md)
- [Operations and rollback](references/operations.md)
- [Recall benchmark methodology](docs/benchmark-methodology.md)
- [Operator recipes](docs/recipes.md)
- [Anonymized dogfood evidence - 2026-09-18](docs/dogfood-2026-09-18.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and generated migration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first output; reports and staged memory artifacts may contain sensitive memory data and should remain outside indexed memory paths.]

## Skill Version(s):

0.1.0-rc.2 (source: CHANGELOG, package.json, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

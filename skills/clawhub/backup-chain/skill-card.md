## Description:

Helps agents create, verify, and restore hash-chained workspace backups with restore drills, an append-only ledger, and optional custody tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[darkd](https://clawhub.ai/user/darkd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to maintain recoverable backups of valuable project files, verify archive integrity, and safely restore after resets or data loss.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backups may include credentials or other sensitive workspace files.

Mitigation: Review the member list and .vault/config.json before building; keep sensitive archives private.

Risk: Optional command adapters and restore overrides can execute user-supplied commands or overwrite files.

Mitigation: Use --allow-cmd-ledger, --stow-cmd, --overwrite, and --force only after reviewing their effects and intended paths.

Risk: A ledger stored alongside a lost workspace may not preserve backup history after a wipe.

Mitigation: Keep the append-only ledger outside the workspace failure domain, and review --allow-external-ledger before using an external path.

## Reference(s):

- [ClawHub backup-chain release](https://clawhub.ai/darkd/skills/backup-chain)
- [Backup protocol](references/PROTOCOL.md)
- [Security guidance](references/SECURITY.md)
- [Residual risks](references/RESIDUAL_RISK.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and JSON check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands creates backup archives, hash receipts, and ledger records.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

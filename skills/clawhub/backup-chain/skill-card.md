## Description:

Creates hash-chained workspace backups with restore drills, ledger-based fencing, and verified recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[darkd](https://clawhub.ai/user/darkd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to back up workspaces, verify archive integrity, and safely restore work after a crash, wipe, or rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backups can contain sensitive workspace files.

Mitigation: Review the member list and configuration; exclude secrets unless archives are stored privately.

Risk: Restores can replace files at the chosen target.

Mitigation: Verify the archive and review the restore target before applying a restore.

Risk: Opt-in ledger commands or external ledger destinations can access resources outside the workspace.

Mitigation: Review configured commands and destinations before using --allow-cmd-ledger or --allow-external-ledger.

## Reference(s):

- [Backup Chain on ClawHub](https://clawhub.ai/darkd/skills/backup-chain)
- [Backup protocol](artifact/references/PROTOCOL.md)
- [Security guidance](artifact/references/SECURITY.md)
- [Residual risks](artifact/references/RESIDUAL_RISK.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Recovery guidance]

**Output Format:** [Markdown with shell commands and JSON status checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Backup archives and SHA-256 receipts are generated when commands run.]

## Skill Version(s):

1.1.1 (source: ClawHub release, skill heading, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

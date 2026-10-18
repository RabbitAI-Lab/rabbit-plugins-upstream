## Description:

Plans and copies a PikPak folder tree into a new local directory without overwriting files, checks downloaded sizes, and creates a local SHA-256 manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can plan an authorized folder download, review its scope, and copy files to a new local directory with a size-checked manifest. The skill is a one-time copy helper, not a versioned or resumable backup system.

### Deployment Geography for Use:

Global; instructions are primarily in Simplified Chinese.

## Known Risks and Mitigations:

Risk: Access to an authenticated PikPak account and unintended downloads.

Mitigation: Use only with an authorized account, review a dry-run plan first, and confirm the destination and scope before downloading.

Risk: Writing into an occupied destination or running an untrusted local executable.

Mitigation: Choose a new empty destination and run only where the operator controls the Python interpreter, script, PATH, and PIKPAK_BIN; avoid untrusted CI and multi-user launchers.

Risk: Mistaking a local checksum or size match for verified remote integrity or a recoverable backup.

Mitigation: Treat the manifest as a local baseline only; independently verify remote content when needed and do not rely on this tool for incremental, resumable, or versioned backups.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-batch-backup)
- [Backup design and verification boundaries](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and commands; optional JSON reports and backup manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloaded files are published only after size checks; local SHA-256 values do not verify remote content.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps users plan and run a one-pass PikPak folder download into a new local backup directory without overwriting files, with size checks and a local SHA-256 manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and developers use this skill to review a folder download plan and copy its files into a new local directory. It reports size-checked downloads and records local SHA-256 hashes without claiming remote content verification or incremental backup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A substituted local PikPak CLI could run unintended commands or access account data.

Mitigation: Run with a trusted PATH and PIKPAK_BIN controlled by the operator.

Risk: A download can write local files and consume disk space; existing files should not be overwritten.

Mitigation: Review the dry-run plan and capacity, then choose a new empty backup directory.

Risk: The backup manifest contains file names and IDs.

Mitigation: Keep the manifest private and limit access to the backup directory.

Risk: Size checks and local SHA-256 hashes do not establish that downloaded bytes match the remote content.

Mitigation: Treat remote integrity as unverified; use separate remote hash verification where required.

Risk: Registration guidance includes a disclosed referral code that may reward the sharer.

Mitigation: Choose whether to use the referral code before registering; declining it does not affect this skill.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pipiguai87-alt/skills/pikpak-batch-backup)
- [Backup design and limitations](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Text guidance and shell commands; local backup files and a JSON manifest when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an existing empty destination for downloads; the manifest records file IDs, paths, sizes, statuses, and local SHA-256 hashes, not verified remote hashes.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

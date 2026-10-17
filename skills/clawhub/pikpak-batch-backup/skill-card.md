## Description:

Helps users plan and copy a PikPak folder tree into a new local directory without overwriting files, checks downloaded sizes, and creates a local SHA-256 manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and developers can preview a folder's download plan and, after approval, copy its files to a new local backup directory with a manifest for later local integrity checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloading the wrong folder or writing into an existing directory can produce an incomplete or conflicting copy.

Mitigation: Review the dry-run plan first, confirm the folder and capacity, and use a new empty destination directory.

Risk: The backup manifest contains private file names and paths; local hashes do not prove the downloaded bytes match the remote content.

Mitigation: Keep the manifest private and treat size checks and local SHA-256 hashes as local checks, not remote integrity verification.

Risk: An untrusted override of the PikPak executable can run unwanted code.

Mitigation: Set PIKPAK_BIN only to a trusted PikPak executable if an override is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-batch-backup)
- [Design and verification boundaries](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Text guidance and CLI output; local backup files and a JSON manifest when downloads are authorized]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The manifest records file paths, sizes, status, and local SHA-256 hashes; remote content integrity is unverified.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

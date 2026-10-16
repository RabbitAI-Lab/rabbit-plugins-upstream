## Description:

Helps users back up their PikPak cloud files to a local folder, with resumable downloads and a backup manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users can back up selected cloud folders or files to a local drive, inspect a dry-run plan, and check download outcomes in a manifest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A backup may download more cloud data than intended or fill the destination drive.

Mitigation: Use a logged-in PikPak account for your own files, run a dry-run first, and confirm the destination has enough space.

Risk: The backup manifest can expose private file names and paths.

Mitigation: Keep backup_manifest.json private and review it before sharing.

## Reference(s):

- [PikPak Batch Backup on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-batch-backup)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON files]

**Output Format:** [Text instructions and a JSON backup manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run previews planned downloads; completed backups record file paths, sizes, and download statuses.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

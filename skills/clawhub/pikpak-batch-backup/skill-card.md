## Description:

Creates a one-time PikPak folder backup plan and copies files to a new local directory without overwriting existing data, checks file sizes, and writes a local SHA-256 manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to plan and perform a one-time backup of a PikPak folder to local storage. It checks downloaded file sizes and creates a local checksum manifest while making clear that these checks do not verify content against the cloud copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An online dry run still accesses the PikPak account, and downloads may be subject to connected-app limits.

Mitigation: Use a trusted PikPak CLI, authorize account access, and review the dry-run plan and applicable quota before downloading.

Risk: Existing destination contents are not overwritten, and unsupported filesystems or insufficient space can prevent a backup.

Mitigation: Choose a new private destination with sufficient space on a supported POSIX filesystem.

Risk: Size checks and local SHA-256 values do not prove that downloaded content matches the cloud copy; resume and incremental backups are unsupported.

Mitigation: Treat this as a one-pass backup, use the manifest only as a local reference, and plan a fresh backup in a new directory when needed.

## Reference(s):

- [Upstream Design Notes](references/upstream-design.md)
- [PikPak connected-app speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [PikPak connected-app transfer quota](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Shell commands and a JSON backup manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-pass backup that refuses to overwrite existing files; verifies size and records a local SHA-256, but does not provide incremental sync, resume, or remote content verification.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

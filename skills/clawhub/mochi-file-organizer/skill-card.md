## Description:

Create a read-only file classification plan and SHA256 duplicate report for an explicitly named local folder. Use for 文件整理, reviewing Downloads, or finding duplicate files before deciding how to organize them. It does not move or delete files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use this skill to inspect an explicitly selected local folder, review an extension-based organization plan, and identify files with matching sizes and SHA256 hashes before making any separate file-management decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports expose file names, local paths, sizes, and hashes, and excerpts may be sent to the configured model.

Mitigation: Scan only a specifically chosen folder, keep reports private, and use an approved local model if excerpts must remain on-device.

Risk: Matching size and SHA256 values identify duplicate candidates but do not establish that a file is safe to remove.

Mitigation: Review duplicate groups and relevant backups or application references; handle any later deletion as a separate task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hznetnewpower/skills/mochi-file-organizer)
- [MochiLab homepage](https://mochilab.bz)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [plan.json and report.md containing a proposed classification, file sizes, SHA256 hashes, duplicate groups, and skipped paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only plan; does not move or delete source files. Reports include local paths and hashes.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata, README)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

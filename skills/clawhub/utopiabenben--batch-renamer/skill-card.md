## Description:

Batch Renamer helps agents guide bulk file-renaming workflows using sequence, date, template, regex, preview, and undo patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[utopiabenben](https://clawhub.ai/user/utopiabenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to plan and run bulk renaming for photos, documents, downloads, and other file collections with preview and undo guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File moves or renames could corrupt or displace files outside the intended working set.

Mitigation: Run the included Python script in a test directory first, use preview before applying changes, and verify the target directory and generated rename mapping.

Risk: Global npm or pip install commands are not backed by verified package ownership, versions, or source linkage in the evidence.

Mitigation: Prefer running only the included Python script unless the publisher provides verifiable package ownership, pinned versions, and source provenance.

Risk: A tampered backup file could affect undo behavior and move or restore files incorrectly.

Mitigation: Keep backups protected from shared or attacker-writable directories and inspect the backup mapping before undoing in sensitive directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/utopiabenben/skills/batch-renamer)
- [README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include preview-first workflows, rename patterns, regex substitutions, and undo instructions.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

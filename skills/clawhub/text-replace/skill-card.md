## Description:

text-replace helps agents perform bulk literal or regex search-and-replace across files, with dry-run previews by default, optional JSON output, and .bak backups before applying changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to preview and apply repeated text changes such as renames, version updates, or endpoint replacements across file sets. It is intended for user-directed file maintenance where dry-run review and backup files reduce accidental edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Applying a broad replacement can modify more files or occurrences than intended.

Mitigation: Run the default dry-run first, keep glob patterns narrow, and review results before using --apply.

Risk: Mutable branch or unpinned installer commands can fetch changed code after review.

Mitigation: Install from a reviewed commit or release.

Risk: Applied replacements write to local files.

Mitigation: Use the generated .bak backups when reviewing or reverting important file changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/text-replace)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default dry-run previews; --apply writes files and creates .bak backups; --json returns machine-readable results.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

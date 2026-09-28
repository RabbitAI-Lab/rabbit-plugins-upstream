## Description:

Finds and replaces literal or regex text across files, previewing matches by default and creating .bak backups before changes are applied.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only; documentation and methodology all rights reserved)

## Use Case:

Developers and other users can preview and apply bulk text replacements across selected files when renaming identifiers, updating versions, or changing addresses. Review the match scope and replacement values before applying edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overly broad file pattern or replacement can change unintended text when --apply is used.

Mitigation: Preview matches first, inspect the exact --glob, --old, and --new values, and keep version control or separate backups for important files.

Risk: Applying changes creates .bak files alongside modified files.

Mitigation: Review backup files before sharing or committing the edited directory.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/text-replace)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Shell commands, Text, JSON]

**Output Format:** [Text or JSON match counts and per-file details; optional shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run by default; --apply writes changes and creates .bak files beside modified files.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents preview and perform rule-based batch file renaming with prefixes, suffixes, numbering, find-and-replace, and extension filtering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and other users can standardize filenames in a chosen directory, preview proposed changes, and apply approved renaming rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can rename local files with --apply, although its permissions metadata understates file access.

Mitigation: Review the dry-run plan first, restrict --dir to the intended folder, and back up important files before applying changes.

## Reference(s):

- [ClawHub batch-renamer release](https://clawhub.ai/zhaoxinghua09-cell/skills/batch-renamer)
- [LGD theory (background referenced in README)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Shell commands, Text, JSON]

**Output Format:** [CLI guidance and plain-text or JSON rename plans and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview by default; applying changes requires --apply.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

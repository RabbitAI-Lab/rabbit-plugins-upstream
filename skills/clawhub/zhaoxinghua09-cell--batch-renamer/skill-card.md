## Description:

Batch Renamer helps agents plan and run rule-based bulk file renames with prefixes, suffixes, sequence numbers, find-and-replace rules, extension filters, dry-run previews, and optional JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, operations staff, and agent users can use this skill to preview and execute repeatable file-renaming chores across local directories. It is most useful when a batch of files needs consistent naming changes before manual review or downstream processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crafted rename patterns can move or overwrite files outside the intended directory.

Mitigation: Use backed-up directories, inspect dry-run output, avoid slashes, backslashes, absolute paths, and .. components, and run with --apply only after review.

Risk: An unpinned global npx install can fetch a remote package version that differs from the reviewed artifact.

Mitigation: Install a reviewed release when possible, verify source and hashes before global installation, and prefer local artifact inspection for sensitive use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/batch-renamer)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run is the default; file changes require the --apply flag.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest; SKILL.md frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

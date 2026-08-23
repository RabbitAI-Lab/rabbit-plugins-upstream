## Description:

Batch rename files with pattern substitution, prefix and suffix addition, sequential numbering, case conversion, extension changes, dry-run previews, rename logs, and undo support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and other external users can use this skill to standardize groups of filenames, add sequence numbers, change case or extensions, and generate undoable rename operations. Users should preview with --dry-run before performing real renames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that the skill falsely says dry-run is the default while the script performs real renames unless --dry-run is explicitly requested.

Mitigation: Run with --dry-run first, test on a small copied directory, and review the proposed rename list before running a real rename.

Risk: Batch rename operations can unintentionally change many files when the target directory, glob, or rename pattern is wrong.

Mitigation: Use an explicit --dir path, narrow the --glob pattern where possible, preserve the generated rename log, and use undo promptly if the result is incorrect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/batch-file-rename)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in filesystem rename operations and generated rename logs when the script is executed.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

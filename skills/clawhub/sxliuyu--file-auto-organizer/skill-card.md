## Description:

File Auto Organizer helps an agent organize local folders by file type or modification date and report folder statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sxliuyu](https://clawhub.ai/user/sxliuyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a Python command-line organizer on folders such as Downloads or Desktop, grouping files by type or date and optionally showing a report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The organizer can move user files without preview or confirmation.

Mitigation: Run it first on a copied or disposable folder, verify the target path before execution, and avoid important directories until preview or dry-run behavior is available.

Risk: Existing files with colliding names may be overwritten or moved unexpectedly.

Mitigation: Back up the target folder before use and manually review duplicate filenames before organizing production or important files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sxliuyu/skills/file-auto-organizer)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Markdown with inline bash commands and command-line text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May move files on disk; optional reports summarize moved files or folder statistics.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

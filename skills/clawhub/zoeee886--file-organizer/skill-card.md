## Description:

Sort and organize files in a directory by type or by modification date, with dry-run preview, duplicate-name handling, and an auto-generated organization report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zoeee886](https://clawhub.ai/user/zoeee886)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to preview and reorganize loose local files into type-based or date-based folders, then produce a Markdown report of the completed organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can move local files in a selected directory.

Mitigation: Use the dry-run preview first, confirm the exact target directory, and avoid important folders unless a backup exists.

Risk: Recursive organization can affect files in subfolders and failures could leave some files already moved.

Mitigation: Use recursion only when the user explicitly wants subfolders included, and review the dry-run plan before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zoeee886/skills/file-organizer)
- [Server-Resolved GitHub Source](https://github.com/zoeee886/clawhub-skills/tree/main/file-organizer)
- [Examples](examples.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown guidance with PowerShell commands and generated organize-report.md files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PowerShell; supports dry-run preview, by-type or by-date organization, optional recursion, and duplicate-name handling.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

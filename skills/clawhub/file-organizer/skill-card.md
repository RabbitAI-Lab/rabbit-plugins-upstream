## Description:

Sort and organize files in a directory by type or by modification date, with dry-run preview, duplicate-name handling, and an auto-generated organization report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zoeee886](https://clawhub.ai/user/zoeee886)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and workspace maintainers use this skill to preview and organize loose files in a selected directory by type or modification date, then create a concise organization report after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Files may be moved into unintended folders if the target directory or grouping mode is wrong.

Mitigation: Use the dry-run preview first, confirm the exact target directory and planned moves, and execute only after user approval.

Risk: Recursive organization can affect files in subfolders beyond the intended scope.

Mitigation: Avoid recursive mode unless the user explicitly requests it and review the planned subfolder moves before approval.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/zoeee886/clawhub-skills/tree/main/file-organizer)
- [ClawHub skill page](https://clawhub.ai/zoeee886/skills/file-organizer)
- [Examples](examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with PowerShell command blocks, preview text, and an organization report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PowerShell; file moves are preceded by dry-run planning and explicit confirmation.]

## Skill Version(s):

0.1.1 (source: release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

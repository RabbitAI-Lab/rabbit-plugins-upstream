## Description:

Organize messy folders by moving files into subfolders grouped by extension, date, or category.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dwzhjt](https://clawhub.ai/user/dwzhjt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to preview and organize messy local folders into subfolders by type, extension, or modification date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Moving files changes paths and may break shortcuts, scripts, configs, or project references.

Mitigation: Review the dry-run output before approval and avoid running on path-sensitive folders unless the moved paths are acceptable.

Risk: Files with missing or incorrect extensions can be grouped into unexpected folders.

Mitigation: Use dry-run output to inspect planned destinations and choose type, extension, or date grouping based on the folder contents.

Risk: Large folder reorganizations can be difficult to inspect and reverse.

Mitigation: Organize large folders in smaller batches and report the script summary after each run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dwzhjt/skills/file-organize-test)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and plain-text move summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports one line per planned or executed move and a final summary.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

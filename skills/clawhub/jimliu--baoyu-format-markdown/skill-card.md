## Description:

Formats plain text or markdown files with frontmatter, titles, summaries, headings, bold, lists, and code blocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimliu](https://clawhub.ai/user/jimliu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and content editors use this skill to improve the structure and readability of plain text or markdown articles while preserving the original content. It can add frontmatter, titles, summaries, headings, bold emphasis, lists, code blocks, and typography fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may overwrite existing formatted output files or modify the original file in typography-only mode.

Mitigation: Use it in a limited workspace, keep backups of source documents, and review generated files before replacing originals.

Risk: The typography workflow may fetch or execute npm packages at runtime.

Mitigation: Pin or preinstall required tools such as bun, npx, and npm dependencies before using the skill on sensitive content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jimliu/skills/baoyu-format-markdown)
- [Homepage](https://github.com/JimLiu/baoyu-skills#baoyu-format-markdown)
- [Title Formulas Reference](references/title-formulas.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown files and concise completion reports with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create an analysis file and a formatted markdown file; typography-only mode may modify the original file.]

## Skill Version(s):

1.117.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

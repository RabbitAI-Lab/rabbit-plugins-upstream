## Description:

Convert Markdown text to DOCX, PPTX, XLSX, PDF, PNG, SVG, HTML, IPYNB, MD, CSV, JSON, JSONL, XML files, and extract code blocks in Markdown to Python, Bash, JS, and other file types.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowenliang123](https://clawhub.ai/user/bowenliang123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to convert Markdown files into document, spreadsheet, presentation, web, image, notebook, and data formats, or to extract fenced code blocks into files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Markdown conversion commands write files to user-provided output paths and code-block extraction can create multiple files or a ZIP archive.

Mitigation: Run conversions only in a user-approved working directory and check output paths before executing generated commands.

Risk: Installing the required markdown-exporter CLI package introduces ordinary third-party package supply-chain risk.

Mitigation: Install only from the expected publisher or source and prefer a pinned or reviewed md-exporter version when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowenliang123/skills/markdown-exporter)
- [Project homepage](https://github.com/bowenliang123/markdown-exporter)
- [Pandoc slide show documentation](https://pandoc.org/MANUAL.html#slide-shows)
- [Markdown Guide: tables](https://www.markdownguide.org/extended-syntax/#tables)
- [Markdown Guide: fenced code blocks](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with command-line examples and file output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of a CLI that reads Markdown file paths and writes converted files or extracted code artifacts.]

## Skill Version(s):

4.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

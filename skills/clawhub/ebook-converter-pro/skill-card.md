## Description:

Ebook Converter Pro helps agents convert and organize EPUB, PDF, MOBI, AZW3, and FB2 ebooks into text, Markdown, HTML, JSON, or image outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

Developers and knowledge workers use this skill to generate and run local ebook conversion workflows, extract metadata and covers, and organize ebook libraries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local ebook directories and writes converted files, reports, copied books, or symlinks, so an imprecise path can affect unintended files.

Mitigation: Use explicit input and output directories, prefer dry-run for library organization, and review commands before OCR, split or merge, metadata edit, and recursive batch operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/ebook-converter-pro)
- [Publisher profile](https://clawhub.ai/user/xuan905)
- [Server-resolved GitHub repository](https://github.com/xuan905/ebook-converter-pro)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated local text, Markdown, HTML, JSON, image, BibTeX, and report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file outputs depend on the selected converter, input ebook format, output directory, and optional OCR, batch, metadata, or organization flags.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

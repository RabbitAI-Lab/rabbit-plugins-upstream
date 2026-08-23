## Description:

Analyzes Word, PDF, and PowerPoint documents by extracting full text, tables, formatting, charts, and image-based content for cross-document summaries and calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and document analysts use this skill to parse and analyze .doc, .docx, .pdf, .ppt, and .pptx files, including multi-file document sets. It supports extraction of text, tables, numeric values, formatting signals, charts, and image-only content for structured answers and summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive document content may be read from selected files, rendered to temporary local images, or passed to the referenced captioning helper for image-based pages and embedded visuals.

Mitigation: Use only with documents approved for this processing path, confirm the captioning helper's data handling before use, and remove temporary rendered files after analysis.

Risk: Tables, charts, OCR-like captioning, and unit-sensitive calculations can produce incorrect or misleading extracted values.

Mitigation: Follow the skill's full-scan workflow, inspect sample rows or pages, print intermediate calculation values, and preserve source units in final answers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sensenova-skills/skills/sn-da-non-spreadsheet-analysis)
- [Main document analysis workflow](artifact/SKILL.md)
- [PDF analysis capability](artifact/capability/pdf-analysis/SKILL.md)
- [PowerPoint analysis capability](artifact/capability/ppt-analysis/SKILL.md)
- [Word analysis capability](artifact/capability/word-analysis/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with extracted text, tables, calculations, and inline Python or shell command snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May render document pages, slides, or embedded images to temporary local files for captioning when source content is image-based.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

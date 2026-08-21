## Description:

Advanced PDF tool for text and table extraction, PDF creation, merge and split operations, forms, OCR, PDF-to-Markdown conversion, batch folder processing, and automatic AI document summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to help agents process local PDF documents: extracting text and tables, converting PDFs to Markdown, batching folder workflows, merging PDFs, and generating document summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF processing can expose local document contents to the agent during text extraction, conversion, batch processing, and summarization.

Mitigation: Use explicit input files or folders and process only PDFs that the agent is allowed to read.

Risk: Conversion, merge, and batch commands can create or overwrite output files at user-selected paths.

Mitigation: Choose output paths carefully and review generated files before relying on or sharing them.

## Reference(s):

- [ClawPDF Master on ClawHub](https://clawhub.ai/northcap-group/skills/clawpdf-master)
- [northcap-group publisher profile](https://clawhub.ai/user/northcap-group)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell command examples; scripts can produce text files, Markdown files, PDF files, and summary Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, pdftotext, and qpdf for disclosed PDF workflows; optional PDF libraries may be needed for specific operations.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

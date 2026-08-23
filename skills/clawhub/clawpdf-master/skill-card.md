## Description:

Advanced PDF tool for text and table extraction, PDF creation, merge and split operations, forms, OCR, PDF-to-Markdown conversion, batch folder processing, and automatic document summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to extract, transform, summarize, merge, split, and generate PDF content from local documents. It is useful for document review workflows where PDFs need to become text, Markdown, summaries, or combined output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local PDF files and may write extracted, converted, merged, summary, or decrypted outputs.

Mitigation: Run it only on PDFs and folders you intend to process, keep outputs in dedicated directories, and protect extracted or decrypted document contents.

Risk: Batch operations can create or overwrite many output files.

Mitigation: Use a separate output folder for batch work and check target paths before running merge, extraction, or conversion commands.

## Reference(s):

- [ClawPDF Master skill page](https://clawhub.ai/northcap-group/skills/clawpdf-master)
- [Northcap Group publisher profile](https://clawhub.ai/user/northcap-group)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with Python and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write extracted text, Markdown conversions, summaries, merged PDFs, split PDFs, or decrypted PDF outputs to local files.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

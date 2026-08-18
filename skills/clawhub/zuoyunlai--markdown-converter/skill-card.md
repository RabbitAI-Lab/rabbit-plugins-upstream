## Description:

Convert documents and files to Markdown using markitdown. Use when converting PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx, .xls), HTML, CSV, JSON, XML, images (with EXIF/OCR), audio (with transcription), ZIP archives, YouTube URLs, or EPubs to Markdown format for LLM processing or text analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert documents, web/data files, media files, archives, and URLs into Markdown for LLM processing or text analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using Azure Document Intelligence can upload document contents to Azure.

Mitigation: Use local conversion by default, and only enable Azure extraction after confirming the document is safe to upload and not sensitive or restricted by policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/markdown-converter)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for invoking markitdown; converted content is emitted as Markdown.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

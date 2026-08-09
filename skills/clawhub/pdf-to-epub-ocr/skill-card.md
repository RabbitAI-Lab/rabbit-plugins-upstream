## Description:

Converts scanned PDF ebooks into structured, reflowable EPUB files using OCR, text cleanup, chapter detection, cover extraction, and metadata handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erich1566](https://clawhub.ai/user/erich1566)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to convert scanned PDF books into mobile-readable EPUB files, including OCR extraction, chapter structuring, EPUB generation, and conversion reporting. It is intended for scanned PDFs that lack a usable text layer, not ordinary text PDFs or general PDF editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pinned vulnerable PDF and image-processing dependencies may increase exposure when processing malicious or untrusted PDFs.

Mitigation: Review and update dependency pins before installation, run conversion in an isolated workspace, and process only trusted PDFs unless resource limits and dependency updates are applied.

Risk: Extracted page images, logs, cover files, OCR text, EPUB files, and conversion artifacts may remain in the local output or work directory.

Mitigation: Avoid confidential documents unless local artifact retention is acceptable, and delete work/output directories after review when sensitive content is processed.

Risk: OCR recognition and cleanup can alter or omit source content.

Mitigation: Review the generated EPUB and conversion report against the source PDF, especially for low-quality scans, technical content, and metadata-sensitive books.

## Reference(s):

- [Server-resolved source repository](https://github.com/Erich1566/pdf-to-epub-ocr)
- [ClawHub skill page](https://clawhub.ai/erich1566/skills/pdf-to-epub-ocr)
- [OCR Best Practices](references/ocr_best_practices.md)
- [Chapter Patterns](references/chapter_patterns.md)
- [EPUB Structure Guide](references/epub_structure_guide.md)
- [Tesseract language data](https://github.com/tesseract-ocr/tessdata/raw/main/chi_sim.traineddata)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [EPUB files, Markdown conversion reports, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local output and work directories containing generated EPUBs, logs, extracted images, cover files, and OCR text.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Extracts text, numbers, and math expressions from images and scanned PDFs using local OCR, with optional language-model downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers use this skill to convert text in photos, worksheets, and scanned PDF pages into editable text for reading or reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic language-model downloads can access the network despite the offline claim.

Mitigation: Use --no-auto-download and preinstall or hash-verify required language models when offline handling matters.

Risk: Extracted text is cached on disk, including potentially sensitive document content.

Mitigation: Avoid sensitive documents unless local text caching is acceptable, and review local cache handling before use.

Risk: OCR can misread handwriting, blurry images, and low-resolution scans.

Mitigation: Review low-confidence lines against the originals rather than assuming unreadable text is correct.

## Reference(s):

- [ClawHub image-ocr release](https://clawhub.ai/lisong2003-lgtm/skills/image-ocr)
- [Tesseract tessdata_fast language models](https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV]

**Output Format:** [Plain text, Markdown table, JSON, or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional file output; low-confidence text is flagged for review.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

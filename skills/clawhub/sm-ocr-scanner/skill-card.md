## Description:

Perform OCR on image files (jpg, png, bmp, gif, tiff) using the system's `tesseract` binary and return extracted plain text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kaarl92](https://clawhub.ai/user/kaarl92)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to extract plain text from image files through local Tesseract OCR. The artifact also includes an optional remote OCR helper, so users handling sensitive documents should prefer the local shell wrapper unless remote processing is intended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Python helper can upload local images to OCR.space even though the main description presents the skill as local-only.

Mitigation: Use the local Tesseract shell script for sensitive documents, and use the Python helper only when remote processing is intentional and acceptable.

Risk: The documented behavior omits remote processing, URL support, PDF support, and related privacy implications.

Mitigation: Review the scripts before installation and require the publisher to document or remove behavior that changes where files are processed.

## Reference(s):

- [Skill page](https://clawhub.ai/kaarl92/skills/sm-ocr-scanner)
- [OCR API Reference](references/api_reference.md)
- [OCR.space API](https://api.ocr.space/parse/image)
- [OCR.space API documentation](https://ocr.space/ocrapi)

## Skill Output:

**Output Type(s):** [text, shell commands, code, guidance]

**Output Format:** [Plain text OCR output, Markdown guidance, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local OCR uses Tesseract with English language settings by default; PDF handling depends on pdftoppm.]

## Skill Version(s):

1.1.0 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

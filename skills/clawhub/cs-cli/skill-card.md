## Description:

CamScanner helps agents process image, PDF, TXT, and Markdown documents with camscanner-cli for OCR, conversion, enhancement, watermarking, translation, merging, detection, and image text editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[camscanner-ai](https://clawhub.ai/user/camscanner-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill through an agent to route document-processing requests to CamScanner CLI commands. It helps convert, OCR, enhance, translate, watermark, merge, validate, and edit scans, images, and PDFs as local files or CamScanner cloud documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer downloads camscanner-cli into PATH without integrity verification.

Mitigation: Install only from a trusted source and prefer a reviewed installer with checksum or signature verification before adding the binary to PATH.

Risk: Document contents and processed results may be sent to CamScanner services or saved to CamScanner cloud documents.

Mitigation: Use local output flags for sensitive files and use -s only when cloud storage is intentional and acceptable.

Risk: Watermark removal and image text editing can alter document content.

Mitigation: Keep originals and perform these operations only when the user is authorized to modify the document.

## Reference(s):

- [CamScanner homepage](https://www.camscanner.com)
- [Server-resolved source repository](https://github.com/camscanner-ai/camscanner)
- [ClawHub skill page](https://clawhub.ai/camscanner-ai/skills/cs-cli)
- [Image Processing Reference](references/image-processing.md)
- [PDF Processing Reference](references/pdf-processing.md)
- [Tool Combination Quick Reference](references/tool-combos.md)
- [Batch Document Conversion Workflow](references/workflows/batch-convert.md)
- [Image Enhancement Workflow](references/workflows/image-enhance.md)
- [OCR Recognition and Content Extraction Workflow](references/workflows/ocr-extract.md)
- [Image Translation Workflow](references/workflows/translate.md)
- [Document Watermark Protection Workflow](references/workflows/watermark-protection.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell command examples and CLI-produced files or stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may be local files, stdout text or JSON, or CamScanner cloud documents depending on the selected CLI command and flags.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

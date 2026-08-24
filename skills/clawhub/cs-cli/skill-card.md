## Description:

CamScanner helps agents process documents with camscanner-cli for OCR, image and PDF conversion, enhancement, translation, watermarking, validation, and local or cloud output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[camscanner-ai](https://clawhub.ai/user/camscanner-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can have an agent run CamScanner CLI workflows to convert, enhance, OCR, translate, watermark, validate, and save document or image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input files are uploaded to CamScanner servers for processing.

Mitigation: Use the skill only for documents approved for CamScanner processing, especially when handling sensitive or regulated content.

Risk: Processed results are saved to the user's CamScanner account by default unless the user asks for local-only output.

Mitigation: Ask for or specify local-only output when persistent cloud storage is not desired.

Risk: Installers and updaters can replace the local CLI executable and skill files.

Mitigation: Install or update only when the CamScanner distribution channel is trusted, and review checksum or version evidence where available.

Risk: The skill requires OAuth login for CamScanner operations.

Mitigation: Use the browser OAuth flow and avoid displaying, copying, or storing tokens outside the supported credential store.

## Reference(s):

- [CamScanner homepage](https://www.camscanner.com)
- [ClawHub CamScanner skill page](https://clawhub.ai/camscanner-ai/skills/cs-cli)
- [Image Processing Reference](references/image-processing.md)
- [PDF Processing Reference](references/pdf-processing.md)
- [Tool Combination Quick Reference](references/tool-combos.md)
- [Batch Document Conversion Workflow](references/batch-convert.md)
- [OCR Recognition and Content Extraction Workflow](references/ocr-extract.md)
- [Image Enhancement and Restoration Workflow](references/image-enhance.md)
- [Multilingual Translation Workflow](references/translate.md)
- [Document Watermark Protection Workflow](references/watermark-protection.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; the CLI may produce files, stdout text, JSON, or cloud document IDs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save processed results locally, to the user's CamScanner account, or both, depending on command flags and user preference.]

## Skill Version(s):

1.1.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

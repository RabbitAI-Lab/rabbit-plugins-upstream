## Description:

CamScanner document processing - an intelligent document conversion and processing platform and official CamScanner Skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[camscanner-ai](https://clawhub.ai/user/camscanner-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to process scanned documents and images with CamScanner CLI workflows, including OCR, format conversion, enhancement, translation, watermark operations, and saving results locally or to a CamScanner account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Files are processed remotely and default behavior may save outputs to a CamScanner cloud account.

Mitigation: Use the skill only for documents appropriate for CamScanner processing; for sensitive documents, explicitly request local-only output and avoid automatic cloud save.

Risk: The updater can replace local CLI and skill files from CamScanner's CDN.

Mitigation: Administrators should review or disable the self-update flow unless signed, consented updates are acceptable.

Risk: Authentication tokens are required for account workflows.

Mitigation: Use the documented browser login flow and do not display token plaintext or write tokens to unsafe locations.

## Reference(s):

- [CamScanner Homepage](https://www.camscanner.com)
- [CamScanner ClawHub Skill](https://clawhub.ai/camscanner-ai/skills/cs-cli)
- [Image Processing Reference](references/image-processing.md)
- [PDF Processing Reference](references/pdf-processing.md)
- [Tool Combination Quick Reference](references/tool-combos.md)
- [Batch Document Conversion Workflow](references/workflows/batch-convert.md)
- [Image Enhancement and Restoration Workflow](references/workflows/image-enhance.md)
- [OCR Recognition and Content Extraction Workflow](references/workflows/ocr-extract.md)
- [Multilingual Translation Workflow](references/workflows/translate.md)
- [Document Watermark Protection Workflow](references/workflows/watermark-protection.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; CLI runs may produce stdout text, JSON, images, PDFs, Word or Excel documents, Markdown, TXT, ZIP files, and cloud-saved documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports JPG, JPEG, PNG, PDF, TXT, and Markdown inputs; uploads are limited to 40 MB and multi-image merge workflows accept up to 100 images.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

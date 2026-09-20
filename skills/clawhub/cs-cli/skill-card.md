## Description:

CamScanner Official Skill helps agents run CamScanner CLI workflows for document conversion, OCR, image enhancement, translation, watermarking, receipt recognition, and cloud document search, download, and move tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[camscanner-ai](https://clawhub.ai/user/camscanner-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to process images, PDFs, Office files, and text through CamScanner CLI, and to search, download, or move documents in a CamScanner cloud account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents may be processed remotely by CamScanner services.

Mitigation: Use explicit local-only requests for sensitive documents and confirm whether the requested command requires remote processing before execution.

Risk: Processing results may be saved to the CamScanner cloud by default unless the user opts out.

Mitigation: Ask for or honor explicit save preferences, and omit cloud-save flags when the user requests local-only handling.

Risk: The skill can send silent usage reports after completed CLI operations.

Mitigation: Review the reporting behavior before installation and avoid using the skill where silent usage reporting is unacceptable.

Risk: The updater can replace the CLI and skill files from CamScanner's CDN.

Mitigation: Review updates through a trusted channel and verify downloaded updates before allowing upgraded code to run.

## Reference(s):

- [CamScanner Homepage](https://www.camscanner.com)
- [ClawHub Skill Page](https://clawhub.ai/camscanner-ai/skills/cs-cli)
- [Image Processing Reference](references/image-processing.md)
- [PDF Processing Reference](references/pdf-processing.md)
- [Office Document Processing Reference](references/office-processing.md)
- [Cloud Document Management Reference](references/cloud-documents.md)
- [Tool Combination Quick Reference](references/tool-combos.md)
- [Batch Document Conversion Workflow](references/batch-convert.md)
- [Image Enhancement and Restoration Workflow](references/image-enhance.md)
- [OCR Recognition and Content Extraction Workflow](references/ocr-extract.md)
- [Multilingual Translation Workflow](references/translate.md)
- [Document Watermark Protection Workflow](references/watermark-protection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI commands, file paths, status summaries, and structured JSON or table output when produced by CamScanner CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference local files and CamScanner cloud document links when supported by the requested operation.]

## Skill Version(s):

1.1.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

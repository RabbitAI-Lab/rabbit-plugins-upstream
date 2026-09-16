## Description:

CamScanner document processing skill for document conversion, image and PDF processing, OCR, translation, watermark handling, formula extraction, document scanning, image text editing, and saving processed results to a user's CamScanner account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[camscanner-ai](https://clawhub.ai/user/camscanner-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to route CamScanner CLI commands for document processing tasks such as OCR, image enhancement, image/PDF conversion, watermarking, translation, receipt recognition, and cloud document search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and self-updates a local CamScanner CLI, which creates supply-chain exposure through the vendor distribution and update channel.

Mitigation: Review installation and upgrade behavior before deployment, and enable automatic upgrades only in environments that trust CamScanner's CDN and release process.

Risk: Document processing can upload user files to CamScanner services and the skill saves processed results to cloud by default.

Mitigation: For sensitive files, explicitly request local-only output and confirm whether cloud saving is acceptable before running commands.

Risk: The skill uses OAuth login and stores tokens in the system keychain.

Mitigation: Use the documented authentication flow, avoid exposing token values, and verify logout or credential cleanup requirements for shared machines.

## Reference(s):

- [CamScanner homepage](https://www.camscanner.com)
- [ClawHub skill page](https://clawhub.ai/camscanner-ai/skills/cs-cli)
- [Image processing reference](artifact/references/image-processing.md)
- [PDF processing reference](artifact/references/pdf-processing.md)
- [Tool combination quick reference](artifact/references/tool-combos.md)
- [Batch document conversion workflow](artifact/references/batch-convert.md)
- [OCR recognition and content extraction workflow](artifact/references/ocr-extract.md)
- [Image enhancement and restoration workflow](artifact/references/image-enhance.md)
- [Multilingual translation workflow](artifact/references/translate.md)
- [Document watermark protection workflow](artifact/references/watermark-protection.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and local or cloud file outputs produced by camscanner-cli]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processed outputs may include images, PDFs, Word documents, Excel spreadsheets, Markdown, TXT, ZIP files, stdout text, or JSON depending on the selected command.]

## Skill Version(s):

1.1.4 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

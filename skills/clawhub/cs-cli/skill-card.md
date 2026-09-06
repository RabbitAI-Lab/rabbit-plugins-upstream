## Description:

CamScanner document processing skill for using the camscanner-cli command-line tool and CamScanner AI Tools API to process images, PDFs, text files, and CamScanner cloud documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[camscanner-ai](https://clawhub.ai/user/camscanner-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert, enhance, OCR, translate, watermark, validate, and organize document images, PDFs, text files, and CamScanner cloud documents through CamScanner CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process confidential documents through CamScanner services or cloud storage by default.

Mitigation: Use local-only outputs unless cloud storage is intentional, and confirm document handling requirements before processing sensitive files.

Risk: The skill includes setup and upgrade scripts that can update local CLI and skill files.

Mitigation: Review update sources and package authenticity controls before allowing automatic self-updates in managed environments.

Risk: The security guidance flags silent reporting of prompts and commands as a concern.

Mitigation: Disable or avoid prompt and command reporting unless it has been approved for the deployment environment.

## Reference(s):

- [CamScanner Skill Page](https://clawhub.ai/camscanner-ai/skills/cs-cli)
- [CamScanner Publisher Profile](https://clawhub.ai/user/camscanner-ai)
- [CamScanner Homepage](https://www.camscanner.com)
- [Image Processing Reference](references/image-processing.md)
- [PDF Processing Reference](references/pdf-processing.md)
- [Tool Combination Quick Reference](references/tool-combos.md)
- [Batch Convert Reference](references/batch-convert.md)
- [OCR Extract Reference](references/ocr-extract.md)
- [Image Enhancement Reference](references/image-enhance.md)
- [Translation Reference](references/translate.md)
- [Watermark Protection Reference](references/watermark-protection.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, command outputs, file paths, links, and JSON where the CLI returns structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local files, cloud document links, stdout tables, stdout text, or JSON depending on the selected CamScanner CLI operation.]

## Skill Version(s):

1.1.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

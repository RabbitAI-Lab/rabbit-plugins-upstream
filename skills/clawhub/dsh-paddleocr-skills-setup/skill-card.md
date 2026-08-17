## Description:

Install and configure the native PaddleOCR plugin for DeepSeek Harness from the Settings > PaddleOCR GUI for OCR, image-to-text, PDF-to-Markdown, structured document parsing, endpoint setup, credential setup, verification, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aidenwu0209](https://clawhub.ai/user/aidenwu0209)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this setup skill to install and configure the PaddleOCR plugin in DeepSeek Harness through the GUI. It supports OCR workflows for screenshots, scanned documents, PDFs, CJK text, tables, formulas, layout parsing, endpoint configuration, credential handling, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs a third-party DeepSeek Harness plugin from a GitHub source.

Mitigation: Confirm the third-party source is trusted before installation.

Risk: OCR requests may send document content to configured OCR service endpoints.

Mitigation: Only process documents appropriate for the selected OCR service and confirm the HTTPS /ocr and /layout-parsing endpoints before use.

Risk: OCR service tokens can be exposed if pasted into files or logs.

Mitigation: Store tokens only through the DSH Credential field and avoid echoing or logging secrets.

## Reference(s):

- [Project homepage](https://github.com/Aidenwu0209/dsh-PaddleOCR-Skills)
- [PaddleOCR website](https://www.paddleocr.com)
- [ClawHub skill page](https://clawhub.ai/aidenwu0209/skills/dsh-paddleocr-skills-setup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports prerequisite versions, install commands, the local Web URL, visible PaddleOCR configuration status, and values still required from the user.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

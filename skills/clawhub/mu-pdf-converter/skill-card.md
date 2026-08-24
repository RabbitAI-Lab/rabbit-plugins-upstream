## Description:

Converts valid text-layer PDFs into editable PPTX, DOCX, XLSX table extracts, page images, filled forms, or watermark-removed PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate office PDF conversion and processing workflows, including PDF-to-PPT, Word, Excel table extraction, page image rendering, form filling, and authorized watermark removal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default PPT conversion may send extracted document text to translation services or an environment-configured model endpoint.

Mitigation: Use --no-translate for confidential, regulated, or customer documents, or configure a trusted local translation endpoint before converting PDFs to PPT.

Risk: Watermark removal can alter documents that the user may not be authorized to modify.

Mitigation: Use watermark removal only on documents the user owns or is authorized to modify, and use detect-only mode before making changes when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-pdf-converter)
- [Publisher profile](https://clawhub.ai/user/muippt)
- [Usage guide](references/usage-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown guidance with shell commands and generated PDF-derived files such as .pptx, .docx, .xlsx, .png, .jpg, or .pdf.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Valid PDF inputs are required; scanned PDFs may require OCR first; batch Excel extraction is capped at 100 PDFs and PPT translation at 5000 text blocks.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

ComPDF OCR helps agents prepare accurate ComPDF Server API request plans for OCR, text extraction, and searchable-PDF generation from scanned PDFs and images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to select supported ComPDF OCR endpoints, assemble request fields, and understand polling or download steps for scanned PDFs and image documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR processing may require sending selected PDFs or images to ComPDF.

Mitigation: Identify affected files and destination before upload, obtain confirmation unless already authorized, and use asynchronous or presigned workflows for large, batch, or security-sensitive uploads.

Risk: The skill stores a ComPDF API key in a local skill file.

Mitigation: Store only after user confirmation, read only the skill-local api_key file, and do not display, log, commit, or include the key in examples.

Risk: The bundled API reference contains broader ComPDF capabilities outside this OCR skill's scope.

Mitigation: Limit use to the OCR operations listed in SKILL.md and do not treat broader reference sections as permission to perform editing, encryption, decryption, watermark, or AI extraction tasks.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [PDF to TXT API](https://www.compdf.com/guides/api-reference/v2/pdf-to-txt)
- [PDF to Editable PDF API](https://www.compdf.com/guides/api-reference/v2/pdf-to-editable-pdf-tool-guide)
- [Image to TXT API](https://www.compdf.com/guides/api-reference/v2/image-to-txt)
- [OCR Language Codes](https://www.compdf.com/guides/api-reference/v2/ocr-languages)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and optional cURL-style request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes next polling or download steps and excludes API keys from examples and final output.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

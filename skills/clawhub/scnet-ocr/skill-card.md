## Description:

scnet-ocr sends user-selected images or PDFs to SCNET's OCR API to extract text and structured fields from general documents, identity documents, invoices, financial records, forms, and related certificates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agent users use this skill when a user explicitly asks to run OCR or structured document extraction on a specified local image or PDF. It is suited for text extraction, invoice and receipt parsing, ID and certificate recognition, table recognition, and similar document workflows where upload to SCNET is acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images or PDFs may contain IDs, bank cards, medical records, financial documents, or other regulated data and are uploaded to SCNET or the configured OCR endpoint.

Mitigation: Confirm the user has permission to upload the file, send only the minimum file needed for the task, and use the skill only when third-party OCR processing is acceptable.

Risk: OCR results may contain sensitive personal or business information.

Mitigation: Keep the returned JSON in trusted environments, avoid pasting it into untrusted tools or chats, and clear or protect outputs according to the user's data-handling requirements.

Risk: A custom SCNET_API_BASE changes where the selected file is sent.

Mitigation: Verify SCNET_API_BASE and SCNET_API_KEY configuration before use, especially in shared or inherited environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/scnet-ocr)
- [SCNET publisher profile](https://clawhub.ai/user/scnet-sugon)
- [Sugon-Scnet OCR API documentation summary](references/api-docs.md)
- [OCR field summary](assets/templates/fields-summary.md)
- [SCNET website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [json, text, guidance]

**Output Format:** [JSON recognition results on stdout, with human-readable privacy notices, retry notices, and error messages on stderr.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and optionally SCNET_API_BASE; uploads the selected file to the configured SCNET OCR endpoint.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

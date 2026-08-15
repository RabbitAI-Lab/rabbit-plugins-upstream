## Description:

Encrypt PDFs with AES-128, AES-256, or RC4 options and decrypt authorized PDFs with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and document operations teams use this skill to prepare ComPDF Server API request plans for encrypting PDFs or decrypting authorized PDFs. It helps select the supported endpoint, request fields, authentication handling, upload mode, and follow-up polling or download steps for document-access protection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF contents and passwords may be sent to ComPDF for processing.

Mitigation: Confirm the exact file and destination before upload, avoid repeating sensitive passwords in output, and use the skill only when that external processing is acceptable.

Risk: Decryption could be misused on files the user is not authorized to unlock.

Mitigation: Require explicit authorization before assisting with decryption and refuse unsupported or unauthorized unlocking workflows.

Risk: A stored ComPDF API key could be exposed if included in examples, logs, or version control.

Mitigation: Keep the key only in the skill-local api_key file, exclude it from publishing and version control, and never display it in request examples or final output.

Risk: The bundled reference snapshot includes endpoints beyond this skill's encrypt/decrypt scope.

Mitigation: Use only the documented Encrypt PDF and Decrypt PDF operations for this skill and do not treat the broader reference snapshot as permission to call unrelated endpoints.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF PDF API catalog](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf)
- [ComPDF authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF PDF encryption API](https://www.compdf.com/guides/api-reference/v2/pdf-encrypt)
- [ComPDF PDF decryption API](https://www.compdf.com/guides/api-reference/v2/pdf-decrypt)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with endpoint, method, content type, request fields, expected task/result fields, and next polling or download step]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF API request details, sourceType=5 routing, and credential setup guidance without exposing the API key.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

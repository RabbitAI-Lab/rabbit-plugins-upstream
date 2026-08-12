## Description:

ComPDF Toolkit helps agents plan ComPDF Server API requests for document conversion, OCR, data extraction, PDF editing, protection, compression, and watermarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to choose the correct ComPDF Server API endpoint and prepare request details for PDF and document workflows such as conversion, OCR, extraction, editing, security operations, compression, and watermarking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents may be sent to ComPDF for third-party processing.

Mitigation: Confirm affected files and destination before upload, and use care with confidential, regulated, or identity documents.

Risk: API keys could be exposed if included in examples, logs, published files, or non-local credential locations.

Mitigation: Store the key only in the skill-local api_key file, exclude that file from publishing, and never display or log the key.

Risk: Document operations such as overwrite, delete, decrypt, or protection changes can permanently alter document state.

Mitigation: Require explicit confirmation before destructive or security-sensitive operations and preserve original files unless replacement is requested.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF Conversion API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview)
- [ComPDF PDF API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint, method, request field, response field, and follow-up step details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF API request details; must not include API keys.]

## Skill Version(s):

1.0.3 (source: server release metadata and user changelog, created 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

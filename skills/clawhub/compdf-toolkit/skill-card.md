## Description:

All-in-one ComPDF workflow for document conversion, OCR, data extraction, PDF editing, protection, compression, and watermarking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to plan ComPDF Server API requests for PDF, Office, HTML, CSV, RTF, TXT, and image document workflows, including conversion, OCR, extraction, editing, protection, compression, and watermarking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents may be uploaded to ComPDF-operated services for processing.

Mitigation: Identify affected files and destination before upload, and obtain user confirmation unless the upload was already authorized.

Risk: A ComPDF API key may be stored as local skill runtime state.

Mitigation: Store only the current skill's API key in the sibling api_key file after user confirmation, and do not display, log, commit, or include the key in examples.

Risk: Decryption, watermark removal, page deletion, or protection changes can affect document integrity or rights.

Mitigation: Use these operations only on documents the user owns or is authorized to modify, confirm before permanent changes, and preserve originals unless replacement is explicitly requested.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF Conversion API catalog](https://www.compdf.com/guides/api-reference/v2/api-overview)
- [ComPDF PDF API catalog](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with endpoint, method, content type, request fields, response fields, and next-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ComPDF request routing details such as sourceType=5; excludes API key values from examples and final output.]

## Skill Version(s):

1.0.4 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

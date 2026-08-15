## Description:

PDF Converter helps agents prepare ComPDF API request plans for bidirectional PDF, document, and image conversion workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and operations teams use this skill to select official ComPDF Server API conversion endpoints and prepare request plans for PDF-to-document, document-to-PDF, and image-to-document workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents are uploaded to ComPDF for processing.

Mitigation: Obtain explicit confirmation before upload and avoid confidential, regulated, encrypted, or third-party documents unless organizational policy permits sharing with ComPDF.

Risk: The skill stores a ComPDF API key in a local api_key file.

Mitigation: Store only the current skill's key, do not display or log it, and keep the file out of version control and published artifacts.

Risk: The skill is scoped to conversion workflows and may be a poor fit for OCR-only, page editing, security, watermark, or compression requests.

Mitigation: Route non-conversion requests to focused skills and use only documented ComPDF endpoints, request fields, and response fields.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF Conversion API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [PDF Converter on ClawHub](https://clawhub.ai/compdf-youna/skills/pdf-converter)

## Skill Output:

**Output Type(s):** [guidance, API Calls, Configuration instructions]

**Output Format:** [Markdown with endpoint, request field, response field, polling, and download guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns request plans and operational guidance; it should not include API keys or upload files without user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

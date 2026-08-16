## Description:

Convert PDF files into reusable HTML with ComPDF. Use for web publishing, browser workflows, portal embedding, content migration, and PDF-to-HTML requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, and AI agents use this skill to prepare ComPDF Server API requests that convert static PDF documents into browser-friendly HTML for web publishing, portal embedding, migration, and reuse workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDFs are uploaded to ComPDF for processing.

Mitigation: Confirm affected files and destination before upload, and use asynchronous or presigned workflows for large, batch, or security-sensitive documents.

Risk: A ComPDF API key is required for requests.

Mitigation: Store only the current skill's key in the skill-local api_key file, and do not display, log, commit, or include the key in examples or final output.

Risk: The artifact bundles broader ComPDF API documentation than the authorized PDF-to-HTML operation.

Mitigation: Use only the PDF-to-HTML endpoint and treat non-PDF-to-HTML reference sections as documentation noise.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF PDF to HTML API](https://www.compdf.com/guides/api-reference/v2/pdf-to-html)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)

## Skill Output:

**Output Type(s):** [guidance, API Calls, configuration]

**Output Format:** [Markdown with endpoint, method, content type, request fields, expected task/result fields, and next polling or download step]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sourceType=5 in final ComPDF request details and preserves original files unless replacement is explicitly requested.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

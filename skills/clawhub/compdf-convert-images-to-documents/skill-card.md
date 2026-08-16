## Description:

Convert image files into Word, Excel, PPT, PDF, HTML, RTF, CSV, TXT, or JSON with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare ComPDF Server API requests that convert screenshots, scans, receipts, forms, and other image-based business files into editable or structured document outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected image files may be uploaded to ComPDF for conversion.

Mitigation: Identify the affected files and destination before upload and obtain user confirmation unless the upload was explicitly authorized.

Risk: The skill stores a ComPDF API key in a local api_key file.

Mitigation: Store only the current skill's key in that file and do not display, log, commit, or include the key in examples.

Risk: The bundled API reference includes endpoints outside this skill's image conversion scope.

Mitigation: Keep use limited to the listed image conversion operations unless a separate, explicit request and focused skill covers another endpoint.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint details, request fields, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF API request plans and credential setup guidance; does not include API keys.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Convert image files into Word, Excel, PPT, PDF, HTML, RTF, CSV, TXT, or JSON with ComPDF. Use for screenshots, scans, receipts, forms, and photo-based business documents that need editable or structured output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare ComPDF Server API requests for converting screenshots, scans, receipts, forms, and other image-based business documents into editable or structured formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a local ComPDF API key and uses it for requests to ComPDF.

Mitigation: Store the key only in the documented local key file, pass it only through the x-api-key header, and never include it in logs, code, examples, or output.

Risk: Selected image files may contain receipts, forms, business records, or personal information and are uploaded to ComPDF for processing.

Mitigation: Review files and request details before approval, and limit use to the listed image-to-document operations.

Risk: Incorrect endpoint or field choices could produce failed or misleading conversion requests.

Mitigation: Use the exact endpoint path, request fields, request mode, and response fields from the bundled official API reference snapshot.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF API Reference: Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF API Reference: Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF API Reference: Conversion API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint, method, content type, request fields, response fields, and next-step instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API key setup guidance, polling or download steps, and confirmation reminders before overwriting files or sending sensitive documents externally.]

## Skill Version(s):

1.0.1 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

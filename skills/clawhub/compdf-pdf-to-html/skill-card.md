## Description: <br>
Convert PDF files into reusable HTML with ComPDF. Use for web publishing, browser workflows, portal embedding, content migration, and PDF-to-HTML requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and content teams use this skill to plan ComPDF Server API requests that convert static PDF documents into reusable HTML for web publishing, portal embedding, browser workflows, and content migration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDFs are sent to ComPDF as an external processor for conversion. <br>
Mitigation: Confirm before sending sensitive documents and use only PDF-to-HTML requests with the documented sync, async, or presigned workflow appropriate to file size and privacy needs. <br>
Risk: The skill requires a ComPDF API key. <br>
Mitigation: Keep the API key in a private local key file, pass it only as the x-api-key header, and never include it in code, logs, examples, or output. <br>
Risk: Using unsupported options or a different conversion endpoint can produce incorrect requests. <br>
Mitigation: Select only the PDF-to-HTML operation and use the exact endpoint path, request fields, request mode, and response fields from the bundled official reference snapshot. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF PDF to HTML API](https://www.compdf.com/guides/api-reference/v2/pdf-to-html) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown request plan with endpoint, method, content type, request fields, expected task/result fields, and next polling or download steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves original files unless replacement is explicitly requested; API keys are handled only through a private local key file and the x-api-key header.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

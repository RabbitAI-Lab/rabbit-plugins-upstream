## Description: <br>
Convert PDF content into structured JSON with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to prepare ComPDF Server API requests that convert PDF text, tables, images, and structured content into JSON for AI pipelines, applications, and system integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF files selected for conversion are processed by ComPDF as an external service. <br>
Mitigation: Use the skill only for documents that may leave the local environment, and choose asynchronous or presigned workflows for larger, batch, or security-sensitive uploads when appropriate. <br>
Risk: The skill requires a ComPDF API key. <br>
Mitigation: Keep the API key in the documented private key file, pass it only as the x-api-key header, and do not include it in code, logs, examples, or output. <br>


## Reference(s): <br>
- [ComPDF skill page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-json) <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF PDF to JSON API](https://www.compdf.com/guides/api-reference/v2/pdf-to-json) <br>
- [ComPDF API Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with endpoint details, request fields, expected response fields, and optional command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ComPDF API key and sends selected PDF files to ComPDF for processing.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

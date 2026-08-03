## Description: <br>
Convert PDF files into reusable HTML with ComPDF for web publishing, browser workflows, portal embedding, content migration, and PDF-to-HTML requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content teams use this skill to prepare ComPDF Server API requests that convert PDFs into reusable HTML for websites, portals, and content migration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs are sent to ComPDF for conversion. <br>
Mitigation: Use the skill only for documents approved for external processing and confirm before security-sensitive uploads. <br>
Risk: The skill relies on a local ComPDF API key file. <br>
Mitigation: Store the key only in the documented private file and never include it in code, logs, examples, or chat output. <br>
Risk: The bundled reference snapshot includes many ComPDF endpoints beyond PDF to HTML. <br>
Mitigation: Limit use to the supported PDF-to-HTML operation and avoid using the broad reference for non-HTML, encryption, decryption, or AI extraction tasks under this skill. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF V2 API Reference](https://www.compdf.com/guides/api-reference/v2/) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [ComPDF PDF to HTML](https://www.compdf.com/guides/api-reference/v2/pdf-to-html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the endpoint, HTTP method, content type, request fields, expected task/result fields, and polling or download next step.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

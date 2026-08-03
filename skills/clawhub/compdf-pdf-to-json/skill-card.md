## Description: <br>
Convert PDF content into structured JSON with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation teams use this skill to prepare ComPDF Server API requests that convert PDF text, tables, images, and structured content into JSON for AI pipelines, applications, and system integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDFs are sent to ComPDF as an external document processing service. <br>
Mitigation: Review the request before upload and avoid sending confidential PDFs unless the ComPDF account, retention, and compliance requirements allow it. <br>
Risk: The workflow depends on a local ComPDF API key file. <br>
Mitigation: Keep the API key file private and pass the key only through the x-api-key request header. <br>


## Reference(s): <br>
- [ComPDF PDF to JSON skill page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-json) <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF API overview](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF PDF to JSON API reference](https://www.compdf.com/guides/api-reference/v2/pdf-to-json) <br>
- [ComPDF authentication reference](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF request workflow reference](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands] <br>
**Output Format:** [Markdown with API request details and next-step instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces request plans and handling guidance; it does not include API keys in output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

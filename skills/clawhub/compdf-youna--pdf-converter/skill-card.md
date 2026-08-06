## Description: <br>
Convert PDFs to Word, Excel, PPT, HTML, RTF, images, CSV, TXT, JSON, Markdown, OFD, or editable PDF, and convert supported documents and images to PDF with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, AI agents, and operations teams use this skill to plan ComPDF Server API requests for bidirectional PDF and document conversion workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected documents are uploaded to ComPDF for processing, which may be inappropriate for highly confidential files. <br>
Mitigation: Confirm each external upload deliberately and use the skill only when the ComPDF account, region, and retention expectations are acceptable. <br>
Risk: The skill reads a local ComPDF API key file to authenticate requests. <br>
Mitigation: Store the key only in the documented private local file and pass it only as the x-api-key header; do not include it in code, logs, examples, or output. <br>
Risk: A stale API snapshot could lead to outdated endpoint paths, fields, or enum values. <br>
Mitigation: Use the included endpoint index and official API snapshot, and refresh the snapshot before release to inspect changed endpoints, fields, and enum values. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF V2 Conversion API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF V2 Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [PDF Converter on ClawHub](https://clawhub.ai/compdf-youna/skills/pdf-converter) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, configuration, shell commands] <br>
**Output Format:** [Markdown with endpoint, request, response, polling, and download details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected ComPDF endpoint, HTTP method, content type, request fields, expected task/result fields, and next polling or download step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

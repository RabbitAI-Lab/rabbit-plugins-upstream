## Description: <br>
Converts Word, Excel, PPT, HTML, TXT, CSV, RTF, PNG, and JPG files into PDF with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and external users use this skill to plan ComPDF Server API requests that convert business documents, web content, and image files into fixed-layout PDFs for sharing, approvals, printing, reporting, or archiving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected documents are uploaded to ComPDF for processing. <br>
Mitigation: Use the skill only for documents approved for external ComPDF processing and prefer the documented asynchronous or presigned workflow for large, batch, or security-sensitive uploads. <br>
Risk: The skill stores and reads a local ComPDF API key file. <br>
Mitigation: Keep the key file private, pass the key only as the x-api-key header, and never include it in code, logs, examples, or agent output. <br>
Risk: The bundled reference snapshot includes broader ComPDF API material than the document-to-PDF operations in scope. <br>
Mitigation: Use only the supported document-to-PDF operations listed in the skill and treat non-conversion API sections as out of scope unless separately authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-documents-to-pdf) <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF API reference](https://www.compdf.com/guides/api-reference/v2/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown with endpoint, method, request fields, response fields, and next-step instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include polling or download steps; must not expose the ComPDF API key.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

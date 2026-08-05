## Description: <br>
Convert image files into Word, Excel, PPT, PDF, HTML, RTF, CSV, TXT, or JSON with ComPDF for editable or structured output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to prepare ComPDF Server API request plans for converting image files into editable document formats or structured data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a local ComPDF API key path and prepares uploads of selected image documents to ComPDF. <br>
Mitigation: Use it only with documents approved for ComPDF processing, keep the API key private, and ensure generated requests place the key only in the x-api-key header. <br>
Risk: The bundled reference material includes PDF and AI document APIs outside the advertised image-to-document scope. <br>
Mitigation: Constrain use to the listed image-to-document operations and require separate review before using PDF decryption, deletion, watermark removal, broad task inspection, or AI extraction capabilities. <br>
Risk: Large, batch, or sensitive files may be unsuitable for a simple synchronous upload flow. <br>
Mitigation: Use asynchronous or presigned workflows for large, batch, browser, mobile, or security-sensitive uploads. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF Conversion API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, and next-step instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ComPDF API method, content type, task fields, result fields, polling, or download guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

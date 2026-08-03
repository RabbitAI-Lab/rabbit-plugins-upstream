## Description: <br>
Convert image files into Word, Excel, PPT, PDF, HTML, RTF, CSV, TXT, or JSON with ComPDF for screenshots, scans, receipts, forms, and photo-based business documents that need editable or structured output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to plan ComPDF Server API requests that convert image-based business files into editable or structured document outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images and derived document outputs are processed by ComPDF. <br>
Mitigation: Review file sensitivity before sending images or outputs, and use the documented asynchronous or presigned workflow for large, batch, or security-sensitive uploads. <br>
Risk: The bundled reference includes broader ComPDF API material than this image-conversion skill needs. <br>
Mitigation: Select only the supported image-conversion operations listed by the skill, and prune the reference snapshot to image-conversion endpoints in a future release. <br>
Risk: API keys could be exposed if copied into chat, code, logs, examples, or output. <br>
Mitigation: Keep the key in a local private key file, pass it only as the x-api-key header, and never display or commit it. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF V2 API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with endpoint details and request-plan fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include endpoint path, HTTP method, content type, request fields, expected task/result fields, and polling or download steps; must not include API key values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
ComPDF Toolkit helps agents plan ComPDF Server API requests for document conversion, OCR, data extraction, PDF editing, protection, compression, and watermarking across PDF, Office, HTML, CSV, RTF, TXT, and image files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-workflow teams use this skill to select official ComPDF Server API endpoints and prepare request plans for conversion, OCR, extraction, PDF editing, protection, compression, watermarking, and related document processing tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External document uploads can expose confidential, regulated, or password-protected files to ComPDF processing. <br>
Mitigation: Confirm before uploading sensitive documents and use the documented asynchronous or presigned workflow for large, batch, or security-sensitive uploads when appropriate. <br>
Risk: API keys can be leaked if pasted into prompts, examples, logs, or committed files. <br>
Mitigation: Keep the key in a private local file and pass it only as the x-api-key header; do not display or embed it in outputs. <br>
Risk: Decrypted outputs and destructive PDF operations can alter or expose protected content. <br>
Mitigation: Identify affected files, preserve originals unless replacement is authorized, and obtain confirmation before overwriting, deleting, decrypting, or applying permanent protection. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF V2 API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF V2 PDF API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf) <br>
- [ComPDF V2 Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF V2 Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with endpoint details, request fields, response fields, and next-step instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include endpoint path, HTTP method, content type, polling or download steps, and API key setup guidance; should not expose API keys.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Add or remove text and image watermarks in PDFs with ComPDF. Use for PDF branding, draft review marks, document control, watermark cleanup, and final-delivery preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to prepare accurate ComPDF Server API request plans for adding text or image watermarks to PDFs or removing existing watermarks from supported files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads a local ComPDF API key file. <br>
Mitigation: Keep the key in a private local file, pass it only as the x-api-key header, and never place it in code, logs, examples, or output. <br>
Risk: Selected PDFs are uploaded to the external ComPDF service for processing. <br>
Mitigation: Use only approved documents, avoid confidential, regulated, or third-party documents without approval, and confirm before sending a document externally. <br>
Risk: Watermark removal or replacement can change document controls or final-delivery status. <br>
Mitigation: Confirm authorization and affected files before removal or replacement, and preserve original files unless replacement is explicitly requested. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](artifact/references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md) <br>
- [ComPDF Add Watermark API](https://www.compdf.com/guides/api-reference/v2/watermark-guides) <br>
- [ComPDF Remove Watermark API](https://www.compdf.com/guides/api-reference/v2/del-watermark-guides) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill returns the endpoint, method, content type, request fields, expected task or result fields, and next polling or download step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Recognize and extract text from scanned PDFs and images with ComPDF OCR workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to plan ComPDF Server API OCR requests for scanned PDFs, screenshots, photographed documents, image OCR, searchable PDF generation, and OCR-derived text extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Chosen documents are sent to ComPDF for OCR processing. <br>
Mitigation: Install and use the skill only when sending those documents to ComPDF is acceptable for the user's data-handling requirements. <br>
Risk: The workflow depends on a local ComPDF API key file. <br>
Mitigation: Store the key only in the documented private key file and pass it only as the x-api-key header; do not display it in code, logs, examples, or output. <br>
Risk: The bundled reference snapshot contains ComPDF APIs beyond this OCR skill's authorized scope. <br>
Mitigation: Keep requests to the listed OCR operations and verify endpoint paths, fields, modes, and response fields against the matching reference section. <br>


## Reference(s): <br>
- [ComPDF OCR skill page](https://clawhub.ai/compdf-youna/skills/compdf-ocr) <br>
- [ComPDF publisher profile](https://clawhub.ai/user/compdf-youna) <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF PDF to TXT API](https://www.compdf.com/guides/api-reference/v2/pdf-to-txt) <br>
- [ComPDF Image to TXT API](https://www.compdf.com/guides/api-reference/v2/image-to-txt) <br>
- [ComPDF PDF to editable PDF API](https://www.compdf.com/guides/api-reference/v2/pdf-to-editable-pdf-tool-guide) <br>
- [ComPDF OCR language codes](https://www.compdf.com/guides/api-reference/v2/ocr-languages) <br>
- [ComPDF request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [ComPDF authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, expected task or result fields, and polling or download steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill returns request plans for the listed OCR operations and avoids exposing API keys.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

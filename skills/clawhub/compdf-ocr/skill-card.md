## Description: <br>
Recognize and extract text from scanned PDFs and images with ComPDF OCR workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and teams use this skill to prepare ComPDF Server API request plans for OCR on scanned PDFs and images, including text extraction and searchable PDF generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents selected for OCR are processed by ComPDF's external service. <br>
Mitigation: Install and use the skill only when comfortable sending the chosen documents to ComPDF, and confirm before uploading sensitive documents. <br>
Risk: The skill requires a ComPDF API key for authenticated requests. <br>
Mitigation: Keep the API key file private, pass the key only through the x-api-key header, and do not place it in code, logs, examples, or output. <br>
Risk: The bundled API snapshot includes non-OCR reference sections that are outside this skill's intended scope. <br>
Mitigation: Use only the supported OCR operations listed by the skill and treat non-OCR reference sections as out of scope. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [ComPDF OCR Language Codes](https://www.compdf.com/guides/api-reference/v2/ocr-languages) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with endpoint, request, response, polling, download, and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses documented ComPDF endpoint paths and request fields; API keys should not be displayed or logged.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

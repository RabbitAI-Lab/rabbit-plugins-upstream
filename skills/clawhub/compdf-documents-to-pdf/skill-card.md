## Description: <br>
Convert Word, Excel, PPT, HTML, TXT, CSV, RTF, PNG, and JPG files into PDF with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, business users, and agents use this skill to prepare ComPDF Server API request plans that convert office documents, web content, plain text, CSV, RTF, PNG, and JPG files into fixed-layout PDF output for sharing, approvals, printing, or archiving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill uses a cloud ComPDF workflow that reads a local API key and uploads documents for processing. <br>
Mitigation: Use it only when cloud processing is approved, keep the API key in a private local file, pass the key only as the x-api-key header, and avoid sensitive files unless upload is authorized. <br>
Risk: The package includes broad ComPDF API reference material beyond the intended document-to-PDF operations. <br>
Mitigation: Constrain agents to the supported document-to-PDF endpoints listed by the skill and verify endpoint selection before using it with sensitive files. <br>


## Reference(s): <br>
- [Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF Conversion API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API request guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with endpoint details, request fields, response fields, and next-step guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces request plans for PDF output only; API keys should not appear in logs, code, examples, or responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

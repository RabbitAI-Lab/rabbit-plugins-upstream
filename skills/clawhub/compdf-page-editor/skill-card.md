## Description: <br>
ComPDF Page Editor helps agents prepare ComPDF Server API requests to merge, split, rotate, insert, delete, and extract PDF pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations teams, and agent users can use this skill to plan PDF page-management requests for document assembly, cleanup, restructuring, and selected-page output through ComPDF. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact bundles broader ComPDF API reference material than the page-management operations in scope. <br>
Mitigation: Use only the documented page-management operations: merge, split, rotate, insert, delete, and extract. <br>
Risk: PDF tasks may require uploading documents to ComPDF. <br>
Mitigation: Do not use the skill on sensitive PDFs unless the user has approved external upload to ComPDF. <br>
Risk: The skill relies on a local ComPDF API key file. <br>
Mitigation: Keep the API key file private and pass the key only in the x-api-key header. <br>


## Reference(s): <br>
- [ComPDF Page Editor on ClawHub](https://clawhub.ai/compdf-youna/skills/compdf-page-editor) <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF PDF API catalog](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown request plan with endpoint, method, content type, fields, response fields, and follow-up steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include polling or download guidance; API keys should not be displayed, logged, or embedded in examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Convert PDF files into editable Word documents with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and AI agents use this skill to prepare ComPDF Server API requests that convert PDFs into editable Word documents for contracts, reports, forms, proposals, review, revision, localization, or business reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs are uploaded to ComPDF for processing under the user's ComPDF account. <br>
Mitigation: Use the skill only when ComPDF processing is approved for the document, and avoid sensitive documents unless organizational policy permits external processing. <br>
Risk: The skill reads a local API key file and uses the key for ComPDF API requests. <br>
Mitigation: Keep the API key file private, pass the key only as the x-api-key header, and do not include the key in code, logs, examples, or output. <br>
Risk: Converted file download links are temporary and may expose converted document access while valid. <br>
Mitigation: Download results promptly, share links only with authorized users, and prefer asynchronous or presigned workflows for larger or security-sensitive uploads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-word) <br>
- [ComPDF Endpoint Index](artifact/references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md) <br>
- [ComPDF PDF to Word API](https://www.compdf.com/guides/api-reference/v2/pdf-to-word) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and next-step guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill prepares request plans for ComPDF PDF-to-Word conversion and instructs agents to keep API keys out of code, logs, examples, and output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

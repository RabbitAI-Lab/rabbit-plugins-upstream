## Description: <br>
Convert PDF content into structured JSON with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare ComPDF Server API requests that convert PDF text, tables, images, and structured content into JSON for AI pipelines, applications, and system integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDF files are uploaded to ComPDF for processing. <br>
Mitigation: Confirm the user is comfortable using ComPDF as a third-party processor before uploading sensitive documents. <br>
Risk: ComPDF API keys could be exposed if copied into prompts, logs, examples, or generated code. <br>
Mitigation: Read the key from a private local key file and pass it only in the x-api-key header. <br>
Risk: Returned fileUrl or downloadUrl values can expose processed document contents while valid. <br>
Mitigation: Treat result URLs as sensitive and avoid sharing or logging them unnecessarily. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-json) <br>
- [ComPDF PDF to JSON API reference](https://www.compdf.com/guides/api-reference/v2/pdf-to-json) <br>
- [ComPDF authentication reference](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF request workflow reference](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [Endpoint index](references/endpoint-index.md) <br>
- [Official API reference snapshot](references/official-api-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown request plan with endpoint, method, content type, request fields, response fields, and next polling or download step] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not expose the API key; preserves original files unless replacement is explicitly requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

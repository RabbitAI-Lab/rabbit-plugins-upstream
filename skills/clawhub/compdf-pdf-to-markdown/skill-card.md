## Description: <br>
Convert PDF files into Markdown with ComPDF for knowledge-base ingestion, developer documentation, content repurposing, research workflows, or PDF-to-Markdown requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and content teams use this skill to prepare accurate ComPDF Server API request plans for converting PDFs into Markdown. It supports document ingestion, documentation reuse, content repurposing, and research workflows that need editable text rather than PDF files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs are uploaded to ComPDF for conversion and may contain sensitive content. <br>
Mitigation: Use the skill only with documents approved for ComPDF processing, and select asynchronous or presigned workflows when larger or security-sensitive uploads require that flow. <br>
Risk: The bundled reference docs cover broader ComPDF operations than the advertised PDF-to-Markdown skill. <br>
Mitigation: Limit use to the supported PDF to Markdown operation and its documented endpoint; do not use unrelated deletion, decryption, watermarking, or AI extraction entries as permission for additional actions. <br>
Risk: API keys could be exposed if copied into prompts, logs, examples, or output. <br>
Mitigation: Read the key from the local configured file and pass it only as the x-api-key header; do not display, commit, upload, or log the key. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF PDF to Markdown API](https://www.compdf.com/guides/api-reference/v2/pdf-to-md) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown request plan with endpoint, method, content type, request fields, expected response fields, and next polling or download step] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Should preserve original files unless replacement is explicitly requested and should never print API keys or other secrets.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

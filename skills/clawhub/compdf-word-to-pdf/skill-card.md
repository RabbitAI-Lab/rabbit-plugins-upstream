## Description: <br>
Convert Word documents into polished PDFs with ComPDF. Use for contracts, reports, proposals, manuals, approvals, formal delivery, and Word-to-PDF requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operations teams, and document-heavy business users use this skill to prepare ComPDF Server API request plans that convert Word documents into stable PDFs for contracts, reports, proposals, manuals, approvals, and formal delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled reference includes many ComPDF operations beyond Word-to-PDF, which could lead an agent to select an unrelated PDF editing, decryption, or AI extraction endpoint. <br>
Mitigation: Constrain use to the supported Word-to-PDF operation and verify the selected endpoint is the documented Word-to-PDF endpoint before preparing a request. <br>
Risk: Word files are sent to ComPDF for conversion, which may expose sensitive document contents to an external service. <br>
Mitigation: Confirm the intended file and upload before sending; for large, batch, or security-sensitive work, prefer the documented asynchronous or presigned workflow. <br>
Risk: ComPDF API keys could be exposed if copied into prompts, code examples, logs, or final output. <br>
Mitigation: Read the key from the configured local key file and pass it only as the x-api-key header; never display or persist the key in generated materials. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF Word to PDF API](https://www.compdf.com/guides/api-reference/v2/word-to-pdf) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with endpoint details, request fields, expected response fields, example shell commands, and next-step instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill should keep API keys out of code, logs, examples, and final output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

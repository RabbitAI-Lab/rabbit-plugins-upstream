## Description: <br>
Convert Word documents into polished PDFs with ComPDF. Use for contracts, reports, proposals, manuals, approvals, formal delivery, and Word-to-PDF requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to prepare ComPDF Server API request plans for converting Word documents into PDFs while preserving document layout for contracts, reports, proposals, manuals, approvals, and delivery workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Word documents are uploaded to ComPDF for conversion. <br>
Mitigation: Use the skill only when external document upload to ComPDF is acceptable for the document sensitivity and workflow. <br>
Risk: A local ComPDF API key is required. <br>
Mitigation: Store the key only in the documented local key file and avoid placing it in code, logs, examples, or chat output. <br>
Risk: The package includes broad ComPDF API reference material beyond the Word-to-PDF operation. <br>
Mitigation: Before routine use, review or trim the references so the agent remains allowlisted to the Word-to-PDF endpoint. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF Word to PDF API Reference](https://www.compdf.com/guides/api-reference/v2/word-to-pdf) <br>
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow) <br>
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with endpoint, method, content type, request fields, expected task/result fields, and next polling or download step] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API request details and local API-key file setup guidance; does not output API keys.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

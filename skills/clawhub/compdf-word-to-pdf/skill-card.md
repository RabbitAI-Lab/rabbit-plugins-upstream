## Description:

Convert Word documents into polished PDFs with ComPDF. Use for contracts, reports, proposals, manuals, approvals, formal delivery, and Word-to-PDF requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document workflow teams use this skill to prepare ComPDF Server API requests that convert Word documents into stable PDFs for contracts, reports, proposals, manuals, approvals, and formal delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Word documents are uploaded to the third-party ComPDF service for processing.

Mitigation: Confirm the exact files and destination before upload, and avoid using the skill for sensitive or regulated documents unless that transfer is approved.

Risk: The skill uses a local ComPDF API key file for credentials.

Mitigation: Create or replace the skill-local api_key file only after user confirmation, exclude it from publishing, and do not display or log the key.

Risk: The bundled API reference covers many ComPDF endpoints beyond this skill's stated Word-to-PDF scope.

Mitigation: Use only the Word to PDF operation and the documented /server/v2/process/docx/pdf endpoint unless a separate skill or review authorizes another operation.

## Reference(s):

- [ComPDF Word to PDF API](https://www.compdf.com/guides/api-reference/v2/word-to-pdf)
- [ComPDF API Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-word-to-pdf)
- [ClawHub Publisher Profile](https://clawhub.ai/user/compdf-youna)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown request plan with endpoint, method, content type, request fields, response fields, and next polling or download step.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sourceType=5 in final ComPDF request details and avoids displaying API keys.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

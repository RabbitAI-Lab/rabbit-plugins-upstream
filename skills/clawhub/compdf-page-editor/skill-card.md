## Description:

Merge, split, rotate, insert, delete, and extract PDF pages with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare ComPDF Server API request plans for PDF page-management work such as document assembly, cleanup, restructuring, and selected-page output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDFs may be uploaded to ComPDF when a user authorizes a request.

Mitigation: Use the skill only with documents the user is allowed to send to ComPDF, identify affected files before upload, and obtain confirmation unless upload was already explicitly authorized.

Risk: The skill stores a ComPDF API key in a skill-local api_key file.

Mitigation: Keep the api_key file private, exclude it from publishing or version control, and do not display, log, or include the key in examples or final output.

Risk: Page-editing operations can restructure documents or remove pages.

Mitigation: Confirm destructive edits unless already authorized and preserve original files unless replacement is explicitly requested.

## Reference(s):

- [ComPDF Page Editor on ClawHub](https://clawhub.ai/compdf-youna/skills/compdf-page-editor)
- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF PDF API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with endpoint, method, content type, request fields, expected response fields, and follow-up polling or download steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF API request details and credential setup guidance, but should not expose API keys.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Convert PDF files into editable Word documents with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents use this skill to prepare ComPDF PDF-to-Word API request details for contracts, reports, forms, proposals, and other PDFs that need editable Word output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDFs may be uploaded to ComPDF for conversion.

Mitigation: Confirm the affected files and destination before upload, and avoid sensitive or regulated documents unless the user has explicitly approved that transfer.

Risk: The skill stores a ComPDF API key in a local api_key file.

Mitigation: Store only the skill-local key, do not display or log it, and keep it out of version control and published artifacts.

Risk: The bundled reference snapshot includes ComPDF endpoints beyond PDF-to-Word.

Mitigation: Keep use scoped to PDF-to-Word and use only the documented endpoint path, request fields, request mode, and response fields for that operation.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF PDF to Word API](https://www.compdf.com/guides/api-reference/v2/pdf-to-word)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Portal](https://www.compdf.com/compdf-portal/signin?utm_source=clawhub&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=clawhub_compdfkit_skills_en)
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-word)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration instructions, Shell commands]

**Output Format:** [Markdown with endpoint, method, content type, request fields, response fields, and next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ComPDF sourceType=5 routing details and preserves the user's original files unless replacement is explicitly requested.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

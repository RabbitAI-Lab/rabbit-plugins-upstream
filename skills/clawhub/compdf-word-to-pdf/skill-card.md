## Description:

Convert Word documents into polished PDFs with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and document workflow users use this skill to prepare ComPDF Server API request plans for converting Word documents into PDFs for contracts, reports, proposals, manuals, approvals, and formal delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected Word documents may be uploaded to ComPDF for processing.

Mitigation: Confirm affected files and destination before upload, and avoid highly confidential documents unless ComPDF's retention, region, and compliance terms fit the use case.

Risk: The skill stores a ComPDF API key in a local skill-specific api_key file.

Mitigation: Store only the current skill's key, keep it out of version control and published artifacts, and do not display or log the key.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-word-to-pdf)
- [ComPDF Portal](https://www.compdf.com/compdf-portal/signin?utm_source=clawhub&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=clawhub_compdfkit_skills_en)
- [ComPDF V2 Word to PDF API Reference](https://www.compdf.com/guides/api-reference/v2/word-to-pdf)
- [ComPDF V2 API Overview](https://www.compdf.com/guides/api-reference/v2/api-overview)
- [ComPDF V2 Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [Endpoint Index](references/endpoint-index.md)
- [Official API Reference Snapshot](references/official-api-reference.md)

## Skill Output:

**Output Type(s):** [guidance, API calls, configuration, shell commands]

**Output Format:** [Markdown with request details and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes endpoint, method, content type, request fields, expected task/result fields, and the next polling or download step.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

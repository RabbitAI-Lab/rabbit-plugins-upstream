## Description:

PDF Converter helps agents select ComPDF Server API endpoints and prepare request plans for supported PDF, document, and image conversion workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI agents, and operations teams use this skill to prepare accurate ComPDF API request plans for bidirectional document conversion. It is intended for supported conversion workflows and requires review before uploading documents to ComPDF.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents may be uploaded to ComPDF for conversion.

Mitigation: Review affected files before use and only approve uploads for documents appropriate to send to ComPDF.

Risk: The skill uses a local api_key file for ComPDF credentials.

Mitigation: Keep the skill-local api_key file private and do not display, log, commit, or include the key in examples.

## Reference(s):

- [ComPDF Endpoint Index](artifact/references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md)
- [ComPDF Conversion API Catalog](https://www.compdf.com/guides/api-reference/v2/api-overview)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/pdf-converter)

## Skill Output:

**Output Type(s):** [Text, Markdown, API request guidance, Configuration guidance]

**Output Format:** [Markdown request plan with endpoint, method, content type, request fields, response fields, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF request fields and polling or download steps; API keys should not be displayed.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

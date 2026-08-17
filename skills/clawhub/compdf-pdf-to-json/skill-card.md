## Description:

Convert PDF content into structured JSON with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration teams use this skill to prepare ComPDF Server API requests that convert PDF text, tables, images, and structured content into JSON for AI pipelines, applications, and system integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDFs may be uploaded to ComPDF for processing.

Mitigation: Review the affected files and destination before upload, and obtain confirmation for sensitive documents or any upload the user has not already authorized.

Risk: The skill stores a ComPDF API key in the skill directory as private runtime state.

Mitigation: Use only the skill-local api_key file, keep the key out of outputs and examples, and exclude private runtime state from version control and publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-json)
- [ComPDF Endpoint Index](artifact/references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md)
- [ComPDF PDF to JSON API](https://www.compdf.com/guides/api-reference/v2/pdf-to-json)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, JSON]

**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF request metadata such as endpoint path, method, content type, sourceType=5, task fields, polling, and download steps; API keys are not displayed.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

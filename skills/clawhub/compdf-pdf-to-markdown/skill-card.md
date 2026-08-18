## Description:

Convert PDF files into Markdown with ComPDF for knowledge-base ingestion, developer documentation, content repurposing, research workflows, and PDF-to-Markdown requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and content teams use this skill to prepare ComPDF Server API requests that convert selected PDF files into structured Markdown. It is suited to workflows that need readable Markdown for documentation, knowledge-base ingestion, summarization, publishing, or downstream text processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDF files are uploaded to ComPDF for processing.

Mitigation: Confirm the exact files and destination before upload, and use the documented secure or presigned workflow for sensitive documents.

Risk: The skill stores a ComPDF API key in a skill-local api_key file.

Mitigation: Keep the api_key file out of chats, logs, and shared repositories, and avoid displaying the key in request examples or final output.

Risk: PDF passwords or other document secrets may be needed for protected files.

Mitigation: Keep passwords out of shared logs and final responses, and request them only when needed for the selected operation.

## Reference(s):

- [ComPDF PDF to Markdown Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-markdown)
- [ComPDF V2 PDF to Markdown API Reference](https://www.compdf.com/guides/api-reference/v2/pdf-to-md)
- [ComPDF V2 Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF V2 Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Endpoint Index](artifact/references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint, method, content type, request fields, expected response fields, and polling or download steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final API request details include sourceType=5 and avoid exposing API keys, PDF passwords, or other secrets.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

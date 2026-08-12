## Description:

Convert PDF files into Markdown with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI agents, and content teams use this skill to prepare ComPDF PDF-to-Markdown API requests for knowledge-base ingestion, developer documentation, content repurposing, research workflows, and similar PDF-to-text pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDFs are uploaded to ComPDF for processing.

Mitigation: Use the skill only for documents whose transfer to ComPDF is allowed by the user's account, retention expectations, and compliance requirements; confirm affected files and destination before upload.

Risk: A ComPDF API key is stored as skill-local runtime state.

Mitigation: Store the key only in the sibling api_key file, exclude that file from publishing and version control, and never display or include the key in examples or final output.

Risk: Unsupported conversion options could produce incorrect request plans.

Mitigation: Use only the PDF-to-Markdown operation and the exact endpoint path, request fields, request mode, and response fields from the bundled ComPDF references.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF PDF to Markdown API](https://www.compdf.com/guides/api-reference/v2/pdf-to-md)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint, method, content type, request fields, expected task or result fields, and next polling or download steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final ComPDF request plans include sourceType=5 and omit API keys from examples and output.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

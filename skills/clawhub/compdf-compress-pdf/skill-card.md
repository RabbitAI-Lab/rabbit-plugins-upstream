## Description:

Compress PDF files with ComPDF while balancing file size and readable visual quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document workflow teams use this skill to prepare ComPDF Server API compression requests, tune quality and resolution settings, and choose optimization flags for smaller PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDFs are sent to ComPDF for compression.

Mitigation: Identify affected files and destination before upload, obtain user confirmation, and use asynchronous or presigned workflows for large or security-sensitive uploads.

Risk: The skill stores a ComPDF API key in a skill-local api_key file.

Mitigation: Store the key only after user confirmation, do not display it in examples or output, and keep it excluded from version control and skill publishing.

Risk: Aggressive optimization flags can remove annotations, metadata, forms, JavaScript actions, attachments, and other document features.

Mitigation: Explain quality and document-content tradeoffs before applying aggressive optimization and confirm destructive choices with the user.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF PDF Compression API](https://www.compdf.com/guides/api-reference/v2/compress-guides)
- [ComPDF Compression Parameters](https://www.compdf.com/guides/api-reference/v2/optimization-flags)
- [ComPDF Request Workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF Authentication](https://www.compdf.com/guides/api-reference/v2/authentication)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and optional cURL-style command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include the next polling or download step; excludes API keys and uploaded file contents.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

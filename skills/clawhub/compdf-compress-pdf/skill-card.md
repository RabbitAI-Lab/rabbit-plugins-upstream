## Description:

Compress PDF files with ComPDF while balancing file size and readable visual quality.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-operations teams use this skill to plan ComPDF Server API requests that reduce PDF file size while balancing visual quality, resolution, and optional removal of embedded document content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDFs are sent to ComPDF for processing.

Mitigation: Use the skill only for documents your organization approves for ComPDF handling, and avoid confidential or regulated files unless that handling is explicitly approved.

Risk: The skill reads a ComPDF API key from a documented local file.

Mitigation: Store the key only in the local key file, do not commit or display it, and pass it only through the x-api-key request header.

Risk: Returned download URLs may expose processed document outputs while valid.

Mitigation: Treat download URLs as sensitive until they expire and avoid sharing them in logs, tickets, or public messages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-compress-pdf)
- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF PDF API catalog](https://www.compdf.com/guides/api-reference/v2/api-overview-pdf)
- [ComPDF authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF compression guide](https://www.compdf.com/guides/api-reference/v2/compress-guides)
- [ComPDF compression flags](https://www.compdf.com/guides/api-reference/v2/optimization-flags)

## Skill Output:

**Output Type(s):** [guidance, API calls, shell commands, configuration]

**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ComPDF endpoint paths, HTTP method, content type, polling or download steps, and API-key file setup guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

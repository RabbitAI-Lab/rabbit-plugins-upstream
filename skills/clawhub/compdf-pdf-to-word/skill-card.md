## Description:

Convert PDF files into editable Word documents with ComPDF for contracts, reports, forms, proposals, review, revision, localization, and business reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, business teams, and AI agents use this skill to prepare scoped ComPDF PDF-to-Word API requests that turn PDFs into editable Word documents while preserving layout as much as possible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDFs are uploaded to ComPDF as an external third-party processor.

Mitigation: Use only documents the user is authorized to send externally, and choose the documented request workflow that fits the file size and sensitivity.

Risk: The skill depends on a local ComPDF API key file.

Mitigation: Keep the API key file private, do not log or display the key, and pass it only through the documented authentication header.

Risk: The bundled API reference covers more endpoints than this release is scoped to use.

Mitigation: Constrain agent use to the PDF-to-Word operation and verify fields against the supported operation before preparing a request.

## Reference(s):

- [ComPDF PDF To Word ClawHub page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-word)
- [ComPDF API authentication](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF request workflow](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ComPDF PDF to Word API](https://www.compdf.com/guides/api-reference/v2/pdf-to-word)
- [Endpoint index](references/endpoint-index.md)
- [Official API reference snapshot](references/official-api-reference.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with endpoint details, request fields, expected response fields, and next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces request plans and operational guidance; it does not directly convert files itself.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

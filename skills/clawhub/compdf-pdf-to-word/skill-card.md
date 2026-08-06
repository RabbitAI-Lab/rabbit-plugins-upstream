## Description:

Convert PDF files into editable Word documents with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business teams use this skill to prepare ComPDF PDF-to-Word API request plans for contracts, reports, forms, proposals, review, revision, localization, and business reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected PDFs are uploaded to ComPDF for conversion.

Mitigation: Use only documents approved for ComPDF processing and follow the documented asynchronous or presigned workflow for large, batch, or security-sensitive uploads.

Risk: A ComPDF API key is stored in a local key file.

Mitigation: Store the key only in the documented private key file or the COMPDF_API_KEY_FILE target, and do not print, commit, upload, or include it in examples.

Risk: The bundled API reference includes many ComPDF endpoints beyond PDF to Word.

Mitigation: Use the skill for PDF-to-Word tasks only unless the user separately requests and reviews another operation.

## Reference(s):

- [ComPDF Endpoint Index](artifact/references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md)
- [ComPDF PDF to Word API Reference](https://www.compdf.com/guides/api-reference/v2/pdf-to-word)
- [ComPDF Authentication Reference](https://www.compdf.com/guides/api-reference/v2/authentication)
- [ComPDF Request Workflow Reference](https://www.compdf.com/guides/api-reference/v2/request-workflow)
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-pdf-to-word)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown text with endpoint details, request fields, response fields, and next-step guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not expose API keys; limited to PDF-to-Word request planning.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

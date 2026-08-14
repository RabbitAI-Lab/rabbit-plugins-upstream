## Description:

ComPDF Documents to PDF helps agents prepare ComPDF Server API requests to convert Word, Excel, PPT, HTML, TXT, CSV, RTF, PNG, and JPG files into PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, business users, and agent operators use this skill to standardize supported office, text, data, web, and image files into fixed-layout PDF outputs for sharing, approvals, printing, and archiving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes broad ComPDF API references for capabilities outside the advertised document-to-PDF scope.

Mitigation: Limit use to Word, Excel, PPT, HTML, TXT, CSV, RTF, PNG, and JPG to PDF endpoints, and do not use editing, decryption, watermark removal, reverse conversion, or AI extraction endpoints under this skill.

Risk: Using the skill may require uploading documents or images to ComPDF.

Mitigation: Identify the affected files and destination, confirm each upload with the user, and avoid sensitive documents unless the organization permits sending them to ComPDF.

Risk: The skill uses a ComPDF API key for authenticated requests.

Mitigation: Keep the key in the skill-local api_key file only, and do not display, log, commit, or include it in examples or final output.

## Reference(s):

- [ComPDF Endpoint Index](references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md)
- [ComPDF Documents to PDF on ClawHub](https://clawhub.ai/compdf-youna/skills/compdf-documents-to-pdf)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown request plans with endpoint, method, request fields, response fields, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exact ComPDF API request details and upload or polling steps; requires user confirmation before document uploads.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

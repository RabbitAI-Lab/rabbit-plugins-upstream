## Description:

Add or remove text and image watermarks in PDFs with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document operations teams use this skill to prepare ComPDF Server API requests for adding or removing PDF watermarks used in branding, draft review, document control, and final-delivery cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a local ComPDF API key file; exposing that key could allow API use under the user's account.

Mitigation: Store the key only in the documented local key file, pass it only as the x-api-key header, and never include it in code, logs, examples, or chat output.

Risk: Selected PDFs are sent to ComPDF for watermark processing, which can expose confidential or regulated documents to an external service.

Mitigation: Use the skill only for intended watermark add or remove tasks and confirm before uploading confidential or regulated files.

Risk: Watermark removal or replacement can alter document control markings.

Mitigation: Confirm authorization and affected files before removal or replacement, and preserve originals unless replacement is explicitly requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/compdf-youna/skills/compdf-add-watermark-remover-watermark)
- [ComPDF endpoint index](references/endpoint-index.md)
- [Official ComPDF V2 API reference snapshot](references/official-api-reference.md)
- [ComPDF add watermark API guide](https://www.compdf.com/guides/api-reference/v2/watermark-guides)
- [ComPDF remove watermark API guide](https://www.compdf.com/guides/api-reference/v2/del-watermark-guides)
- [ComPDF authentication guide](https://www.compdf.com/guides/api-reference/v2/authentication)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown request plan with endpoint, method, headers, request fields, response fields, and follow-up polling or download steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill should not expose API keys and should request confirmation before external upload, overwrite, deletion, or watermark removal when authorization is not already explicit.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

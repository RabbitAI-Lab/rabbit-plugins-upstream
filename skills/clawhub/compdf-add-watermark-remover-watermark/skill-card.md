## Description:

Add or remove text and image watermarks in PDFs with ComPDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[compdf-youna](https://clawhub.ai/user/compdf-youna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, document operations teams, and external users use this skill to prepare ComPDF Server API request plans for adding or removing PDF watermarks during branding, review, cleanup, and final-delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled ComPDF reference includes capabilities outside watermark management and could steer an agent toward unrelated PDF operations.

Mitigation: Restrict use to the add-watermark and remove-watermark endpoints listed by the skill, and validate each request path against the watermark reference sections.

Risk: Using the skill can involve sending selected PDFs to ComPDF.

Mitigation: Confirm affected files and destination before upload, and avoid confidential or regulated documents unless ComPDF is approved for that data.

Risk: The skill uses a ComPDF API key stored as local runtime state.

Mitigation: Store only the skill-local API key file, exclude it from publishing and version control, and never display, log, or include the key in examples.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-add-watermark-remover-watermark)
- [ComPDF Endpoint Index](artifact/references/endpoint-index.md)
- [Official ComPDF V2 API Reference Snapshot](artifact/references/official-api-reference.md)
- [ComPDF Add Watermark API](https://www.compdf.com/guides/api-reference/v2/watermark-guides)
- [ComPDF Remove Watermark API](https://www.compdf.com/guides/api-reference/v2/del-watermark-guides)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown request plan with endpoint, method, fields, response expectations, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill should preserve original files unless replacement is explicitly requested.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

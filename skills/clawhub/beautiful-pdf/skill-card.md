## Description:

Produce polished, print-ready PDFs from Markdown or HTML with Pandoc, WeasyPrint, reusable CSS, and a mandatory rendered-page review loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, developers, and agents use this skill to turn Markdown or static HTML into polished PDFs for reports, proposals, briefs, CVs, invoices, letters, and dossiers, with rendered-page inspection before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private documents and generated page images may expose sensitive content if processed or shared outside an approved environment.

Mitigation: Use the helper only on documents the user is allowed to process, and keep private PDFs, source files, and rasterized page images private.

Risk: Large PDFs or unusually high DPI rasterization can consume significant local resources.

Mitigation: Use normal DPI settings where possible and process unusually large or untrusted PDFs in a constrained environment.

Risk: Missing Pandoc, WeasyPrint, or PyMuPDF dependencies can prevent rendering or page inspection.

Mitigation: Report missing requirements explicitly and avoid silently installing dependencies.

## Reference(s):

- [Document Type Guide](references/doc-types.md)
- [PDF Style Guide](references/style-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or static HTML source, CSS adjustments, shell commands, PDF files, PNG page images, and concise review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final delivery should include the PDF path, page count, preserved editable source, and visual issues checked.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

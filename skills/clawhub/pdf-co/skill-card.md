## Description:

Helps agents use PDF.co through a user-authorized Maton connection to convert, assemble, edit, and extract data from PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can direct an agent to convert, merge, split, edit, or extract information from PDFs using their authorized PDF.co connection. Optional automation can run approved PDF.co actions on a schedule or supported external events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF documents and extracted data may be sent to an external processor or exposed through output links.

Mitigation: Obtain approval for each document and avoid sensitive or regulated material; do not share output links for sensitive documents.

Risk: Automations and event destinations can continue processing or forwarding data after setup.

Mitigation: Use direct API calls for routine work; separately approve the connection, destination, and any code before enabling automation.

## Reference(s):

- [PDF.co API documentation](https://docs.pdf.co)
- [PDF.co API reference](https://docs.pdf.co/api-reference)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [ClawHub PDF.co skill](https://clawhub.ai/byungkyu/skills/pdf-co)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API results may include temporary document links.]

## Skill Version(s):

1.2.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

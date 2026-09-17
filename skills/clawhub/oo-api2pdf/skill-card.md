## Description:

API2PDF (api2pdf.com) routes API2PDF tasks through an OOMOL-connected account, including Markdown-to-PDF conversion that returns generated PDF URLs and conversion metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate API2PDF through an OOMOL-connected account, primarily to convert raw Markdown into a PDF and receive the generated PDF URL plus metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Markdown content is sent to API2PDF through OOMOL for conversion.

Mitigation: Use the skill only when the user is comfortable sending the Markdown content to the external PDF service.

Risk: The setup guidance includes pipe-to-shell installer commands.

Mitigation: Avoid running installer commands unless the installer source and integrity have been separately verified.

## Reference(s):

- [API2PDF homepage](https://www.api2pdf.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub API2PDF skill page](https://clawhub.ai/oomol/skills/oo-api2pdf)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generated PDF URLs and conversion metadata from API2PDF through OOMOL.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

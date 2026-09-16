## Description:

PDF.co helps agents operate PDF.co through an OOMOL-connected account for PDF reading, creation, conversion, compression, splitting, and merging tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run PDF.co document operations from an agent through the OOMOL oo CLI. It supports PDF compression, metadata inspection, text extraction, splitting, merging, and PDF creation from HTML or public URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include running remote installer scripts directly in a shell.

Mitigation: Before installing, prefer an official package-manager or verified release path for the oo CLI instead of piping downloaded scripts directly into a shell.

Risk: PDF.co work is routed through OOMOL and may include write-action payloads such as PDF merging.

Mitigation: Use this skill only when PDF.co work is intended to go through OOMOL, and review write-action payloads before approving them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pdf-co)
- [PDF.co Homepage](https://pdf.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and generated PDF or text output URLs.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

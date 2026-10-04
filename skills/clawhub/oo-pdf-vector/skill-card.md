## Description:

Use this skill for PDF Vector (pdfvector.com) requests involving searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate PDF Vector through an OOMOL-connected account for asking questions about public PDFs, extracting structured JSON from public PDFs, and parsing public PDFs into Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public document URLs, questions, and extraction schemas are sent through the OOMOL PDF Vector connector.

Mitigation: Use public PDF URLs and avoid sending sensitive document details unless the connected OOMOL and PDF Vector account is approved for that data.

Risk: First-time setup may ask the user to run a remote installer command for the oo CLI.

Mitigation: Review the installer source or use the vendor's documented installation method before running one-time setup commands.

## Reference(s):

- [PDF Vector homepage](https://www.pdfvector.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pdf-vector)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

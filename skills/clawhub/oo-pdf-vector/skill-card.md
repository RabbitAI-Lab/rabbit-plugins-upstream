## Description:

PDF Vector lets agents ask questions about public PDF documents, extract schema-shaped JSON, and parse documents to Markdown through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate PDF Vector on public document URLs for question answering, structured extraction, and Markdown parsing through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remotely fetched installer scripts directly in a shell.

Mitigation: Review the OOMOL oo CLI installation path before installation and prefer a verified package-manager, checksum, or signature-based install when available.

Risk: PDF actions send document URLs and requested extraction tasks through PDF Vector and OOMOL-connected services.

Mitigation: Use only documents intended for PDF Vector/OOMOL processing and connect the PDF Vector API key only when the publisher and connector path are trusted.

## Reference(s):

- [PDF Vector homepage](https://www.pdfvector.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pdf-vector)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before submitting JSON requests; connector responses include data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

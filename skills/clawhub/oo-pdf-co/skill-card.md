## Description:

PDF.co helps agents inspect, transform, generate, merge, split, compress, and extract text from PDF documents through an OOMOL-connected PDF.co account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow authors use this skill to operate PDF.co through OOMOL for PDF compression, merging, splitting, metadata inspection, HTML or URL to PDF conversion, text extraction, and account balance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may require installing and trusting OOMOL's CLI distribution before actions can run.

Mitigation: Review the skill before installing, use only trusted OOMOL CLI distribution paths, and require explicit approval before installation or sign-in.

Risk: PDF.co actions can create files, transform or upload documents, and consume credits.

Mitigation: Require explicit approval before file-creating, document-transforming, uploading, or credit-consuming actions, and confirm payload and effect for write-tagged actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pdf-co)
- [PDF.co homepage](https://pdf.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector actions may return URLs, inline text, account balance data, or generated PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, OOMOL sign-in, a connected PDF.co account, and explicit approval for file-creating, document-transforming, upload, or credit-consuming actions.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

ChatPDF lets an agent inspect ChatPDF connector schemas, import public PDF URLs, ask stateless questions about imported sources, and delete sources through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use ChatPDF to import publicly reachable PDFs, ask questions about imported sources, and remove sources from a ChatPDF account through an OOMOL-connected CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Review the installer path, prefer a trusted package manager or verified release, and avoid running installer commands in an elevated shell.

Risk: The skill can import PDFs into ChatPDF and delete existing ChatPDF sources.

Mitigation: Inspect the live action schema, confirm the exact payload and effect with the user before imports, and require explicit approval before deletions.

## Reference(s):

- [ChatPDF homepage](https://www.chatpdf.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chatpdf)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with bash and PowerShell command examples and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When connector actions run, responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

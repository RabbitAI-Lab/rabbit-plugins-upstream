## Description:

TemplateDocs (templatedocs.io) helps agents read, create, update, generate, and delete TemplateDocs data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TemplateDocs through an OOMOL-connected account, including listing templates, retrieving template metadata, generating DOCX or PDF documents, updating template settings, and deleting templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can run remote installer scripts for the oo CLI.

Mitigation: Review the CLI setup path before installation and prefer a verified package or official instructions with checksum or signature verification.

Risk: TemplateDocs write and destructive actions can generate documents, update template settings, or permanently delete templates.

Mitigation: Approve write or delete actions only after checking the exact target template, action name, and JSON payload.

## Reference(s):

- [TemplateDocs homepage](https://templatedocs.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-templatedocs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; generated documents may be returned through file transit.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

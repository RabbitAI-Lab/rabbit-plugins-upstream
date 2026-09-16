## Description:

Docsumo helps agents use the OOMOL-connected Docsumo connector to read, create, and update Docsumo data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Docsumo through an OOMOL-connected account, including account inspection, document listing, document detail retrieval, extracted data access, summaries, and URL-based document uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Use a trusted, version-pinned, verifiable oo CLI installation path before running connector actions.

Risk: The upload_document_from_url action changes Docsumo state.

Mitigation: Confirm the exact URL, document type, and expected effect with the user before running uploads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-docsumo)
- [Docsumo Homepage](https://www.docsumo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Docsumo action schemas before constructing request payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

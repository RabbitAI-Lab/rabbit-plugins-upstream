## Description:

AlgoDocs helps agents operate AlgoDocs through an OOMOL-connected account to read extracted document data, list account resources, and upload public document URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate AlgoDocs from an agent through the OOMOL `oo` CLI. It supports reading extractors, folders, extracted data, account identity, and importing a public document URL into AlgoDocs after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands, which creates supply-chain risk if run without verification.

Mitigation: Prefer the official install guide and verify package integrity with available checksums or signatures before installing the `oo` CLI.

Risk: `upload_document_from_url` changes AlgoDocs account state by importing a document URL.

Mitigation: Confirm the exact URL, extractor, folder, and expected effect with the user before running the upload action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-algo-docs)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [AlgoDocs homepage](https://algodocs.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses `oo connector schema` to inspect action contracts before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

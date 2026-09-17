## Description:

Provides Moorcheh access through the OOMOL oo CLI connector for searching, retrieving, uploading, creating, and deleting text data in Moorcheh namespaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Moorcheh through an OOMOL-connected account, including listing namespaces, searching text, retrieving documents, uploading text documents, creating namespaces, and deleting documents with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may pipe a remote installer directly into a shell.

Mitigation: Review the oo CLI installation path and prefer official, versioned, verifiable installation instructions before installing.

Risk: Moorcheh upload, namespace creation, and document deletion actions can change or remove user data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before any write or destructive action.

## Reference(s):

- [Moorcheh homepage](https://www.moorcheh.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Moorcheh ClawHub skill page](https://clawhub.ai/oomol/skills/oo-moorcheh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

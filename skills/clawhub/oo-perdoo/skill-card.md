## Description:

Perdoo lets agents read, create, and update Perdoo data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Perdoo goals and progress updates from an agent after connecting their Perdoo account through OOMOL. It supports goal retrieval, listing, GraphQL operations, and confirmed progress-update writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad mutation capability through Perdoo GraphQL operations and progress update writes.

Mitigation: Require explicit confirmation of the exact operation, variables, target records, and expected effect before any write or mutation.

Risk: The artifact includes pipe-to-shell installer guidance for first-time oo CLI setup.

Mitigation: Install only after independently verifying the official install method and trusting OOMOL and the requested Perdoo connection scope.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-perdoo)
- [Perdoo Homepage](https://www.perdoo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Perdoo Connection](https://console.oomol.com/app-connections?provider=perdoo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may call Perdoo through the OOMOL oo CLI and can return JSON responses.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Parma (parma.ai). Use this skill for ANY Parma request, including reading, creating, updating, and deleting data through the OOMOL-connected Parma connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate on data in a connected Parma workspace through OOMOL's oo CLI, including reads, relationship and note updates, group assignment, and explicitly confirmed destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may require executing a remote oo CLI installer.

Mitigation: Install only from an official, verifiable OOMOL CLI distribution path and review the installer before running it.

Risk: The connector can create, update, and delete data in a connected Parma workspace.

Mitigation: Require explicit user confirmation for every create, update, or delete action, and confirm the exact target and payload before destructive actions.

## Reference(s):

- [Parma homepage](https://parma.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Parma connection](https://console.oomol.com/app-connections?provider=parma)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Parma action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

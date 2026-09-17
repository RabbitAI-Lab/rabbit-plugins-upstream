## Description:

TriliumNext Notes helps agents read, create, update, and delete TriliumNext Notes data through OOMOL-connected CLI actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate TriliumNext Notes from an agent session, including searching notes, reading content, managing branches, attributes, and attachments, and performing confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include direct execution of unverified remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installation, prefer an official versioned, signed, or checksum-verified installation method, and do not allow an agent to run the remote installer automatically.

Risk: Write and destructive actions can change or delete Trilium notes, branches, attributes, attachments, or note content.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, and require explicit approval before destructive actions run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trilium)
- [TriliumNext Notes homepage](https://triliumnotes.org)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents inspect live action schemas before building payloads and should obtain confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

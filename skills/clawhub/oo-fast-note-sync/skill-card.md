## Description:

Fast Note Sync lets an agent read, create, update, delete, and manage Fast Note Sync notes, vaults, and attachments through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Fast Note Sync from an agent session, including vault, note, and attachment listing, search, creation, updates, uploads, downloads, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote oo CLI installer.

Mitigation: Install only when the oo CLI is missing, and verify the installer through official OOMOL documentation before running it.

Risk: The connected account can create, overwrite, or delete Fast Note Sync data.

Mitigation: Require explicit user confirmation for write or destructive actions, including the exact target, payload, and expected effect.

Risk: Action payloads can drift from the current connector contract.

Mitigation: Fetch the live connector schema before execution and build payloads to match that schema.

## Reference(s):

- [ClawHub Fast Note Sync Skill](https://clawhub.ai/oomol/skills/oo-fast-note-sync)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Fast Note Sync Homepage](https://github.com/haierkeys/fast-note-sync-service)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

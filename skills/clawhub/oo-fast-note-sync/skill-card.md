## Description:

Fast Note Sync lets an agent read, create, update, delete, search, and manage Markdown notes, vaults, and attachment metadata through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected Fast Note Sync account from an agent, including note, vault, and attachment workflows. It is suited for account-scoped note management where read actions can run directly and write or destructive actions require confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote oo CLI installer scripts.

Mitigation: Install only from a trusted OOMOL distribution path, prefer a verified package or inspect the installer first, and avoid administrator privileges unless necessary.

Risk: Write and destructive actions can create, overwrite, delete, or permanently remove Fast Note Sync data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running actions tagged write or destructive.

Risk: Connector actions operate against the user's connected Fast Note Sync account.

Mitigation: Inspect the live action schema before submitting JSON payloads and run authentication or connection setup only after a command fails for that reason.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fast-note-sync)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Fast Note Sync Homepage](https://github.com/haierkeys/fast-note-sync-service)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before payload construction; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Fast Note Sync lets an agent use the OOMOL oo CLI to read, create, update, delete, search, and manage Fast Note Sync notes, vaults, and attachment metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with connected OOMOL and Fast Note Sync accounts use this skill to operate note vaults, Markdown notes, and attachments through the oo CLI while confirming write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include remote installer commands that download and execute scripts directly in a shell.

Mitigation: Install the oo CLI through a trusted, reviewed, integrity-checked method and avoid allowing an agent to run the remote installer commands automatically.

Risk: The skill can write to or delete Fast Note Sync notes, vaults, and attachments.

Mitigation: Require explicit user confirmation for every write or destructive action, including the exact target and JSON payload.

## Reference(s):

- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Fast Note Sync homepage](https://github.com/haierkeys/fast-note-sync-service)
- [Fast Note Sync ClawHub page](https://clawhub.ai/oomol/skills/oo-fast-note-sync)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can execute oo CLI connector actions that return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

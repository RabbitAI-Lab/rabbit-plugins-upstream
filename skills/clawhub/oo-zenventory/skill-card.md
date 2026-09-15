## Description:

Zenventory helps agents operate Zenventory through an OOMOL-connected account for reading, creating, listing, searching, and updating inventory items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Zenventory inventory records through the OOMOL `oo` CLI. It supports schema inspection, JSON-based connector actions, and guarded create and update workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer scripts executed directly in a shell.

Mitigation: Review the installer path before installing, and prefer an official package manager, signed release, or downloaded installer with checksum or signature verification.

Risk: Create and update actions can change Zenventory data.

Mitigation: Confirm exact create or update payloads and intended effects before allowing the skill to modify Zenventory records.

## Reference(s):

- [Zenventory homepage](https://www.zenventory.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zenventory skill on ClawHub](https://clawhub.ai/oomol/skills/oo-zenventory)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when actions are run with `--json`.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

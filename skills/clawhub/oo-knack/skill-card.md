## Description:

Knack (knack.com). Use this skill for ANY Knack request: reading, creating, updating, and deleting data through the OOMOL Knack connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators who manage Knack applications use this skill to inspect live connector schemas and run record create, retrieve, list, update, and delete workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance tells users to run remote installer scripts directly in a shell.

Mitigation: Review the installer path before use; prefer a verified package or a downloaded installer with a published checksum or signature.

Risk: Write and delete actions can modify or remove Knack records.

Mitigation: Confirm the exact Knack object, record ID, and payload before allowing write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-knack)
- [Knack Homepage](https://www.knack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON payloads, guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Embase (elsevier.com). Use this skill for ANY Embase request: searching and reading data through an OOMOL-connected Embase account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Embase biomedical literature and retrieve individual article records through the OOMOL `embase` connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Install the oo CLI only from trusted OOMOL sources, prefer checksum- or signature-verified installation methods, and avoid elevated privileges unless clearly required.

Risk: Connector action payloads can become stale if Embase connector schemas change.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing or running each payload.

## Reference(s):

- [Embase ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-embase)
- [Embase Homepage](https://www.elsevier.com/products/embase)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; Embase responses are returned through the oo CLI JSON wrapper.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

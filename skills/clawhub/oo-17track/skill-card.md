## Description:

17TRACK (17track.net). Use this skill for ANY 17TRACK request - reading, creating, and updating data. Whenever a task involves 17TRACK, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage 17TRACK shipments through an OOMOL-connected account, including quota checks, shipment detail retrieval, tracking lists, and registering tracking numbers for monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review the OOMOL CLI installation path first and prefer official, versioned, signed, or checksum-verified installation instructions.

Risk: The register_trackings action changes 17TRACK account state by registering tracking numbers for monitoring.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [17TRACK homepage](https://www.17track.net/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-17track)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Positionstack helps agents use OOMOL's oo CLI to inspect and run Positionstack connector actions for forward and reverse geocoding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform Positionstack geocoding tasks through an OOMOL-connected account, including converting addresses or place names to coordinates and resolving coordinates or IP inputs to location results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad oo CLI command authority.

Mitigation: Install and use it only where broad oo CLI access is acceptable, and review the exact Positionstack action before execution.

Risk: The setup guidance includes remote installer commands that are not independently verified in the evidence.

Mitigation: Install the oo CLI from a trusted, verifiable source and prefer a version-pinned or checksum-verified installation path.

Risk: Address, coordinate, or IP lookup data may be sent to the connected Positionstack service.

Mitigation: Confirm the intended action and payload before sending location-related data.

## Reference(s):

- [Positionstack homepage](https://positionstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-positionstack)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

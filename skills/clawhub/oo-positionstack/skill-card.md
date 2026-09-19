## Description:

Positionstack enables agents to operate OOMOL-managed Positionstack geocoding actions through the oo CLI for forward and reverse geocoding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to inspect Positionstack connector schemas and run forward or reverse geocoding actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands.

Mitigation: Review the setup path before installing and prefer a trusted, versioned oo CLI source with checksum or signature verification.

Risk: Geocoding requests may include personal addresses, precise coordinates, or identifiable IP addresses.

Mitigation: Send sensitive location or IP data only when the user is comfortable with OOMOL and Positionstack processing that data.

Risk: The forward geocoding action is tagged as write-capable in the artifact.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [Positionstack ClawHub Skill](https://clawhub.ai/oomol/skills/oo-positionstack)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Positionstack Homepage](https://positionstack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads; connector responses include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
